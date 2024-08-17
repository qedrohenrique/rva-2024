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

