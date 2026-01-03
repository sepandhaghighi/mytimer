# -*- coding: utf-8 -*-
"""mytimer functions."""
from typing import Tuple, Dict, Any, Callable, Union
import os
import sys
import time
import datetime
import jdatetime
import random
import argparse
from nava import play
from colorama import Fore, Back, Style
from mytimer.params import INPUT_ERROR_MESSAGE, SOUND_ERROR_MESSAGE
from mytimer.params import INPUT_EXAMPLE, TIME_ELEMENTS, MESSAGE_TEMPLATE
from mytimer.params import FACES_MAP, PROGRAMS_MAP, BREAKS_MAP, TONES_MAP
from mytimer.params import MY_TIMER_VERSION, PROGRAMS_LIST_TEMPLATE, EXIT_MESSAGE
from mytimer.params import FACES_LIST_EXAMPLE_MESSAGE
from mytimer.params import DEFAULT_PARAMS, PROGRAMS_DEFAULTS, BREAKS_DEFAULTS
from mytimer.params import NEXT_PROGRAM_MESSAGE, END_ROUND_MESSAGE
from mytimer.params import KEEP_ON_MESSAGE, SET_ON_MESSAGE
from mytimer.params import KEEP_ON_MAX
from mytimer.params import MY_TIMER_OVERVIEW, MY_TIMER_REPO
from mytimer.params import TIME_HMS_TEMPLATE_HORIZONTAL, TIME_HM_TEMPLATE_HORIZONTAL
from mytimer.params import TIME_HMS_TEMPLATE_VERTICAL, TIME_HM_TEMPLATE_VERTICAL
from mytimer.params import CLOCK_FORMAT, DATE_FORMAT
from mytimer.params import FACES_LIST, TONES_LIST
from mytimer.params import ADDITIONAL_INFO, SIGNS_LIST
from mytimer.params import DATE_SYSTEMS_LIST, COLORS_LIST, INTENSITY_LIST
from art import tprint


def print_message(
        message: str,
        v_shift: int = 0,
        h_shift: int = 0,
        confirm: bool = False) -> None:
    """
    Print message.

    :param message: message text
    :param v_shift: vertical shift
    :param h_shift: horizontal shift
    :param confirm: confirm flag
    """
    function = print
    if confirm:
        function = input
    print('\n' * v_shift, end='')
    function(h_shift * " " + message)


def print_mytimer_info() -> None:
    """Print mytimer info."""
    tprint("MyTimer")
    tprint("V:" + MY_TIMER_VERSION)
    print(MY_TIMER_OVERVIEW)
    print(MY_TIMER_REPO)


def load_program_params(program_name: str, is_break: bool = False) -> Dict[str, Any]:
    """
    Load program/break params.

    :param program_name: program name
    :param is_break: break flag
    """
    program_params = dict()
    reference_map = PROGRAMS_MAP
    reference_defaults = PROGRAMS_DEFAULTS
    if is_break:
        reference_map = BREAKS_MAP
        reference_defaults = BREAKS_DEFAULTS
    for item in DEFAULT_PARAMS:
        if item in reference_map[program_name]:
            program_params[item] = reference_map[program_name][item]
        elif item in reference_defaults:
            program_params[item] = reference_defaults[item]
        else:
            program_params[item] = DEFAULT_PARAMS[item]
    return program_params


def show_programs_list() -> None:
    """Show programs list."""
    print("Programs list:\n")
    for i, program in enumerate(sorted(PROGRAMS_MAP), 1):
        print(
            PROGRAMS_LIST_TEMPLATE.format(
                index=i,
                program=program,
                message=PROGRAMS_MAP[program]['message']))


def show_faces_list() -> None:
    """Show faces list."""
    print("Faces list:\n")
    for i in sorted(FACES_MAP):
        print('Face {}\n'.format(i))
        tprint(FACES_LIST_EXAMPLE_MESSAGE, font=get_face(i))
        print('=' * 80)


def check_null_time(args: argparse.Namespace) -> bool:
    """
    Check that all time elements are null or not.

    :param args: input arguments
    """
    for item in TIME_ELEMENTS:
        if getattr(args, item) is not None:
            return False
    return True


