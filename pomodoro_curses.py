import os
import time
import curses
# Define the enlarged pixel graphics for numbers
enlarged_pixel_numbers = {
    "0": [
        "  █████  ",
        " █     █ ",
        " █     █ ",
        " █     █ ",
        " █     █ ",
        " █     █ ",
        "  █████  "
    ],
    "1": [
        "    █    ",
        "   ██    ",
        "    █    ",
        "    █    ",
        "    █    ",
        "    █    ",
        "  █████  "
    ],
    "2": [
        "  █████  ",
        " █     █ ",
        "       █ ",
        "      █  ",
        "     █   ",
        "   █     ",
        " ██████  "
    ],
    "3": [
        "  █████  ",
        " █     █ ",
        "       █ ",
        "  █████  ",
        "       █ ",
        " █     █ ",
        "  █████  "
    ],
    "4": [
        " █      █ ",
        " █      █ ",
        " █      █ ",
        " ████████ ",
        "        █ ",
        "        █ ",
        "        █ "
    ],
    "5": [
        " ██████  ",
        " █       ",
        " █       ",
        " ██████  ",
        "       █ ",
        "       █ ",
        " ██████  "
    ],
    "6": [
        "  █████  ",
        " █       ",
        " █       ",
        " ██████  ",
        " █     █ ",
        " █     █ ",
        "  █████  "
    ],
    "7": [
        " ███████ ",
        "       █ ",
        "      █  ",
        "     █   ",
        "    █    ",
        "   █     ",
        "  █      "
    ],
    "8": [
        "  █████  ",
        " █     █ ",
        " █     █ ",
        "  █████  ",
        " █     █ ",
        " █     █ ",
        "  █████  "
    ],
    "9": [
        "  █████  ",
        " █     █ ",
        " █     █ ",
        "  ██████ ",
        "       █ ",
        "       █ ",
        "  █████  "
    ],
    ":": [
        "         ",
        "         ",
        "   ██    ",
        "         ",
        "         ",
        "   ██    ",
        "         "
    ]
}
def display_enlarged_pixel_time(stdscr, minutes, seconds):
    """Display the time in enlarged pixel graphics using curses."""
    stdscr.clear()
    min_str = str(minutes).zfill(2)
    sec_str = str(seconds).zfill(2)
    time_str = min_str + ":" + sec_str
    
    for row in range(7):  # 7 rows for the enlarged numbers
        for i, char in enumerate(time_str):
            stdscr.addstr(row, i * 10, enlarged_pixel_numbers[char][row])  # Position each character with some spacing
    stdscr.refresh()

def say_and_print(stdscr, message):
    """Prints the message and speaks it aloud if on macOS."""
    stdscr.addstr(10, 0, message)
    stdscr.refresh()
    if os.name != 'nt':  # Not Windows, so likely macOS or Linux. This will use 'say' command on macOS.
        os.system(f'say "{message}"')

def countdown_timer(stdscr, seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        display_enlarged_pixel_time(stdscr, mins, secs)
        time.sleep(1)
        seconds -= 1

def pomodoro_timer_with_curses(stdscr):
    pomodoro_count = 0
    while True:
        message = f"Starting Pomodoro #{pomodoro_count + 1} ..."
        say_and_print(stdscr, message)
        countdown_timer(stdscr, 25 * 60)  # 25 minutes
        pomodoro_count += 1
        
        if pomodoro_count % 4 == 0:
            message = "\nYou've completed 4 Pomodoros! Take a 15-minute break."
            say_and_print(stdscr, message)
            countdown_timer(stdscr, 15 * 60)  # 15 minutes
        else:
            message = "\nPomodoro complete! Take a 5-minute break."
            say_and_print(stdscr, message)
            countdown_timer(stdscr, 5 * 60)  # 5 minutes

    message = "Thank you for using the Pomodoro Timer!"
    say_and_print(stdscr, message)

if __name__ == "__main__":
    curses.wrapper(pomodoro_timer_with_curses)