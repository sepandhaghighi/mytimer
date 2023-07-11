# -*- coding: utf-8 -*-
"""mytimer main."""
from mytimer.params import FACES_MAP, PROGRAMS_MAP, TONES_MAP
from mytimer.functions import run_timer
import argparse


def main():
    """
    CLI main function.

    :return: None
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--minute', help='minute', type=int)
    parser.add_argument('--second', help='second', type=int)
    parser.add_argument('--hour', help='hour', type=int)
    parser.add_argument('--message', help='message', type=str)
    parser.add_argument(
        '--face',
        help='face',
        type=int,
        choices=sorted(
            FACES_MAP.keys()))
    parser.add_argument(
        '--tone',
        help='alarm tone',
        type=int,
        choices=sorted(
            TONES_MAP.keys()))
    parser.add_argument(
        '--program',
        help='program',
        type=str,
        choices=sorted(
            PROGRAMS_MAP.keys()))
    parser.add_argument(
        '--countdown',
        help='countdown timer',
        nargs="?",
        const=1)
    parser.add_argument('--countup', help='countup timer', nargs="?", const=1)
    parser.add_argument('--alarm', help='alarm', nargs="?", const=1)
    parser.add_argument('--version', help='version', nargs="?", const=1)
    args = parser.parse_args()
    run_timer(args)


if __name__ == "__main__":
    main()
