#!/usr/bin/python
import sys
import argparse
from .constants import DEFAULT_CONFIG_FILENAME, EXAMPLE_CONFIG_FILENAME

class CLI:
    def __init__(self, command):
        # use dispatch pattern to invoke method with same name
        getattr(self, command)()

    def stream(self):

        parser = argparse.ArgumentParser(
                        description=f"""LSL integration for EyeTechDS devices. Currently tested on the EyeTech VT3-Mini. """)
        parser.add_argument('-s', '--srate', type=int, nargs=1, default=60, required=False, dest="srate",
                        help=f"Sets the LSL streams sampling rate. Default: 60")
        parser.add_argument('-c', '--config', type=str, nargs=1, default=DEFAULT_CONFIG_FILENAME, required=False, dest="config_filename",
                        help=f"""File name / path of the Quicklink2 device configuration.
                        See './{EXAMPLE_CONFIG_FILENAME}' for an example configuration & further information.""")
        parser.add_argument('-v', '--video', action="store_const", const=True, default=False, required=False, dest="video",
                        help=f"""Creates an additional VideoRaw stream from the devices camera. The video's sampling rate varies depending on available bandwidth.""")
        parser.add_argument('--verbose', action="store_const", const=True, default=False, required=False, dest="verbose",
                        help=f"""Outputs debug information to the console every 250 data samples.""")


        args = parser.parse_args(sys.argv[2:])
        from .stream import init

        init(args.srate, args.config_filename, args.video, args.verbose)

    def video(self):
        parser = argparse.ArgumentParser(
                        description=f"""OpenCV Previewer for the EyeTechDS VideoRaw stream""")
        parser.add_argument('-t', '--timeout', type=int, nargs=1, default=None, required=False, dest="timeout",
                        help=f"Exits the video stream after the specified timeout")
        args = parser.parse_args(sys.argv[2:])
        from .video import init
        init(args.timeout)