# -*- coding: utf-8 -*-
"""mytimer main."""
from mytimer.params import MY_TIMER_VERSION, FACES_MAP, PROGRAMS_MAP
from mytimer.functions import countdown_timer, countup_timer, load_params
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
    params = load_params(args)
    if args.version:
        print(MY_TIMER_VERSION)
    else:
        if args.countdown:
            countdown_timer(**params)
        else:
            countup_timer(**params)


if __name__ == "__main__":
    main()
