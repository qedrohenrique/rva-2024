import math
import shutil
import sys
import termios
import tty

from UseCases import options
from UI.ANSI_terminal_operators import *
from UI.info_texts import *
from UI.menu import *


explanation_options = {
    "object tracking": explain_object_tracking,
    "object recognition": explain_object_recognition,
    "object_reconstruction": explain_object_reconstruction,
    "image_segmentation": explain_image_segmentation
}

def main():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    tty.setraw(sys.stdin)

    selected = 0
    info_screen = False

    clear_screen()
    move_to(0, 0)

    screen_width, _ = shutil.get_terminal_size()

    print_menu(screen_width, options)
    
    while True:
        ch = sys.stdin.read(1)

        if ch in ["q"]:
            break

        if info_screen:
            if ch == "m":
                clear_screen()
                move_to(0, 0)
                print_menu(screen_width, options)
                info_screen = False
                for i in range(selected):
                    move_cursor_down(SPACE_BETWEEN_OPTIONS)
            continue

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

        if ch == "i":
            clear_screen()
            move_to(0, 0)
            list(explanation_options.values())[selected](screen_width)
            info_screen = True

        if ch.isdigit():
            val = int(ch)
            if val >= 0 and val < len(options.values()):
                clear_screen()
                move_to(0, 0)
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
                list(options.values())[val]()

    clear_screen()
    move_to(0, 0)
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

