import math
import sys


def clear_screen():
    sys.stdout.write(f"\033[2J")
    sys.stdout.flush()

def move_to(x, y):
    sys.stdout.write(f"\033[{x};{y}H")
    sys.stdout.flush()

def move_cursor_up(lines: int = 1):
    sys.stdout.write(f"\033[{lines}A")
    sys.stdout.flush()

def move_cursor_down(lines: int = 1):
    sys.stdout.write(f"\033[{lines}B")
    sys.stdout.flush()

def move_cursor_forward(columns: int = 1):
    sys.stdout.write(f"\033[{columns}C")
    sys.stdout.flush()

def move_cursor_backward(columns: int = 1):
    sys.stdout.write(f"\033[{columns}D")
    sys.stdout.flush()

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

