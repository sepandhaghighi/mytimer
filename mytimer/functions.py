# -*- coding: utf-8 -*-
"""mytimer functions."""
import os
import sys
import subprocess
import time
from mytimer.params import INPUT_ERROR_MESSAGE, SOUND_ERROR_MESSAGE
from mytimer.params import INPUT_EXAMPLE, TIME_ELEMENTS, MESSAGE_TEMPLATE
from mytimer.params import FACES_MAP, PROGRAMS_MAP, TONES_MAP
from mytimer.params import MY_TIMER_VERSION, PROGRAMS_LIST_TEMPLATE
from mytimer.params import FACES_LIST_EXAMPLE_MESSAGE, TIME_PRINT_TEMPLATE
from mytimer.params import DEFAULT_PARAMS, PROGRAMS_DEFAULTS
from mytimer.params import NEXT_PROGRAM_MESSAGE
from art import tprint


def load_program_params(program_name):
    """
    Load program params.

    :param program_name: program name
    :type program_name: str
    :return: program params as dict
    """
    program_params = dict()
    for item in DEFAULT_PARAMS:
        if item in PROGRAMS_MAP[program_name]:
            program_params[item] = PROGRAMS_MAP[program_name][item]
        elif item in PROGRAMS_DEFAULTS:
            program_params[item] = PROGRAMS_DEFAULTS[item]
        else:
            program_params[item] = DEFAULT_PARAMS[item]
    return program_params


def show_programs_list():
    """
    Show programs list.

    :return: None
    """
    print("Programs list:\n")
    for i, program in enumerate(sorted(PROGRAMS_MAP), 1):
        print(
            PROGRAMS_LIST_TEMPLATE.format(
                i,
                program,
                PROGRAMS_MAP[program]['message']))


def show_faces_list():
    """
    Show faces list.

    :return: None
    """
    print("Faces list:\n")
    for i, face in sorted(FACES_MAP.items(), key=lambda item: (item[0])):
        print('Face {}\n'.format(i))
        tprint(FACES_LIST_EXAMPLE_MESSAGE, font=face)
        print('=' * 80)


def check_null_time(args):
    """
    Check that all time elements are null or not.

    :param args: input arguments
    :type args: argparse.Namespace
    :return: result as bool
    """
    for item in TIME_ELEMENTS:
        if getattr(args, item) is not None:
            return False
    return True


def load_params(args):
    """
    Load params.

    :param args: input arguments
    :type args: argparse.Namespace
    :return: params as dict
    """
    params = DEFAULT_PARAMS.copy()
    if args.program:
        params = load_program_params(args.program)
    for item in params:
        if getattr(args, item) is not None:
            if item not in TIME_ELEMENTS:
                params[item] = getattr(args, item)
            else:
                if not args.program:
                    params[item] = getattr(args, item)
    if not args.countdown:
        if check_null_time(args) and not args.program:
            params["hour"] = 100000000
    return params


def input_handler(func):
    """
    Input handler decorator for timer functions.

    :param func: input function
    :type func: function
    :return: inner function
    """
    def inner_function(
            hour,
            minute,
            second,
            alarm,
            face,
            message,
            tone,
            alarm_repeat,
            v_shift,
            h_shift):
        """
        Inner function.

        :param hour: hour
        :type hour: int
        :param minute: minute
        :type minute: int
        :param second: second
        :type second: int
        :param alarm: alarm flag
        :type alarm: bool
        :param face: face index
        :type face: int
        :param message: message
        :type message: str
        :param tone: tone index
        :type tone: int
        :param alarm_repeat: alarm repeat
        :type alarm_repeat: int
        :param v_shift: vertical shift
        :type v_shift: int
        :param h_shift: horizontal shift
        :type h_shift: int
        :return: None
        """
        message = message.strip()
        if len(message) > 0:
            message = MESSAGE_TEMPLATE.format(message)
        if alarm_repeat < 1:
            alarm_repeat = DEFAULT_PARAMS["alarm_repeat"]
        if h_shift < 0:
            h_shift = DEFAULT_PARAMS["h_shift"]
        if v_shift < 0:
            v_shift = DEFAULT_PARAMS["v_shift"]
        items_list = [hour, minute, second]
        if sum(items_list) != 0 and all(map(lambda x: x >= 0, items_list)):
            if second >= 60:
                minute += second // 60
                second %= 60
            if minute >= 60:
                hour += minute // 60
                minute %= 60
            func(
                hour,
                minute,
                second,
                alarm,
                face,
                message,
                tone,
                alarm_repeat,
                v_shift,
                h_shift)
        else:
            print(INPUT_ERROR_MESSAGE)
            print(INPUT_EXAMPLE)
    return inner_function


