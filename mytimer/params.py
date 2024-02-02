# -*- coding: utf-8 -*-
"""mytimer params."""

MY_TIMER_VERSION = "1.2"
ADDITIONAL_INFO = "Additional information: Press `Ctrl+C` to exit."
INPUT_ERROR_MESSAGE = "[Error] Wrong input"
SOUND_ERROR_MESSAGE = "[Error] Unable to play sound"
EXIT_MESSAGE = "See you. Bye!"
NEXT_PROGRAM_MESSAGE = "Press `Enter` to continue (Next: {0})"
PROGRAMS_LIST_TEMPLATE = "{0}. `{1}` - {2}"
TIME_PRINT_TEMPLATE = "{0:02} : {1:02} : {2:02}"
FACES_LIST_EXAMPLE_MESSAGE = "12 : 34 : 56"
INPUT_EXAMPLE = "Example: mytimer --hour=1 --minute=1 --second=1"
TIME_ELEMENTS = ["minute", "second", "hour"]
MESSAGE_TEMPLATE = "Message: {0}"

TONES_MAP = {
    1: '1.wav',
    2: '2.wav',
    3: '3.wav',
    4: '4.wav',
    5: '5.wav',
    6: '6.wav',
    7: '7.wav',
    8: '8.wav',
    9: '9.wav',
    10: '10.wav',
    11: '11.wav'}

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
    21: 'lockergnome',
    22: 'dotmatrix',
    23: '3-d',
    24: 'sweet',
    25: 'epic',
}

DEFAULT_PARAMS = {
    "hour": 0,
    "minute": 0,
    "second": 0,
    "alarm": 0,
    "alarm_repeat": 1,
    "face": 1,
    "tone": 1,
    "message": "",
    "v_shift": 0,
    "h_shift": 0,
}

PROGRAMS_DEFAULTS = {
    "alarm": 1
}

PROGRAMS_MAP = {
    "poached-egg": {
        "hour": 0,
        "minute": 1,
        "second": 30,
        "message": "Poached egg (1.5 mins)",
    },
    "boiled-egg": {
        "hour": 0,
        "minute": 3,
        "second": 0,
        "message": "Boiled egg (3 mins)",
    },
    "soft-boiled-egg": {
        "hour": 0,
        "minute": 5,
        "second": 0,
        "message": "Soft-boiled egg (5 mins)",
    },
    "hard-boiled-egg": {
        "hour": 0,
        "minute": 10,
        "second": 0,
        "message": "Hard-boiled egg (10 mins)",
    },
    "pasta": {
        "hour": 0,
        "minute": 8,
        "second": 0,
        "message": "Pasta (8 mins)",
    },
    "quick-rice": {
        "hour": 0,
        "minute": 10,
        "second": 0,
        "message": "Quick cooking rice (10 mins)",
    },
    "japanese-green-tea": {
        "hour": 0,
        "minute": 2,
        "second": 0,
        "message": "Japanese green tea (2 mins)",
    },
    "tea-bag": {
        "hour": 0,
        "minute": 2,
        "second": 0,
        "message": "Tea bag (2 mins)",
    },
    "chinese-green-tea": {
        "hour": 0,
        "minute": 5,
        "second": 0,
        "message": "Chinese green tea (5 mins)",
    },
    "black-tea": {
        "hour": 0,
        "minute": 5,
        "second": 0,
        "message": "Black tea (5 mins)",
    },
    "oolong-tea": {
        "hour": 0,
        "minute": 5,
        "second": 0,
        "message": "Oolong tea (5 mins)",
    },
    "fruit-tea": {
        "hour": 0,
        "minute": 8,
        "second": 0,
        "message": "Fruit tea (8 mins)",
    },
    "white-tea": {
        "hour": 0,
        "minute": 10,
        "second": 0,
        "message": "White tea (10 mins)",
    },
    "work": {
        "hour": 0,
        "minute": 25,
        "second": 0,
        "message": "Time to work (25 mins)",
    },
    "pomodoro": {
        "hour": 0,
        "minute": 25,
        "second": 0,
        "message": "Time to work (25 mins)",
    },
    "52-17": {
        "hour": 0,
        "minute": 52,
        "second": 0,
        "message": "Time to work (52 mins)",
    },
    "112-26": {
        "hour": 1,
        "minute": 52,
        "second": 0,
        "message": "Time to work (112 mins)",
    },
    "short-break": {
        "hour": 0,
        "minute": 10,
        "second": 0,
        "message": "Short break (10 mins)",
    },
    "long-break": {
        "hour": 0,
        "minute": 30,
        "second": 0,
        "message": "Long break (30 mins)",
    },
    "noodle": {
        "hour": 0,
        "minute": 3,
        "second": 0,
        "message": "Instant noodle (3 mins)",
    }
}
