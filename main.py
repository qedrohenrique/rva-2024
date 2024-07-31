import math
import shutil
import sys
import termios
import tty

from ANSI_terminal_operators import *
from UseCases import options


def main():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    tty.setraw(sys.stdin)

    selected = 0

    clear_screen()
    move_to(0, 0)

    screen_width, _ = shutil.get_terminal_size()

    SPACE_BETWEEN_OPTIONS = 3
    TOP_MARGIN = 5

    print("\n" * TOP_MARGIN)
    print_logo(screen_width)
    print_options(options.keys(), screen_width, SPACE_BETWEEN_OPTIONS)

    while True:
        ch = sys.stdin.read(1)

        if ch in ["j"]:
            if selected + 1 < len(options):
                selected += 1
                move_cursor_down(SPACE_BETWEEN_OPTIONS)

        if ch in ["k"]:
            if selected > 0:
                selected -= 1
                move_cursor_up(SPACE_BETWEEN_OPTIONS)

        if ch == "s":
            clear_screen()
            move_to(0, 0)
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            list(options.values())[selected]()

        if ch in ["q"]:
            break

    clear_screen()
    move_to(0, 0)
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

if __name__ == "__main__":
    main()

