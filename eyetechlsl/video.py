import numpy as np
import cv2
from pylsl import StreamInlet, resolve_stream
import time
from math import floor

def init(timeout):
    window_title = 'EyeTechDS LSL Stream (Q to quit)'
    streams = resolve_stream('type', 'VideoRaw')
    inlet = StreamInlet(streams[0])
    info = inlet.info()
    encoding = info.desc().child('encoding')
    w, h = encoding.child_value('width'), encoding.child_value('height')

    print(f"Received VideoRaw dimensions: {w} x {h}")

    # Bandwidth constraints mean that the VideoRaw frame will be identical
    # until the device has pushed a new frame over USB.
    diff = 0
    w, h = int(w), int(h)

    # Used to sample 10 x 10 evenly spaced pixels from each frame to compare the diff 
    # and check if the received frame is different from the previous one.
    w_diff, h_diff = w // 5, h // 5

    chunk = np.ndarray((1, w*h), dtype='uint8', order='C')
    prev_sec = np.floor(time.time())
    curr_sec = prev_sec

    # Keep track of FPS 
    fps = 0
    frames = 0
    new_frame_time = 0
    prev_frame = None

    while(True):
        new_frame_time = time.time()
        curr_sec = np.floor(time.time())
        stats = f"{w}px x {h}px @ {fps:.2f} FPS"
        if curr_sec > prev_sec:
            print(stats, end="\r", flush=True)
            fps = 0
            prev_sec = curr_sec

        inlet.pull_chunk(max_samples=1, dest_obj=chunk)
        if len(chunk) == 0:
            continue
        sample2d = np.reshape(chunk[0], (w, h))
        
        cv2.imshow(window_title, sample2d)
        if frames == 0:
            cv2.moveWindow(window_title, 100, 100)
        else:
            sample_diff = prev_frame[::w_diff, ::h_diff] - sample2d[::w_diff, ::h_diff]
            diff = np.sum(sample_diff)
        prev_frame = np.copy(sample2d)
        if diff != 0:
            fps += 1
        frames += 1
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break
        
    inlet.close_stream()
    cv2.destroyAllWindows()