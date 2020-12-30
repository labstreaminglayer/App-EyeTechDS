import numpy as np
from pylsl import StreamInfo, StreamOutlet
from os.path import isfile, isdir
from glob import glob
from ctypes import c_int, c_float, c_char, c_void_p
from ctypes import create_string_buffer, CDLL, pointer, sizeof

from .quicklink_types import QLSettingsId, QLDeviceId, QLDeviceInfo, QLFrameData
from .quicklink_types import infoToString, errorToString, imageDataToString
from .quicklink_types import QL_ERROR_OK, QL_ERROR_INTERNAL_ERROR

from .constants import CHANNEL_METADATA, CHANNEL_NAMES, DEFAULT_CONFIG_FILENAME, EXAMPLE_CONFIG_FILENAME, SDK_URL

def is64bitOS():
    """
    Returns True if the size of a void pointer is 8 bits (64 bit system),
    False otherwise
    """
    return sizeof(c_void_p) == 8

def initDataOutlet(serial_number: str, srate: int=60) -> StreamOutlet:
    """
    Returns an outlet for the device data.

    Args:
        serial_number (int):
            The serial number of the device to set as the LSL stream ID.
        srate int:
            The sampling rate of the video stream.
    Returns:
        video_outlet (StreamOutlet): A pylsl.StreamOutlet
    """
    if len(serial_number) == 0:
        raise ValueError("Empty serial number specified")
    stream_id = 'eyetechds_SN#' + serial_number
    data_stream_info = StreamInfo(
        name='EyeTechDS Data',
        type='Gaze',
        channel_count=len(CHANNEL_NAMES),
        channel_format='float32',
        nominal_srate=srate,
        source_id=stream_id)
    acquisition = data_stream_info.desc().append_child("acquisition")
    acquisition.append_child_value("manufacturer", "EyeTechDS")
    acquisition.append_child_value("model", "VT3-Mini")
    acquisition.append_child_value("application", "LSL EyeTechDS")

    channels = data_stream_info.desc().append_child("channels")
    for chn_data in CHANNEL_METADATA:
        ch = channels.append_child("channel")
        ch.append_child_value("label", chn_data['label'])
        ch.append_child_value("eye", chn_data['eye'])
        ch.append_child_value("unit", chn_data['unit'])
        ch.append_child_value("type", chn_data['type'])

    data_outlet = StreamOutlet(data_stream_info)
    return data_outlet
    
def initVideoOutlet(serial_number: str, dims: tuple) -> StreamOutlet:
    """
    Returns an outlet for the video data.

    Args:
        serial_number (int):
            The serial number of the device to set as the LSL stream ID.
        dims (tuple[int, int]):
            The nominal sampling rate of the data stream.
    Returns:
        video_outlet (StreamOutlet): A pylsl.StreamOutlet
    """
    if len(serial_number) == 0:
        raise ValueError("Empty serial number specified")
    w, h = dims
    video_stream_id = 'eyetechds_video_SN#' + str(serial_number)
    video_stream_info = StreamInfo(
        name='EyeTechDS Video',
        type='VideoRaw',
        channel_count=w * h,
        channel_format='int8',
        source_id=video_stream_id)
    
    encoding = video_stream_info.desc().append_child("encoding")
    encoding.append_child_value("width", str(w))
    encoding.append_child_value("height", str(h))
    encoding.append_child_value("color_channels", "1")
    encoding.append_child_value("color_format", "GRAY")
    encoding.append_child_value("codec", "RAW")

    acquisition = video_stream_info.desc().append_child("acquisition")
    acquisition.append_child_value("manufacturer", 'EyeTechDS')
    acquisition.append_child_value("serial_number", serial_number)

    video_outlet = StreamOutlet(video_stream_info)
    return video_outlet

def getImageSampleFromFrame(frame: QLFrameData) -> np.array:
    """
    Returns a numpy array from the given QLFrameData

    Args:
        frame (QLFrameData): The frame data object from the Quicklink2 device
    Returns:
        imgData (np.array): A 1-dimensional numpy array containing the greyscale image data
    """
    w, h = frame.ImageData.Height, frame.ImageData.Width
    imgData = np.ctypeslib.as_array(frame.ImageData.PixelData,
            shape=(1, h * w))
    imgData = imgData.astype('int8', order='C')
    return imgData


def getDataSampleFromFrame(frame: QLFrameData) -> np.array:
    """
    Returns the computed data sample in the same order as CHANNEL_NAMES

    Args:
        frame (QLFrameData): The frame data object from the Quicklink2 device
    Returns:
        sample (np.array): A 1-dimensional numpy array containing the sample data
    """
    l, r, wgp = frame.LeftEye, frame.RightEye, frame.WeightedGazePoint
    sample = np.array([
        float(l.Found),
        float(l.Calibrated),
        l.PupilDiameter,
        l.Pupil.x,
        l.Pupil.y,
        l.Glint0.x,
        l.Glint0.y,
        l.Glint1.x,
        l.Glint1.y,
        l.GazePoint.x,
        l.GazePoint.y,

        float(r.Found),
        float(r.Calibrated),
        r.PupilDiameter,
        r.Pupil.x,
        r.Pupil.y,
        r.Glint0.x,
        r.Glint0.y,
        r.Glint1.x,
        r.Glint1.y,
        r.GazePoint.x,
        r.GazePoint.y,

        float(wgp.Valid),
        wgp.x,
        wgp.y,
        wgp.LeftWeight,
        wgp.RightWeight,

        frame.Focus,
        frame.Distance
    ])
    return sample



