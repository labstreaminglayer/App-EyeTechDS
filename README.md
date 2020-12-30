# EyeTechDS LSL

A Python package for streaming Gaze data from EyeTechDS devices. 

## Requirements

- Windows OS 
    - XP / 7 / 8 / 10 (32 or 64 bit)
- The [EyeTechDS SDK](https://eyetechds.com/developer-corner/software-downloads/quicklink2-sdk-download) 
- A valid driver for your device. On Windows 10, the "EyeTech HID Eye Tracking Device" driver is automatically installed upon connecting the device.

**Supported devices (non-exhaustive)**
- [VT3-Mini](https://eyetechds.com/eye-tracking-products/vt3-mini-eye-tracker/)

## Getting Started


### Installation

Install from source

    $ pip install git+https://github.com/intheon/eyetechds-lsl


## Setting Up a Stream

To begin the LSL stream ([Gaze](https://github.com/sccn/xdf/wiki/Gaze-Meta-Data)) from the first available EyeTechDS device:

    $ eyetechlsl stream  

To specify a configuration file:

    $ eyetechlsl stream --config device-config.file

If you wish to also start a [VideoRaw](https://github.com/sccn/xdf/wiki/Video-Raw-Meta-Data) stream:

    $ eyetechlsl stream --video

## Viewing the VideoRaw stream

Ensure that you have [`opencv-python`](https://pypi.org/project/opencv-python/) installed.

    $ eyetechlsl video

The `VideoRaw` stream will transmit at the same rate as the `Gaze` stream, but a new `VideoRaw` sample will only be transmitted when the QuickLink2 API receives a new frame, so actual frames-per-second will likely be lower. On a VT-3 Mini running at full resolution, actual FPS was around 6-7. 

## Configuration

Device configuration uses the format and parameters specified in `./config.template`.
By default a `./config` file will be loaded if it exists.

EyeTechDS devices prioritize streaming processed data before raw video data. As a result, the VideoRaw stream `DeviceDownsampleScaleFactor` configuration parameter (float between 1.0 - 20.0) specifies the fractional downscaling of the video data that the device will transmit. A higher `DeviceDownsampleScaleFactor` value will result in an increase in frames-per-second, at the cost of reduced image resolution. 

## What is LSL?

Lab Streaming Layer or LSL is a system designed to unify the collection of time series data for research experiments. It has become standard in the field of EEG-based brain-computer interfaces for its ability to make seperate streams of data available on a network with time synchronization and near real-time access. For more information, check out this [lecture from Modern Brain-Computer Interface Design](https://www.youtube.com/watch?v=Y1at7yrcFW0) or the [LSL repository](https://github.com/sccn/labstreaminglayer)
