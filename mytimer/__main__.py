# -*- coding: utf-8 -*-
"""mytimer main."""
from mytimer.params import MY_TIMER_VERSION, FACES_MAP
from mytimer.functions import countdown_timer, countup_timer, check_null_time
import argparse


def main():
    """
    CLI main function.

    :return: None
    """
    params = {
        "minute": 0,
        "hour": 0,
        "second": 0,
        "alarm": 0,
        "face": 1,
        "message": ""}
    parser = argparse.ArgumentParser()
    parser.add_argument('--minute', help='minute', type=int)
    parser.add_argument('--second', help='second', type=int)
    parser.add_argument('--hour', help='hour', type=int)
    parser.add_argument('--message', help='message', type=str)
    parser.add_argument(
        '--face',
        help='face',
        type=int,
        choices=list(
            FACES_MAP.keys()))
    parser.add_argument(
        '--countdown',
        help='countdown timer',
        nargs="?",
        const=1)
    parser.add_argument('--countup', help='countup timer', nargs="?", const=1)
    parser.add_argument('--alarm', help='alarm', nargs="?", const=1)
    parser.add_argument('--version', help='version', nargs="?", const=1)
    args = parser.parse_args()
    for item in params:
        if getattr(args, item) is not None:
            params[item] = getattr(args, item)
    if args.version:
        print(MY_TIMER_VERSION)
    else:
        if args.countdown:
            countdown_timer(**params)
        else:
            if check_null_time(args):
                params["hour"] = 100000000
            countup_timer(**params)


if __name__ == "__main__":
    main()
