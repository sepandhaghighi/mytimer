# -*- coding: utf-8 -*-
"""mytimer functions."""
import os
import sys
import time
import datetime
from nava import play
from mytimer.params import INPUT_ERROR_MESSAGE, SOUND_ERROR_MESSAGE
from mytimer.params import INPUT_EXAMPLE, TIME_ELEMENTS, MESSAGE_TEMPLATE
from mytimer.params import FACES_MAP, PROGRAMS_MAP, BREAKS_MAP, TONES_MAP
from mytimer.params import MY_TIMER_VERSION, PROGRAMS_LIST_TEMPLATE
from mytimer.params import FACES_LIST_EXAMPLE_MESSAGE, TIME_PRINT_TEMPLATE
from mytimer.params import DEFAULT_PARAMS, PROGRAMS_DEFAULTS, BREAKS_DEFAULTS
from mytimer.params import NEXT_PROGRAM_MESSAGE, END_ROUND_MESSAGE
from mytimer.params import KEEP_ON_MESSAGE, SET_ON_MESSAGE
from mytimer.params import KEEP_ON_MAX
from art import tprint


def print_message(message, v_shift=0, h_shift=0, confirm=False):
    """
    Print message.

    :param message: message text
    :type message: str
    :param v_shift: vertical shift
    :type v_shift: int
    :param h_shift: horizontal shift
    :type h_shift: int
    :param confirm: confirm flag
    :type confirm: bool
    :return: None
    """
    func = print
    if confirm:
        func = input
    print('\n' * v_shift, end='')
    func(h_shift * " " + message)


def load_program_params(program_name, is_break=False):
    """
    Load program/break params.

    :param program_name: program name
    :type program_name: str
    :param is_break: break flag
    :type is_break: bool
    :return: program/break params as dict
    """
    program_params = dict()
    ref_map = PROGRAMS_MAP
    ref_defaults = PROGRAMS_DEFAULTS
    if is_break:
        ref_map = BREAKS_MAP
        ref_defaults = BREAKS_DEFAULTS
    for item in DEFAULT_PARAMS:
        if item in ref_map[program_name]:
            program_params[item] = ref_map[program_name][item]
        elif item in ref_defaults:
            program_params[item] = ref_defaults[item]
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


def load_params(args, program=None, is_break=False):
    """
    Load params.

    :param args: input arguments
    :type args: argparse.Namespace
    :param program: program name
    :type program: str
    :param is_break: break flag
    :type is_break: bool
    :return: params as dict
    """
    params = DEFAULT_PARAMS.copy()
    if program is not None:
        params = load_program_params(program, is_break=is_break)
    elif args.program:
        params = load_program_params(args.program, is_break=is_break)
    for item in params:
        if getattr(args, item) is not None:
            if item not in TIME_ELEMENTS:
                params[item] = getattr(args, item)
            else:
                if not args.program:
                    params[item] = getattr(args, item)
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
            h_shift,
            sign):
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
        :param sign: timer sign
        :type sign: str
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
                h_shift,
                sign)
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
        play(sound_path)
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
        h_shift=DEFAULT_PARAMS["h_shift"],
        sign=DEFAULT_PARAMS["sign"]):
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
    :param sign: timer sign
    :type sign: str
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
                sign,
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
        h_shift=DEFAULT_PARAMS["h_shift"],
        sign=DEFAULT_PARAMS["sign"]):
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
    :param sign: timer sign
    :type sign: str
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
                sign,
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


def pomodoro_timer(timer_func, params, long_break_params, short_break_params):
    """
    Pomodoro timer function.

    :param timer_func: timer function
    :type timer_func: function
    :param params: program params
    :type params: dict
    :param long_break_params: long break params
    :type long_break_params: dict
    :param short_break_params: short break params
    :type short_break_params: dict
    :return: None
    """
    h_shift = params["h_shift"]
    for index in range(4):
        work_params = params.copy()
        work_params["message"] += " {0}/{1}".format(index + 1, 4)
        timer_func(**work_params)
        if index == 3:
            break
        print_message(message=NEXT_PROGRAM_MESSAGE.format("Short break"), h_shift=h_shift, confirm=True)
        timer_func(**short_break_params)
        print_message(message=NEXT_PROGRAM_MESSAGE.format(
            "Work {0}/{1}".format(index + 2, 4)), h_shift=h_shift, confirm=True)
    print_message(message=NEXT_PROGRAM_MESSAGE.format("Long break"), h_shift=h_shift, confirm=True)
    timer_func(**long_break_params)