def load_params(args: argparse.Namespace, program: str = None, is_break: bool = False) -> Dict[str, Any]:
    """
    Load params.

    :param args: input arguments
    :param program: program name
    :param is_break: break flag
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


def input_handler(function: Callable) -> Callable:
    """
    Input handler decorator for timer functions.

    :param function: input function
    """
    def inner_function(
            hour: int,
            minute: int,
            second: int,
            alarm: bool,
            face: int,
            message: str,
            tone: int,
            alarm_repeat: int,
            v_shift: int,
            h_shift: int,
            sign: str,
            hide_second: bool,
            hide_datetime: bool,
            vertical: bool,
            date_system: str) -> None:
        """
        Inner function.

        :param hour: hour
        :param minute: minute
        :param second: second
        :param alarm: alarm flag
        :param face: face index
        :param message: message
        :param tone: tone index
        :param alarm_repeat: alarm repeat
        :param v_shift: vertical shift
        :param h_shift: horizontal shift
        :param sign: timer sign
        :param hide_second: hide second flag
        :param hide_datetime: hide date/time flag
        :param vertical: vertical mode flag
        :param date_system: date system
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
            function(
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


def clear_screen() -> None:
    """Clear screen function."""
    if sys.platform == "win32":
        os.system('cls')
    else:
        os.system('clear')


def get_face(index: int) -> str:
    """
    Return face name.

    :param index: face index
    """
    if index == -1:
        index = random.choice(sorted(FACES_MAP))
    return FACES_MAP[index]


def set_color(color: str) -> None:
    """
    Set text color.

    :param color: color name
    """
    if color:
        color = color.strip().upper()
        if color.startswith("LIGHT"):
            color += "_EX"
        print(getattr(Fore, color, ""), end="")


def set_bg_color(bg_color: str) -> None:
    """
    Set background color.

    :param bg_color: background color name
    """
    if bg_color:
        bg_color = bg_color.strip().upper()
        if bg_color.startswith("LIGHT"):
            bg_color += "_EX"
        print(getattr(Back, bg_color, ""))


def set_intensity(intensity: str) -> None:
    """
    Set text intensity.

    :param intensity: intensity name
    """
    if intensity:
        intensity = intensity.strip().upper()
        print(getattr(Style, intensity, ""), end="")


def get_tone(index: int) -> str:
    """
    Return tone file name.

    :param index: tone index
    """
    if index == -1:
        index = random.choice(sorted(TONES_MAP))
    return TONES_MAP[index]


def get_sound_path(sound_name: str) -> str:
    """
    Return sound path.

    :param sound_name: .wav sound name
    """
    cd, _ = os.path.split(__file__)
    return os.path.join(cd, "sounds", sound_name)


def play_sound(sound_path: str) -> None:
    """
    Play sound.

    :param sound_path: sound path
    """
    try:
        play(sound_path)
    except Exception:
        print(SOUND_ERROR_MESSAGE)


def play_alarm(tone: int, repeat: int) -> None:
    """
    Play alarm.

    :param tone: alarm tone index
    :param repeat: alarm repeat
    """
    tone = get_tone(tone)
    sound_path = get_sound_path(tone)
    for _ in range(repeat):
        play_sound(sound_path)


def test_tone(tone: int, repeat: int) -> None:
    """
    Test tone.

    :param tone: alarm tone index
    :param repeat: alarm repeat
    """
    print("Tone: {tone}".format(tone=tone))
    print("Repeat: {repeat}".format(repeat=repeat))
    start = time.perf_counter()
    play_alarm(tone, repeat)
    end = time.perf_counter()
    duration = round(end - start, 4)
    print("Duration: {duration} s".format(duration=duration))


def print_date_time(start_datetime: Union[datetime.datetime, jdatetime.datetime],
                    current_datetime: Union[datetime.datetime, jdatetime.datetime], h_shift: int) -> None:
    """
    Print date and time.

    :param start_datetime: start date and time
    :param current_datetime: current date and time
    :param h_shift: horizontal shift
    """
    current_time = current_datetime.strftime(CLOCK_FORMAT)
    current_date = current_datetime.strftime(DATE_FORMAT)
    start_time = start_datetime.strftime(CLOCK_FORMAT)
    print(" " * h_shift, end='')
    print("Start  : {start_time}".format(start_time=start_time))
    print(" " * h_shift, end='')
    print("Current: {current_time}".format(current_time=current_time))
    print(" " * h_shift, end='')
    print(current_date)
    print("")
    print(" " * h_shift, end='')


@input_handler
def countup_timer(
        hour: int,
        minute: int,
        second: int,
        alarm: bool = DEFAULT_PARAMS["alarm"],
        face: int = DEFAULT_PARAMS["face"],
        message: str = DEFAULT_PARAMS["message"],
        tone: int = DEFAULT_PARAMS["tone"],
        alarm_repeat: int = DEFAULT_PARAMS["alarm_repeat"],
        v_shift: int = DEFAULT_PARAMS["v_shift"],
        h_shift: int = DEFAULT_PARAMS["h_shift"],
        sign: str = DEFAULT_PARAMS["sign"],
        hide_second: bool = DEFAULT_PARAMS["hide_second"],
        hide_datetime: bool = DEFAULT_PARAMS["hide_datetime"],
        vertical: bool = DEFAULT_PARAMS["vertical"],
        date_system: str = DEFAULT_PARAMS["date_system"]) -> None:
    """
    Count-up timer function.

    :param hour: hour
    :param minute: minute
    :param second: second
    :param alarm: alarm flag
    :param face: face index
    :param message: message
    :param tone: tone index
    :param alarm_repeat: alarm repeat
    :param v_shift: vertical shift
    :param h_shift: horizontal shift
    :param sign: timer sign
    :param hide_second: hide second flag
    :param hide_datetime: hide date/time flag
    :param vertical: vertical mode flag
    :param date_system: date system
    """
    timer_second = 0
    timer_minute = 0
    timer_hour = 0
    face = get_face(face)
    timer_template = TIME_HMS_TEMPLATE_VERTICAL if vertical else TIME_HMS_TEMPLATE_HORIZONTAL
    if hide_second:
        timer_template = TIME_HM_TEMPLATE_VERTICAL if vertical else TIME_HM_TEMPLATE_HORIZONTAL
    datetime_lib = datetime
    if date_system == "jalali":
        datetime_lib = jdatetime
    start_datetime = datetime_lib.datetime.now()
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
            current_datetime = datetime_lib.datetime.now()
            print_date_time(start_datetime, current_datetime, h_shift)
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
        hour: int,
        minute: int,
        second: int,
        alarm: bool = DEFAULT_PARAMS["alarm"],
        face: int = DEFAULT_PARAMS["face"],
        message: str = DEFAULT_PARAMS["message"],
        tone: int = DEFAULT_PARAMS["tone"],
        alarm_repeat: int = DEFAULT_PARAMS["alarm_repeat"],
        v_shift: int = DEFAULT_PARAMS["v_shift"],
        h_shift: int = DEFAULT_PARAMS["h_shift"],
        sign: str = DEFAULT_PARAMS["sign"],
        hide_second: bool = DEFAULT_PARAMS["hide_second"],
        hide_datetime: bool = DEFAULT_PARAMS["hide_datetime"],
        vertical: bool = DEFAULT_PARAMS["vertical"],
        date_system: str = DEFAULT_PARAMS["date_system"]) -> None:
    """
    Countdown timer function.

    :param hour: hour
    :param minute: minute
    :param second: second
    :param alarm: alarm flag
    :param face: face index
    :param message: message
    :param tone: tone index
    :param alarm_repeat: alarm repeat
    :param v_shift: vertical shift
    :param h_shift: horizontal shift
    :param sign: timer sign
    :param hide_second: hide second flag
    :param hide_datetime: hide date/time flag
    :param vertical: vertical mode flag
    :param date_system: date system
    """
    face = get_face(face)
    timer_template = TIME_HMS_TEMPLATE_VERTICAL if vertical else TIME_HMS_TEMPLATE_HORIZONTAL
    if hide_second:
        timer_template = TIME_HM_TEMPLATE_VERTICAL if vertical else TIME_HM_TEMPLATE_HORIZONTAL
    datetime_lib = datetime
    if date_system == "jalali":
        datetime_lib = jdatetime
    start_datetime = datetime_lib.datetime.now()
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
            current_datetime = datetime_lib.datetime.now()
            print_date_time(start_datetime, current_datetime, h_shift)
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


