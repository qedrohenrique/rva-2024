import math

from UI.ANSI_terminal_operators import *


SPACE_BETWEEN_OPTIONS = 3
TOP_MARGIN = 5


def print_logo(screen_width: int):
    string = r"""
  _________                    .______.            _________  ____   ____
 /   _____/_____     ____    __| _/\_ |__    ____  \_   ___ \ \   \ /   /
 \_____  \ \__  \   /    \  / __ |  | __ \  /  _ \ /    \  \/  \   Y   / 
 /        \ / __ \_|   |  \/ /_/ |  | \_\ \(  <_> )\     \____  \     /  
/_______  /(____  /|___|  /\____ |  |___  / \____/  \______  /   \___/   
        \/      \/      \/      \/      \/                 \/
"""
    lines = string.split("\n")[1:]
    width = len(lines[0])
    print(math.ceil((screen_width - width) / 2) * " ")
    for line in lines:
        print(line)
        move_cursor_backward(width)

def print_options(options: list[str], screen_width, space_between_options):
    left_margin = math.ceil((screen_width * 0.7) / 2)
    for i, option in enumerate(options):
        move_cursor_down(space_between_options)
        move_cursor_forward(left_margin)
        print(option, end="")
        move_cursor_forward(screen_width - (2 * left_margin) - len(option) - 3)
        print(f"[{i}]", end="\r")
    move_cursor_up(space_between_options * (len(options) - 1))
    move_cursor_forward(left_margin)

def print_menu(screen_width: int, options: dict[str, callable]):
    print("\n" * TOP_MARGIN)
    print_logo(screen_width)
    print_options(options.keys(), screen_width, SPACE_BETWEEN_OPTIONS)