def two_step_timer(timer_func, params1, params2):
    """
    Two step timer function.

    :param timer_func: timer function
    :type timer_func: function
    :param params1: program-1 params
    :type params1: dict
    :param params2: program-2 params
    :type params2: dict
    :return: None
    """
    h_shift = params1["h_shift"]
    timer_func(**params1)
    print_message(message=NEXT_PROGRAM_MESSAGE.format("Break"), h_shift=h_shift, confirm=True)
    timer_func(**params2)


def keep_on_timer(params):
    """
    Keep-on timer.

    :param params: timer params
    :type params: dict
    :return: None
    """
    params["hour"] = KEEP_ON_MAX
    params["message"] += KEEP_ON_MESSAGE
    if params["sign"] in ["+", ""]:
        params["sign"] = "-"
    else:
        params["sign"] = "+"
    countup_timer(**params)


def update_set_on_params(params):
    """
    Update set-on mode params.

    :param params: timer params
    :type params: dict
    :return: timer params as dict
    """
    if params["message"] == "":
        params["message"] = SET_ON_MESSAGE.format(params["hour"], params["minute"], params["second"])
    time_now = datetime.datetime.now()
    time_then = datetime.datetime(
        time_now.year,
        time_now.month,
        time_now.day,
        params["hour"],
        params["minute"],
        params["second"])
    if time_then < time_now:
        time_then += datetime.timedelta(days=1)
    time_diff = time_then - time_now
    params["hour"] = time_diff.seconds // 3600
    params["minute"] = time_diff.seconds % 3600 // 60
    params["second"] = time_diff.seconds % 60
    return params


def select_timer_func(args, params):
    """
    Select timer function.

    :param args: input arguments
    :type args: argparse.Namespace
    :param params: timer params
    :type params: dict
    :return: timer function, timer params
    """
    timer_func = countdown_timer
    if args.countup:
        timer_func = countup_timer
    if args.countdown:
        timer_func = countdown_timer
    else:
        if check_null_time(args) and not args.program:
            params["hour"] = KEEP_ON_MAX
            timer_func = countup_timer
    return timer_func, params


def run_timer(args):
    """
    Run timer.

    :param args: input arguments
    :type args: argparse.Namespace
    :return: None
    """
    params = load_params(args)
    timer_func, params = select_timer_func(args, params)
    if args.set_on:
        params = update_set_on_params(params)
    if args.version:
        print(MY_TIMER_VERSION)
    elif args.faces_list:
        show_faces_list()
    elif args.programs_list:
        show_programs_list()
    else:
        timer_round = 1
        while timer_round <= args.repeat or args.repeat == -1:
            if args.program == "pomodoro":
                short_break_params = load_params(args, program="pomodoro-short-break", is_break=True)
                long_break_params = load_params(args, program="pomodoro-long-break", is_break=True)
                pomodoro_timer(
                    timer_func,
                    params=params,
                    long_break_params=long_break_params,
                    short_break_params=short_break_params)
            elif args.program in ["52-17", "112-26", "animedoro"]:
                break_params = load_params(args, is_break=True)
                two_step_timer(timer_func, params1=params, params2=break_params)
            else:
                timer_func(**params)
            end_round_message = END_ROUND_MESSAGE.format("{0}/{1}".format(timer_round, args.repeat))
            if args.repeat == -1:
                end_round_message = END_ROUND_MESSAGE.format(timer_round)
            if timer_round < args.repeat or args.repeat == -1:
                print_message(
                    message=end_round_message,
                    h_shift=params["h_shift"],
                    confirm=True)
            timer_round += 1
        if args.keep_on:
            keep_on_timer(params)
