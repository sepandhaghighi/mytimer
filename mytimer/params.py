# -*- coding: utf-8 -*-
"""mytimer params."""

MY_TIMER_VERSION = "0.5"
WRONG_INPUT_ERROR = "[Error] Wrong input"
SOUND_ERROR_MESSAGE = "[Error] Unable to play sound"
INPUT_EXAMPLE = "Example: python -m mytimer --hour=1 --minute=1 --second=1"
TIME_ELEMENTS = ["minute", "second", "hour"]
MESSAGE_TEMPLATE = "Message: {0}"
FACES_MAP = {
    1: 'bulbhead',
    2: 'soft',
    3: '4max',
    4: '5x7',
    5: 'charact4',
    6: 'o8',
    7: 'alphabet',
    8: 'shadow',
    9: 'speed',
    10: 'rounded',
    11: 'chartri',
    12: 'standard',
    13: 'contessa',
    14: 'avatar',
    15: 'mini',
    16: 'twopoint',
    17: '3x5',
    18: 'threepoint',
    19: 'ascii_new_roman',
    20: 'serifcap',
    21: 'lockergnome'}

PROGRAMS_MAP = {
    "program1": {
        "minute": 0,
        "hour": 0,
        "second": 30,
        "alarm": 0,
        "face": 2,
        "message": "Program1"},
    "program2": {
        "minute": 2,
        "hour": 0,
        "second": 0,
        "alarm": 0,
        "face": 1,
        "message": "Program2"}
}