def pomodoro_timer(
        timer_function: Callable,
        params: Dict[str, Any],
        long_break_params: Dict[str, Any],
        short_break_params: Dict[str, Any]) -> None:
    """
    Pomodoro timer function.

    :param timer_function: timer function
    :param params: program params
    :param long_break_params: long break params
    :param short_break_params: short break params
    """
    h_shift = params["h_shift"]
    for index in range(4):
        work_params = params.copy()
        work_params["message"] += " {round}/{repeat}".format(round=index + 1, repeat=4)
        timer_function(**work_params)
        if index == 3:
            break
        print_message(message=NEXT_PROGRAM_MESSAGE.format(next_program="Short break"), h_shift=h_shift, confirm=True)
        timer_function(**short_break_params)
        print_message(message=NEXT_PROGRAM_MESSAGE.format(
            next_program="Work {round}/{repeat}".format(round=index + 2, repeat=4)), h_shift=h_shift, confirm=True)
    print_message(message=NEXT_PROGRAM_MESSAGE.format(next_program="Long break"), h_shift=h_shift, confirm=True)
    timer_function(**long_break_params)


def two_step_timer(timer_function: Callable, params1: Dict[str, Any], params2: Dict[str, Any]) -> None:
    """
    Two step timer function.

    :param timer_function: timer function
    :param params1: program-1 params
    :param params2: program-2 params
    """
    h_shift = params1["h_shift"]
    timer_function(**params1)
    print_message(message=NEXT_PROGRAM_MESSAGE.format(next_program="Break"), h_shift=h_shift, confirm=True)
    timer_function(**params2)


