# -*- coding: utf-8 -*-
"""mytimer main."""
from mytimer.params import MY_TIMER_VERSION, EXIT_MESSAGE
from mytimer.functions import set_color, set_bg_color, set_intensity
from mytimer.functions import load_params, select_timer_function
from mytimer.functions import update_set_on_params, print_mytimer_info
from mytimer.functions import show_faces_list, show_programs_list, test_tone
from mytimer.functions import handle_args, run_timer


def main() -> None:
    """CLI main function."""
    args = handle_args()
    set_color(color=args.color)
    set_bg_color(bg_color=args.bg_color)
    set_intensity(intensity=args.intensity)
    params = load_params(args)
    timer_function, params = select_timer_function(args, params)
    if args.set_on:
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
        if program == "pomodoro":
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


if __name__ == "__main__":
    main()
