import argparse

from sys import argv
from pylsl import StreamInfo, StreamOutlet, local_clock
from .quicklink_types import QLDeviceId, QLDeviceInfo, QL_ERROR_OK, QLFrameData, errorToString

from ctypes import CDLL, pointer
from .utils import getDataSampleFromFrame, getImageSampleFromFrame, initDataOutlet, initVideoOutlet
from .constants import CHANNEL_METADATA, CHANNEL_NAMES, DEFAULT_CONFIG_FILENAME, EXAMPLE_CONFIG_FILENAME, QUICKLINK_POLL_TIME_MS
from .utils import initQuicklink2

def run(quicklink2_api: CDLL, device_info: QLDeviceInfo, device_id: QLDeviceId, srate: int, video: bool, verbose: bool):
    device_serial_number = device_info.serialNumber.decode("utf-8")
    frame = (QLFrameData)()
    frame_ptr = pointer(frame)
    # ms to wait for a new frame before throwing a QL_ERROR_TIMEOUT_ELAPSED
    received_samples = 0
    data_outlet = initDataOutlet(serial_number=device_serial_number, srate=srate)
    
    def getFrame():
        # Blocking call
        ret_val = quicklink2_api.QLDevice_GetFrame(device_id, QUICKLINK_POLL_TIME_MS, frame_ptr)
        if (ret_val != QL_ERROR_OK):
            raise ValueError(errorToString(ret_val))
        return True

    # The image dimensions (=> LSL channel size) can only be determined after we receive the first frame
    video_outlet = None
    if video and getFrame():
        dims = frame.ImageData.Height, frame.ImageData.Width
        video_outlet = initVideoOutlet(serial_number=device_serial_number, dims=dims)
    while getFrame():
        sample = getDataSampleFromFrame(frame)
        data_outlet.push_sample(sample)
        
        if video:
            image = getImageSampleFromFrame(frame)
            video_outlet.push_chunk(image)
        if verbose and received_samples % 250 == 0:
            sample_dict = dict(zip(CHANNEL_NAMES, sample))
            print(f"Pushed sample #{received_samples}:\n{sample_dict}\n")
        received_samples += 1

def init(srate=60, config_filename=DEFAULT_CONFIG_FILENAME, video=False, verbose=False):
    quicklink2_api, device_info, device_id = initQuicklink2()
    try:
        run(quicklink2_api=quicklink2_api, 
            device_info=device_info, 
            device_id=device_id,
            srate=srate,
            video=video,
            verbose=verbose)
    except KeyboardInterrupt:
        print("Shutdown signal received. Stopping Quicklink2...")
        ret = quicklink2_api.QLDevice_Stop_All()
        if(ret != QL_ERROR_OK):
            raise ValueError(errorToString(ret))
        print("Shutdown complete.")