def keep_on_timer(params: Dict[str, Any]) -> None:
    """
    Keep-on timer.

    :param params: timer params
    """
    params["hour"] = KEEP_ON_MAX
    params["message"] += KEEP_ON_MESSAGE
    if params["sign"] in ["+", ""]:
        params["sign"] = "-"
    else:
        params["sign"] = "+"
    countup_timer(**params)


def update_set_on_params(params: Dict[str, Any]) -> Dict[str, Any]:
    """
    Update set-on mode params.

    :param params: timer params
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


def select_timer_function(args: argparse.Namespace, params: Dict[str, Any]) -> Tuple[Callable, Dict[str, Any]]:
    """
    Select timer function and parameters.

    :param args: input arguments
    :param params: timer params
    """
    timer_function = countdown_timer
    if args.countup:
        timer_function = countup_timer
    if args.countdown:
        timer_function = countdown_timer
    else:
        if check_null_time(args) and not args.program:
            params["hour"] = KEEP_ON_MAX
            timer_function = countup_timer
    return timer_function, params


def handle_args() -> argparse.Namespace:
    """Handle CLI arguments."""
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
        '--color',
        help='text color',
        type=str.lower,
        choices=COLORS_LIST)
    parser.add_argument(
        '--bg-color',
        help='background color',
        type=str.lower,
        choices=COLORS_LIST)
    parser.add_argument(
        '--intensity',
        help='text intensity',
        type=str.lower,
        choices=INTENSITY_LIST)
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
    parser.add_argument(
        '--date-system',
        help='date system',
        type=str.lower,
        choices=DATE_SYSTEMS_LIST,
        default="gregorian")
    parser.add_argument(
        '--programs-list',
        help='programs list',
        nargs="?",
        const=1)
    args = parser.parse_args()
    return args


def run_timer(timer_function: Callable, params: Dict[str, dict], repeat: int, program: str, keep_on: bool) -> None:
    """
    Run timer.

    :param timer_function: timer function
    :param params: timer and breaks params
    :param repeat: number of repeats
    :param program: program name
    :param keep_on: keep-on flag
    """
    try:
        timer_round = 1
        while timer_round <= repeat or repeat == -1:
            if program == "pomodoro":
                pomodoro_timer(
                    timer_function,
                    params=params["timer"],
                    long_break_params=params["long_break"],
                    short_break_params=params["short_break"])
            elif program in ["52-17", "112-26", "animedoro"]:
                two_step_timer(timer_function, params1=params["timer"], params2=params["break"])
            else:
                timer_function(**params["timer"])
            end_round_message = END_ROUND_MESSAGE.format(
                round="{round}/{repeat}".format(round=timer_round, repeat=repeat))
            if repeat == -1:
                end_round_message = END_ROUND_MESSAGE.format(round=timer_round)
            if timer_round < repeat or repeat == -1:
                print_message(
                    message=end_round_message,
                    h_shift=params["timer"]["h_shift"],
                    confirm=True)
            timer_round += 1
        if keep_on:
            keep_on_timer(params["timer"])
    except (KeyboardInterrupt, EOFError):
        print(EXIT_MESSAGE)


def main() -> None:
    """CLI main function."""
    args = handle_args()
    set_color(color=args.color)
    set_bg_color(bg_color=args.bg_color)
    set_intensity(intensity=args.intensity)
    params = load_params(args)
    timer_function, params = select_timer_function(args, params)
    if args.set_on and not args.program:
        params = update_set_on_params(params)
    if args.version:
        print(MY_TIMER_VERSION)
    elif args.info:
        print_mytimer_info()
    elif args.faces_list:
        show_faces_list()
    elif args.programs_list:
        show_programs_list()
    elif args.test_tone:
        test_tone(params["tone"], params["alarm_repeat"])
    else:
        params_dict = {"timer": params}
        if args.program == "pomodoro":
            params_dict["short_break"] = load_params(args, program="pomodoro-short-break", is_break=True)
            params_dict["long_break"] = load_params(args, program="pomodoro-long-break", is_break=True)
        elif args.program in ["52-17", "112-26", "animedoro"]:
            params_dict["break"] = load_params(args, is_break=True)
        try:
            run_timer(
                timer_function=timer_function,
                params=params_dict,
                repeat=args.repeat,
                program=args.program,
                keep_on=args.keep_on)
        except (KeyboardInterrupt, EOFError):
            print(EXIT_MESSAGE)
