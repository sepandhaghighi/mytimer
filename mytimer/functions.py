# -*- coding: utf-8 -*-
"""mytimer functions."""
import os
import sys
import subprocess
import time
from mytimer.params import INPUT_ERROR_MESSAGE, SOUND_ERROR_MESSAGE
from mytimer.params import INPUT_EXAMPLE, TIME_ELEMENTS, MESSAGE_TEMPLATE
from mytimer.params import FACES_MAP, PROGRAMS_MAP
from mytimer.params import MY_TIMER_VERSION
from art import tprint


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
    params = {
        "minute": 0,
        "hour": 0,
        "second": 0,
        "alarm": 0,
        "face": 1,
        "message": ""}
    if args.program:
        params = PROGRAMS_MAP[args.program]
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


def input_check(func):
    """
    Input check decorator for timer functions.

    :param func: input function
    :type func: function
    :return: inner function
    """
    def inner_function(hour, minute, second, alarm, face, message):
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
        :param face: face number
        :type face: int
        :param message: message
        :type message: str
        :return: None
        """
        message = message.strip()
        if len(message) > 0:
            message = MESSAGE_TEMPLATE.format(message)
        font = FACES_MAP[face]
        items_list = [hour, minute, second]
        if sum(items_list) != 0 and all(map(lambda x: x >= 0, items_list)):
            if second >= 60:
                minute += second // 60
                second %= 60
            if minute >= 60:
                hour += minute // 60
                minute %= 60
            func(hour, minute, second, alarm, font, message)
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


@input_check
def countup_timer(hour, minute, second, alarm, font=FACES_MAP[1], message=""):
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
    :param font: font name
    :type font: str
    :param message: message
    :type message: str
    :return: None
    """
    timer_second = 0
    timer_minute = 0
    timer_hour = 0
    while True:
        start = time.perf_counter()
        clear_screen()
        print('\n' * 5)
        tprint(
            '\t\t\t\t  %d : %d : %d ' %
            (timer_hour,
             timer_minute,
             timer_second),
            font=font)
        print(message)
        if timer_hour == hour and timer_minute == minute and timer_second == second:
            print("End!")
            if alarm:
                play_sound(get_sound_path("1.wav"))
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


@input_check
def countdown_timer(
        hour,
        minute,
        second,
        alarm,
        font=FACES_MAP[1],
        message=""):
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
    :param font: font name
    :type font: str
    :param message: message
    :type message: str
    :return: None
    """
    while True:
        start = time.perf_counter()
        clear_screen()
        print('\n' * 5)
        tprint('\t\t\t\t  %d : %d : %d ' %
               (hour, minute, second), font=font)
        print(message)
        second -= 1
        if second == -1:
            second = 59
            minute -= 1
        if minute == -1:
            minute = 59
            hour -= 1
        if hour == -1:
            print("End!")
            if alarm:
                play_sound(get_sound_path("1.wav"))
            break
        end = time.perf_counter()
        time.sleep(max(0, 1 - (end - start)))


def run_timer(args):
    """
    Run timer.

    :param args: input arguments
    :type args: argparse.Namespace
    :return: None
    """
    params = load_params(args)
    if args.version:
        print(MY_TIMER_VERSION)
    else:
        if args.countdown:
            countdown_timer(**params)
        else:
            countup_timer(**params)
