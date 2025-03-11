# -*- coding: utf-8 -*-
"""mytimer params."""

MY_TIMER_VERSION = "2.2"
ADDITIONAL_INFO = "Additional information: Press `Ctrl+C` to exit."
INPUT_ERROR_MESSAGE = "[Error] Wrong input"
SOUND_ERROR_MESSAGE = "[Error] Unable to play sound"
EXIT_MESSAGE = "See you. Bye!"
END_ROUND_MESSAGE = "Round {round} done! Press `Enter` to continue..."
NEXT_PROGRAM_MESSAGE = "Press `Enter` to continue (Next: {next_program})"
PROGRAMS_LIST_TEMPLATE = "{index}. `{program}` - {message}"
TIME_HMS_TEMPLATE_HORIZONTAL = "{sign}{hour:02} : {minute:02} : {second:02}"
TIME_HM_TEMPLATE_HORIZONTAL = "{sign}{hour:02} : {minute:02}"
TIME_HMS_TEMPLATE_VERTICAL = "{sign}\n{hour:02}\n{minute:02}\n{second:02}"
TIME_HM_TEMPLATE_VERTICAL = "{sign}\n{hour:02}\n{minute:02}"
FACES_LIST_EXAMPLE_MESSAGE = "12 : 34 : 56"
INPUT_EXAMPLE = "Example: mytimer --hour=1 --minute=1 --second=1"
TIME_ELEMENTS = ["minute", "second", "hour"]
MESSAGE_TEMPLATE = "Message: {message}"
KEEP_ON_MESSAGE = " **Timeout!"
SET_ON_MESSAGE = "Timer set for {hour:02d}:{minute:02d}:{second:02d}"
DATE_FORMAT = "%A, %B %d, %Y"
CLOCK_FORMAT = "%H:%M %p"
KEEP_ON_MAX = 10000000

SIGNS_LIST = ["", "+", "-"]

MY_TIMER_OVERVIEW = '''
MyTimer is a Python project that aims to provide a simple yet efficient timer for terminal users,
particularly targeting the geek community.
This project allows users to set timers directly from their command line interface,
making it convenient for those who spend a significant amount of time working in the terminal!
'''

MY_TIMER_REPO = "Repo : https://github.com/sepandhaghighi/mytimer"

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
    11: '11.wav',
    12: '12.wav',
    13: '13.wav',
    14: '14.wav',
    15: '15.wav',
    16: '16.wav',
    17: '17.wav',
    18: '18.wav',
    19: '19.wav',
    20: '20.wav',
    21: '21.wav',
    22: '22.wav',
    23: '23.wav',
    24: '24.wav',
    25: '25.wav',
    26: '26.wav',
    27: '27.wav',
    28: '28.wav',
    29: '29.wav',
    30: '30.wav',
    31: '31.wav',
    32: '32.wav',
    33: '33.wav',
    34: '34.wav',
}

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
    "hide_second": 0,
    "hide_datetime": 0,
    "date_system": "gregorian",
    "vertical": 0,
    "alarm_repeat": 1,
    "face": 1,
    "tone": 1,
    "message": "",
    "v_shift": 0,
    "h_shift": 0,
    "sign": ""
}

PROGRAMS_DEFAULTS = {
    "alarm": 1
}

BREAKS_DEFAULTS = {
    "alarm": 1,
    "tone": 2
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
        "message": "Japanese green tea (2 mins, 70-85 C)",
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
        "message": "Chinese green tea (5 mins, 70-85 C)",
    },
    "black-tea": {
        "hour": 0,
        "minute": 5,
        "second": 0,
        "message": "Black tea (5 mins, 85-100 C)",
    },
    "oolong-tea": {
        "hour": 0,
        "minute": 5,
        "second": 0,
        "message": "Oolong tea (5 mins, 70-80 C)",
    },
    "fruit-tea": {
        "hour": 0,
        "minute": 8,
        "second": 0,
        "message": "Fruit tea (8 mins, 85-100 C)",
    },
    "white-tea": {
        "hour": 0,
        "minute": 3,
        "second": 0,
        "message": "White tea (3 mins, 70-80 C)",
    },
    "rooibos-tea": {
        "hour": 0,
        "minute": 6,
        "second": 0,
        "message": "Rooibos tea (6 mins, 90-100 C)",
    },
    "yellow-tea": {
        "hour": 0,
        "minute": 2,
        "second": 0,
        "message": "Yellow tea (2 mins, 70-85 C)",
    },
    "puer-tea": {
        "hour": 0,
        "minute": 5,
        "second": 0,
        "message": "Pu-erh tea (5 mins, 85-100 C)",
    },
    "purple-tea": {
        "hour": 0,
        "minute": 3,
        "second": 0,
        "message": "Purple tea (3 mins, 80-85 C)",
    },
    "mate": {
        "hour": 0,
        "minute": 5,
        "second": 0,
        "message": "Mate (5 mins, 65-70 C)",
    },
    "french-press": {
        "hour": 0,
        "minute": 4,
        "second": 0,
        "message": "French press (4 mins, 93-96 C)",
    },
    "meditation": {
        "hour": 0,
        "minute": 20,
        "second": 0,
        "message": "Meditation (20 mins)",
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
    "animedoro": {
        "hour": 0,
        "minute": 40,
        "second": 0,
        "message": "Time to work (40 mins)",
    },
    "short-break": {
        "hour": 0,
        "minute": 5,
        "second": 0,
        "message": "Short break (5 mins)",
    },
    "coffee-break": {
        "hour": 0,
        "minute": 10,
        "second": 0,
        "message": "Coffee break (10 mins)",
    },
    "mid-break": {
        "hour": 0,
        "minute": 15,
        "second": 0,
        "message": "Medium break (15 mins)",
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

BREAKS_MAP = {
    "52-17": {
        "hour": 0,
        "minute": 17,
        "second": 0,
        "message": "52-17 break (17 mins)",
    },
    "112-26": {
        "hour": 0,
        "minute": 26,
        "second": 0,
        "message": "112-26 break (26 mins)",
    },
    "animedoro": {
        "hour": 0,
        "minute": 20,
        "second": 0,
        "message": "Animedoro break (20 mins)",
    },
    "pomodoro-short-break": {
        "hour": 0,
        "minute": 5,
        "second": 0,
        "message": "Pomodoro short break (5 mins)",
    },
    "pomodoro-long-break": {
        "hour": 0,
        "minute": 15,
        "second": 0,
        "message": "Pomodoro long break (15 mins)",
    },
}

FACES_LIST = [-1] + sorted(FACES_MAP)

TONES_LIST = [-1] + sorted(TONES_MAP)

DATE_SYSTEMS_LIST = ["gregorian", "jalali"]
