# -*- coding: utf-8 -*-
"""mytimer main."""
from mytimer.params import FACES_LIST, PROGRAMS_MAP, TONES_LIST
from mytimer.params import EXIT_MESSAGE, ADDITIONAL_INFO, SIGNS_LIST
from mytimer.params import DATE_SYSTEMS_LIST
from mytimer.functions import run_timer
import argparse


def main():
    """
    CLI main function.

    :return: None
    """
    parser = argparse.ArgumentParser()
    parser.epilog = ADDITIONAL_INFO
    parser.add_argument('--minute', help='minute', type=int)
    parser.add_argument('--second', help='second', type=int)
    parser.add_argument('--hour', help='hour', type=int)
    parser.add_argument('--message', help='message', type=str)
    parser.add_argument(
        '--face',
        help='face',
        type=int,
        choices=FACES_LIST)
    parser.add_argument(
        '--tone',
        help='alarm tone',
        type=int,
        choices=TONES_LIST)
    parser.add_argument(
        '--program',
        help='program',
        type=str.lower,
        choices=sorted(PROGRAMS_MAP))
    parser.add_argument(
        '--sign',
        help='timer sign',
        type=str,
        choices=SIGNS_LIST)
    parser.add_argument('--alarm-repeat', help='alarm repeat', type=int)
    parser.add_argument('--v-shift', help='vertical shift', type=int)
    parser.add_argument('--h-shift', help='horizontal shift', type=int)
    parser.add_argument('--repeat', help='number of repeats', type=int, default=1)
    parser.add_argument(
        '--countdown',
        help='countdown timer',
        nargs="?",
        const=1)
    parser.add_argument('--countup', help='countup timer', nargs="?", const=1)
    parser.add_argument('--alarm', help='alarm', nargs="?", const=1)
    parser.add_argument('--keep-on', help='keep-on', nargs="?", const=1)
    parser.add_argument('--set-on', help='set-on', nargs="?", const=1)
    parser.add_argument('--test-tone', help='test tone', nargs="?", const=1)
    parser.add_argument('--faces-list', help='faces list', nargs="?", const=1)
    parser.add_argument('--version', help='version', nargs="?", const=1)
    parser.add_argument('--info', help='info', nargs="?", const=1)
    parser.add_argument('--hide-second', help='hide second', nargs="?", const=1)
    parser.add_argument('--hide-datetime', help='hide datetime', nargs="?", const=1)
    parser.add_argument('--vertical', help='vertical mode', nargs="?", const=1)
    parser.add_argument('--date-system', help='date system', type=str.lower, choices=DATE_SYSTEMS_LIST, default="gregorian")
    parser.add_argument(
        '--programs-list',
        help='programs list',
        nargs="?",
        const=1)
    args = parser.parse_args()
    try:
        run_timer(args)
    except (KeyboardInterrupt, EOFError):
        print(EXIT_MESSAGE)


if __name__ == "__main__":
    main()