def clear_screen():
    """
    Clear screen function.

    :return: None
    """
    if sys.platform == "win32":
        os.system('cls')
    else:
        os.system('clear')


def get_sound_path(sound_name):
    """
    Return sound path.

    :param sound_name: .wav sound name
    :type sound_name: str
    :return: direct path to sound
    """
    cd, _ = os.path.split(__file__)
    return os.path.join(cd, "sounds", sound_name)


def play_sound(sound_path):
    """
    Play sound.

    :param sound_path: sound path
    :type sound_path: str
    :return: None
    """
    try:
        sys_platform = sys.platform
        if sys_platform == "win32":
            import winsound
            winsound.PlaySound(sound_path, winsound.SND_FILENAME)
        elif sys_platform == "darwin":
            _ = subprocess.check_call(["afplay",
                                       sound_path],
                                      shell=False,
                                      stderr=subprocess.PIPE,
                                      stdin=subprocess.PIPE,
                                      stdout=subprocess.PIPE)
        else:
            _ = subprocess.check_call(["aplay",
                                       sound_path],
                                      shell=False,
                                      stderr=subprocess.PIPE,
                                      stdin=subprocess.PIPE,
                                      stdout=subprocess.PIPE)
    except Exception:
        print(SOUND_ERROR_MESSAGE)


@input_handler
def countup_timer(
        hour,
        minute,
        second,
        alarm=DEFAULT_PARAMS["alarm"],
        face=DEFAULT_PARAMS["face"],
        message=DEFAULT_PARAMS["message"],
        tone=DEFAULT_PARAMS["tone"],
        alarm_repeat=DEFAULT_PARAMS["alarm_repeat"],
        v_shift=DEFAULT_PARAMS["v_shift"],
        h_shift=DEFAULT_PARAMS["h_shift"]):
    """
    Count-up timer function.

    :param hour: hour
    :type hour: int
    :param minute: minute
    :type minute: int
    :param second: second
    :type second: int
    :param alarm: alarm flag
    :type alarm: bool
    :param face: face index
    :type face: int
    :param message: message
    :type message: str
    :param tone: tone index
    :type tone: int
    :param alarm_repeat: alarm repeat
    :type alarm_repeat: int
    :param v_shift: vertical shift
    :type v_shift: int
    :param h_shift: horizontal shift
    :type h_shift: int
    :return: None
    """
    timer_second = 0
    timer_minute = 0
    timer_hour = 0
    face = FACES_MAP[face]
    tone = TONES_MAP[tone]
    while True:
        start = time.perf_counter()
        clear_screen()
        print('\n' * v_shift, end='')
        print(" " * h_shift, end='')
        tprint(
            TIME_PRINT_TEMPLATE.format(
                timer_hour,
                timer_minute,
                timer_second),
            font=face,
            sep="\n" + " " * h_shift)
        print(" " * h_shift, end='')
        print(message)
        if timer_hour == hour and timer_minute == minute and timer_second == second:
            print(" " * h_shift, end='')
            print("End!")
            if alarm:
                for _ in range(alarm_repeat):
                    play_sound(get_sound_path(tone))
            break
        timer_second += 1
        if timer_second == 60:
            timer_second = 0
            timer_minute += 1
        if timer_minute == 60:
            timer_minute = 0
            timer_hour += 1
        end = time.perf_counter()
        time.sleep(max(0, 1 - (end - start)))


