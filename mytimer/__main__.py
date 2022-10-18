# -*- coding: utf-8 -*-
"""mytimer main."""
from mytimer.functions import countdown_timer, countup_timer
import argparse


def main():
    """
    CLI main function.

    :return: None
    """
    params = {"minute": 0, "hour": 0, "second": 0, "alarm": 0}
    parser = argparse.ArgumentParser()
    parser.add_argument('--minute', help='minute', type=float)
    parser.add_argument('--second', help='second', type=float)
    parser.add_argument('--hour', help='hour', type=float,)
    parser.add_argument(
        '--countdown',
        help='countdown timer',
        nargs="?",
        const=1)
    parser.add_argument('--countup', help='countup timer', nargs="?", const=1)
    parser.add_argument('--alarm', help='alarm', nargs="?", const=1)
    args = parser.parse_args()
    for item in params:
        if getattr(args, item) is not None:
            params[item] = getattr(args, item)
    if args.countdown:
        countdown_timer(**params)
    else:
        countup_timer(**params)


if __name__ == "__main__":
    main()
