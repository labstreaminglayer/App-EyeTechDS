import argparse
import sys
from .cli import CLI


def main():
    parser = argparse.ArgumentParser(
        description='Python package for streaming, recording, and visualizing Gaze and VideoRaw data from the EyeTech VT-3.',
        usage='''eyetech <command> [<args>]
    Available commands:

    stream      Start an LSL stream from the EyeTechDS headset.
    video       Preview the video stream from the `stream` command
    ''')

    parser.add_argument('command', help='Command to run.')

    # parse_args defaults to [1:] for args, but you need to
    # exclude the rest of the args too, or validation will fail
    
    args = parser.parse_args(sys.argv[1:2])
    print(args.command)
    if not hasattr(CLI, args.command):
        print('Incorrect usage. See help below.')
        parser.print_help()
        exit(1)

    cli = CLI(args.command)


if __name__ == '__main__':
    main()
