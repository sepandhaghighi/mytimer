# -*- coding: utf-8 -*-
"""mytimer functions."""
import os
import sys
import time
import datetime
import jdatetime
import random
from nava import play
from mytimer.params import INPUT_ERROR_MESSAGE, SOUND_ERROR_MESSAGE
from mytimer.params import INPUT_EXAMPLE, TIME_ELEMENTS, MESSAGE_TEMPLATE
from mytimer.params import FACES_MAP, PROGRAMS_MAP, BREAKS_MAP, TONES_MAP
from mytimer.params import MY_TIMER_VERSION, PROGRAMS_LIST_TEMPLATE
from mytimer.params import FACES_LIST_EXAMPLE_MESSAGE
from mytimer.params import DEFAULT_PARAMS, PROGRAMS_DEFAULTS, BREAKS_DEFAULTS
from mytimer.params import NEXT_PROGRAM_MESSAGE, END_ROUND_MESSAGE
from mytimer.params import KEEP_ON_MESSAGE, SET_ON_MESSAGE
from mytimer.params import KEEP_ON_MAX
from mytimer.params import MY_TIMER_OVERVIEW, MY_TIMER_REPO
from mytimer.params import TIME_HMS_TEMPLATE_HORIZONTAL, TIME_HM_TEMPLATE_HORIZONTAL
from mytimer.params import TIME_HMS_TEMPLATE_VERTICAL, TIME_HM_TEMPLATE_VERTICAL
from mytimer.params import CLOCK_FORMAT, DATE_FORMAT
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


def mytimer_info():
    """
    Print mytimer details.

    :return: None
    """
    tprint("MyTimer")
    tprint("V:" + MY_TIMER_VERSION)
    print(MY_TIMER_OVERVIEW)
    print(MY_TIMER_REPO)


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
                index=i,
                program=program,
                message=PROGRAMS_MAP[program]['message']))


