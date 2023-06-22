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
    "poached-egg": {
        "hour": 0,
        "minute": 1,
        "second": 30,
        "alarm": 0,
        "face": 1,
        "message": "Poached egg (1.5 mins)"},
    "boiled-egg": {
        "hour": 0,
        "minute": 3,
        "second": 0,
        "alarm": 0,
        "face": 1,
        "message": "Boiled egg (3 mins)"},
    "soft-boiled-egg": {
        "hour": 0,
        "minute": 5,
        "second": 0,
        "alarm": 0,
        "face": 1,
        "message": "Soft-boiled egg (5 mins)"},
    "hard-boiled-egg": {
        "hour": 0,
        "minute": 10,
        "second": 0,
        "alarm": 0,
        "face": 1,
        "message": "Hard-boiled egg (10 mins)"},
    "pasta": {
        "hour": 0,
        "minute": 8,
        "second": 0,
        "alarm": 0,
        "face": 1,
        "message": "Pasta (8 mins)"},
    "quick-rice": {
        "hour": 0,
        "minute": 10,
        "second": 0,
        "alarm": 0,
        "face": 1,
        "message": "Quick cooking rice (10 mins)"},
}