@input_handler
def countdown_timer(
        hour,
        minute,
        second,
        alarm=DEFAULT_PARAMS["alarm"],
        face=DEFAULT_PARAMS["face"],
        message=DEFAULT_PARAMS["message"],
        tone=DEFAULT_PARAMS["tone"],
        alarm_repeat=DEFAULT_PARAMS["alarm_repeat"],
        v_shift=DEFAULT_PARAMS["v_shift"],
        h_shift=DEFAULT_PARAMS["h_shift"]):
    """
    Countdown timer function.

    :param hour: hour
    :type hour: int
    :param minute: minute
    :type minute: int
    :param second: second
    :type second: int
    :param alarm: alarm flag
    :type alarm: bool
    :param face: face index
    :type face: int
    :param message: message
    :type message: str
    :param tone: tone index
    :type tone: int
    :param alarm_repeat: alarm repeat
    :type alarm_repeat: int
    :param v_shift: vertical shift
    :type v_shift: int
    :param h_shift: horizontal shift
    :type h_shift: int
    :return: None
    """
    face = FACES_MAP[face]
    tone = TONES_MAP[tone]
    while True:
        start = time.perf_counter()
        clear_screen()
        print('\n' * v_shift, end='')
        print(" " * h_shift, end='')
        tprint(
            TIME_PRINT_TEMPLATE.format(
                hour,
                minute,
                second),
            font=face,
            sep="\n" + " " * h_shift)
        print(" " * h_shift, end='')
        print(message)
        second -= 1
        if second == -1:
            second = 59
            minute -= 1
        if minute == -1:
            minute = 59
            hour -= 1
        if hour == -1:
            print(" " * h_shift, end='')
            print("End!")
            if alarm:
                for _ in range(alarm_repeat):
                    play_sound(get_sound_path(tone))
            break
        end = time.perf_counter()
        time.sleep(max(0, 1 - (end - start)))


def pomodoro_timer(timer_func, **params):
    """
    Pomodoro timer function.

    :param timer_func: timer function
    :type timer_func: function
    :param params: counter parameters
    :type params: dict
    :return: None
    """
    short_break_params = load_program_params("short-break")
    long_break_params = load_program_params("long-break")
    for index in range(4):
        work_params = params.copy()
        work_params["message"] += " {0}/{1}".format(index + 1, 4)
        timer_func(**work_params)
        if index == 3:
            break
        _ = input(NEXT_PROGRAM_MESSAGE.format("Short break"))
        timer_func(**short_break_params)
        _ = input(NEXT_PROGRAM_MESSAGE.format(
            "Work {0}/{1}".format(index + 2, 4)))
    _ = input(NEXT_PROGRAM_MESSAGE.format("Long break"))
    timer_func(**long_break_params)


def _52_17_timer(timer_func, **params):
    """
    52/17 timer function.

    :param timer_func: timer function
    :type timer_func: function
    :param params: counter parameters
    :type params: dict
    :return: None
    """
    short_break_params = load_program_params("short-break")
    short_break_params['minute'] = 17
    short_break_params['message'] = "Short break (17 mins)"
    timer_func(**params)
    _ = input(NEXT_PROGRAM_MESSAGE.format("Short break"))
    timer_func(**short_break_params)


def _112_26_timer(timer_func, **params):
    """
    112/26 timer function.

    :param timer_func: timer function
    :type timer_func: function
    :param params: counter parameters
    :type params: dict
    :return: None
    """
    short_break_params = load_program_params("short-break")
    short_break_params['minute'] = 26
    short_break_params['message'] = "Short break (26 mins)"
    timer_func(**params)
    _ = input(NEXT_PROGRAM_MESSAGE.format("Short break"))
    timer_func(**short_break_params)


def run_timer(args):
    """
    Run timer.

    :param args: input arguments
    :type args: argparse.Namespace
    :return: None
    """
    params = load_params(args)
    timer_func = countup_timer
    if args.countdown:
        timer_func = countdown_timer
    if args.version:
        print(MY_TIMER_VERSION)
    elif args.faces_list:
        show_faces_list()
    elif args.programs_list:
        show_programs_list()
    elif args.program == "pomodoro":
        pomodoro_timer(timer_func, **params)
    elif args.program == "52-17":
        _52_17_timer(timer_func, **params)
    elif args.program == "112-26":
        _112_26_timer(timer_func, **params)
    else:
        timer_func(**params)