def show_faces_list():
    """
    Show faces list.

    :return: None
    """
    print("Faces list:\n")
    for i in sorted(FACES_MAP):
        print('Face {}\n'.format(i))
        tprint(FACES_LIST_EXAMPLE_MESSAGE, font=get_face(i))
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
            sign,
            hide_second,
            hide_datetime,
            vertical,
            date_system):
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
        :param hide_second: hide second flag
        :type hide_second: bool
        :param hide_datetime: hide date/time flag
        :type hide_datetime: bool
        :param vertical: vertical mode flag
        :type vertical: bool
        :param date_system: date system
        :type date_system: str
        :return: None
        """
        message = message.strip()
        if len(message) > 0:
            message = MESSAGE_TEMPLATE.format(message=message)
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
                sign,
                hide_second,
                hide_datetime,
                vertical,
                date_system)
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


def get_face(index):
    """
    Return face name.

    :param index: face index
    :type index: int
    :return: face name as str
    """
    if index == -1:
        index = random.choice(sorted(FACES_MAP))
    return FACES_MAP[index]


def get_tone(index):
    """
    Return tone file name.

    :param index: tone index
    :type index: int
    :return: tone file name as str
    """
    if index == -1:
        index = random.choice(sorted(TONES_MAP))
    return TONES_MAP[index]


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


def play_alarm(tone, repeat):
    """
    Play alarm.

    :param tone: alarm tone index
    :type tone: int
    :param repeat: alarm repeat
    :type repeat: int
    :return: None
    """
    tone = get_tone(tone)
    sound_path = get_sound_path(tone)
    for _ in range(repeat):
        play_sound(sound_path)


def test_tone(tone, repeat):
    """
    Test tone.

    :param tone: alarm tone index
    :type tone: int
    :param repeat: alarm repeat
    :type repeat: int
    :return: None
    """
    print("Tone: {tone}".format(tone=tone))
    print("Repeat: {repeat}".format(repeat=repeat))
    start = time.perf_counter()
    play_alarm(tone, repeat)
    end = time.perf_counter()
    duration = round(end - start, 4)
    print("Duration: {duration} s".format(duration=duration))


def print_date_time(h_shift, date_system):
    """
    Print date and time.

    :param h_shift: horizontal shift
    :type h_shift: int
    :param date_system: date system
    :type date_system: str
    :return: None
    """
    datetime_lib = datetime
    if date_system == "jalali":
        datetime_lib = jdatetime
    datetime_now = datetime_lib.datetime.now()
    current_time = datetime_now.strftime(CLOCK_FORMAT)
    current_date = datetime_now.strftime(DATE_FORMAT)
    print(" " * h_shift, end='')
    print(current_time)
    print(" " * h_shift, end='')
    print(current_date)
    print("")
    print(" " * h_shift, end='')


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
        sign=DEFAULT_PARAMS["sign"],
        hide_second=DEFAULT_PARAMS["hide_second"],
        hide_datetime=DEFAULT_PARAMS["hide_datetime"],
        vertical=DEFAULT_PARAMS["vertical"],
        date_system=DEFAULT_PARAMS["date_system"]):
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
    :param hide_second: hide second flag
    :type hide_second: bool
    :param hide_datetime: hide date/time flag
    :type hide_datetime: bool
    :param vertical: vertical mode flag
    :type vertical: bool
    :param date_system: date system
    :type date_system: str
    :return: None
    """
    timer_second = 0
    timer_minute = 0
    timer_hour = 0
    face = get_face(face)
    timer_template = TIME_HMS_TEMPLATE_VERTICAL if vertical else TIME_HMS_TEMPLATE_HORIZONTAL
    if hide_second:
        timer_template = TIME_HM_TEMPLATE_VERTICAL if vertical else TIME_HM_TEMPLATE_HORIZONTAL
    while True:
        start = time.perf_counter()
        clear_screen()
        print('\n' * v_shift, end='')
        print(" " * h_shift, end='')
        timer_params = {"sign": sign, "hour": timer_hour, "minute": timer_minute, "second": timer_second}
        if hide_second:
            del timer_params["second"]
        tprint(timer_template.format(**timer_params), font=face, sep="\n" + " " * h_shift)
        if not hide_datetime:
            print_date_time(h_shift, date_system)
        print(message)
        if timer_hour == hour and timer_minute == minute and timer_second == second:
            print(" " * h_shift, end='')
            print("End!")
            if alarm:
                play_alarm(tone, alarm_repeat)
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
        sign=DEFAULT_PARAMS["sign"],
        hide_second=DEFAULT_PARAMS["hide_second"],
        hide_datetime=DEFAULT_PARAMS["hide_datetime"],
        vertical=DEFAULT_PARAMS["vertical"],
        date_system=DEFAULT_PARAMS["date_system"]):
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
    :param hide_second: hide second flag
    :type hide_second: bool
    :param hide_datetime: hide date/time flag
    :type hide_datetime: bool
    :param vertical: vertical mode flag
    :type vertical: bool
    :param date_system: date system
    :type date_system: str
    :return: None
    """
    face = get_face(face)
    timer_template = TIME_HMS_TEMPLATE_VERTICAL if vertical else TIME_HMS_TEMPLATE_HORIZONTAL
    if hide_second:
        timer_template = TIME_HM_TEMPLATE_VERTICAL if vertical else TIME_HM_TEMPLATE_HORIZONTAL
    while True:
        start = time.perf_counter()
        clear_screen()
        print('\n' * v_shift, end='')
        print(" " * h_shift, end='')
        timer_params = {"sign": sign, "hour": hour, "minute": minute, "second": second}
        if hide_second:
            del timer_params["second"]
        tprint(timer_template.format(**timer_params), font=face, sep="\n" + " " * h_shift)
        if not hide_datetime:
            print_date_time(h_shift, date_system)
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
                play_alarm(tone, alarm_repeat)
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
        work_params["message"] += " {round}/{repeat}".format(round=index + 1, repeat=4)
        timer_func(**work_params)
        if index == 3:
            break
        print_message(message=NEXT_PROGRAM_MESSAGE.format(next_program="Short break"), h_shift=h_shift, confirm=True)
        timer_func(**short_break_params)
        print_message(message=NEXT_PROGRAM_MESSAGE.format(
            next_program="Work {round}/{repeat}".format(round=index + 2, repeat=4)), h_shift=h_shift, confirm=True)
    print_message(message=NEXT_PROGRAM_MESSAGE.format(next_program="Long break"), h_shift=h_shift, confirm=True)
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
    print_message(message=NEXT_PROGRAM_MESSAGE.format(next_program="Break"), h_shift=h_shift, confirm=True)
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
        params["message"] = SET_ON_MESSAGE.format(hour=params["hour"], minute=params["minute"], second=params["second"])
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
    elif args.info:
        mytimer_info()
    elif args.faces_list:
        show_faces_list()
    elif args.programs_list:
        show_programs_list()
    elif args.test_tone:
        test_tone(params["tone"], params["alarm_repeat"])
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
            end_round_message = END_ROUND_MESSAGE.format(
                round="{round}/{repeat}".format(round=timer_round, repeat=args.repeat))
            if args.repeat == -1:
                end_round_message = END_ROUND_MESSAGE.format(round=timer_round)
            if timer_round < args.repeat or args.repeat == -1:
                print_message(
                    message=end_round_message,
                    h_shift=params["h_shift"],
                    confirm=True)
            timer_round += 1
        if args.keep_on:
            keep_on_timer(params)
