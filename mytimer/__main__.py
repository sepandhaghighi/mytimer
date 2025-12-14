# -*- coding: utf-8 -*-
"""mytimer main."""
from mytimer.params import EXIT_MESSAGE
from mytimer.functions import handle_args, run_timer


def main() -> None:
    """CLI main function."""
    args = handle_args()
    try:
        run_timer(args)
    except (KeyboardInterrupt, EOFError):
        print(EXIT_MESSAGE)


if __name__ == "__main__":
    main()