def initQuicklink2(config_filename=DEFAULT_CONFIG_FILENAME):
    """
    Loads the QuickLINK2 dll & initializes the device with
    the specified configuration file (if any).

    Args:
        config_filename str:
            The name of the settings file. Defaults to 'quicklink2_api_config'
    Returns:
        tuple(quicklink2_api: CDLL, device_info: QLDeviceInfo, device_id: QLDeviceID)
    Raises:
        FileNotFoundError: If a user-specified configuration file is not found
    """
    lib_paths = []
    found_dll_in_program_files = False
    if is64bitOS():
        base_path = r"C:\Program Files\EyeTechDS"
        lib_paths = glob(base_path + r"\QuickLINK*\*64*\QuickLink2.dll")
        if isdir(base_path) and len(lib_paths) > 0:
            found_dll_in_program_files = True
    else:
        base_path = r"C:\Program Files (x86)\EyeTechDS"
        lib_paths = glob(base_path + r"\QuickLINK*\bin\QuickLink2.dll")
        if isdir(base_path) and len(lib_paths) > 0:
            found_dll_in_program_files = True

    if not found_dll_in_program_files:
        lib_paths = glob('./QuickLink2.dll')
        if len(lib_paths) == 0:
            raise EnvironmentError(
                f"Unable to find QuickLink2.dll. Please install the QuickLink2 SDK from\n{SDK_URL}\n\t OR include QuickLink2.dll in the root folder of this application.")
    quicklink2_api: CDLL = None

    # Assume multiple libary versions were found
    for i, lib_path in enumerate(lib_paths):
        quicklink2_api = CDLL(lib_path)
        if(quicklink2_api == 0 and i == len(lib_paths) - 1):
            raise ValueError('No valid QuickLink2.dll was found.')
        else:
            break
        
    # Get the Quicklink 2 API version
    buff_size = 128
    version_str = create_string_buffer(buff_size)
    ret_val = quicklink2_api.QLAPI_GetVersion(c_int(buff_size), version_str)
    if(ret_val != QL_ERROR_OK):
        raise ValueError(errorToString(ret_val))
    else:
        print("Quicklink2 API Version: ", version_str.value.decode("utf-8"))

    # Pass in a buffer of 10 DeviceId's
    device_id = QLDeviceId()
    num_devices = c_int(10)
    num_devices_ptr = pointer(num_devices)
    device_buffer = (num_devices.value * QLDeviceId)()
    device_buffer_ptr = pointer(device_buffer)
    ret_val = quicklink2_api.QLDevice_Enumerate(num_devices_ptr, device_buffer_ptr)
    if(ret_val != QL_ERROR_OK):
        raise ValueError(errorToString(ret_val))
    else:
        print("Num of devices found:", num_devices.value)
        for num in range(0, num_devices.value):
            print("Device ID:", device_buffer[num])
        device_id = device_buffer[0]
    if(device_id == 0):
        raise ValueError('No devices found')

    # Retrieve the device_info containing the device model / serial no. / sensor W x H (px)
    device_info = (QLDeviceInfo)()
    device_info_ptr = pointer(device_info)
    ret_val = quicklink2_api.QLDevice_GetInfo(device_id, device_info_ptr)
    if(ret_val != QL_ERROR_OK):
        raise ValueError(errorToString(ret_val))
    else:
        print(infoToString(device_info))

    print("Starting device")
    ret_val = quicklink2_api.QLDevice_Start(device_id)

    # Check for file not found through python 
    if isfile(config_filename):
        print("Loading device configuration file")
        path = create_string_buffer(config_filename.encode("utf-8"))
        settingsId = QLSettingsId()
        settingsId_ptr = pointer(settingsId)
        res = quicklink2_api.QLSettings_Load(path, settingsId_ptr)
        settingsId = settingsId_ptr.contents.value
        quicklink2_api.QLDevice_ImportSettings(device_id, settingsId)
        if res == QL_ERROR_OK:
            print(f"Configuration file loaded successfully")
        elif res == QL_ERROR_INTERNAL_ERROR:
            print(f"""
            Invalid settings file (Quicklink2 API error code: {QL_ERROR_INTERNAL_ERROR}).
            Please see the '{EXAMPLE_CONFIG_FILENAME}' file for valid values
            """)
    elif config_filename != DEFAULT_CONFIG_FILENAME:
        raise FileNotFoundError(config_filename)

    initquicklink2_api_result = (quicklink2_api, device_info, device_id)
    return initquicklink2_api_result
