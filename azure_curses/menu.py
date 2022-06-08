import curses
import curses.ascii
import os
import platform
from typing import List

class CursesWindow:
    ENTER_KEY = ord('\n')

    def __init__(self):
        self.window = curses.initscr()
        self.window.keypad(1) # interpret o.a. arrow keys
        
        curses.start_color() # activate colors (Required for init_pair)
        curses.noecho() # do not echo user input
        curses.cbreak() # read keys without waiting for ENTER
        curses.curs_set(0) # Hide cursor

        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        self.colors_highlight = curses.color_pair(1)
        self.colors_default = curses.A_NORMAL

        self.reset()
    
    def input(self):
        key = self.window.getch()
        return key

    def reset(self):
        self.window.erase()
        self.window.refresh()
        self.window.border(0)

        self.max_y, self.max_x = self.window.getmaxyx()
        text = f"[{self.max_y}, {self.max_x}]"
        self.write(self.max_x - (len(text) + 2), 0, text)
    
    def menu_help(self):
        self.write(2, self.max_y - 1, f"move: arrows / j/k - enter: select - esc: quit")
    
    def clear_terminal(self):
        PLATFORM_WINDOWS = "Windows"
        if platform.system() == PLATFORM_WINDOWS:
            os.system("cls")
        else:
            os.system("clear")
    
    def quit(self):
        curses.endwin()
        self.clear_terminal()        
    
    def write(self, x: int, y: int, text: str, highlight: bool = False):
        if text is not str:
            text = str(text)
        
        max_y, max_x = self.window.getmaxyx()
        
        # prevent writing outside of available area
        if 0 <= x and x + len(text) < max_x and 0 <= y < max_y:
            self.window.addstr(y, x, text, self.colors_highlight if highlight else self.colors_default)
    
    def menu(self, list_items: List) -> int:
        current_selected_index = 0

        max_width = max(len(x) for x in list_items)
        KEYS_UP = [curses.KEY_UP, ord('k')]
        KEYS_DOWN = [curses.KEY_DOWN, ord('j')]

        def draw_menu():
            for i, item in enumerate(list_items):
                x, y = 2, 1 + i

                highlight = i == current_selected_index
                text = (" " + item).ljust(max_width+2)
                self.write(x, y, text, highlight=highlight)
        
        self.menu_help()
        while True:
            draw_menu()

            key = self.input()
            
            if key == curses.ascii.ESC:
                self.quit()
                return
            elif key in KEYS_UP and current_selected_index != 0:
                current_selected_index -= 1
            elif key in KEYS_DOWN and current_selected_index + 1 != len(list_items):
                current_selected_index += 1
            elif key == self.ENTER_KEY:
                break
            elif key == ord('r'):
                self.reset()
                self.menu_help()

        return current_selected_index
