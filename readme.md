# Pomodoro Timer with Speech and Visual Countdown

This repository provides two versions of a Pomodoro Timer with voice prompts and visual countdowns, specially designed for use in terminal environments.

## Features

- **pomodoro.py**: Original version of the Pomodoro Timer using enlarged pixel graphics and terminal clear for visual countdown.
- **pomodoro_curses.py**: Updated version utilizing the `curses` library for smoother terminal updates without clearing scrollback history.
- Displays the countdown time using enlarged pixel graphics for clear visibility.
- Speaks out alerts for starting Pomodoro, taking breaks, and completing a cycle.
- Alert beep sounds at the end of each timer.
- After every 4 Pomodoros, suggests a longer 15-minute break.
- User can opt to skip breaks or exit the loop.

## Modules & Functions

### Common Modules

- **os** and **time**: Used for system operations and time-based functions respectively.
  
### Specific to `pomodoro_curses.py`

- **curses**: Enables smooth visual updates without clearing terminal scrollback history.

## Main Functions in `pomodoro_curses.py`

### `display_enlarged_pixel_time(stdscr, minutes, seconds)`

- Takes minutes and seconds as arguments and displays them in an enlarged pixel format in the terminal using `curses`.

### `say_and_print(stdscr, message)`

- Prints the provided message to the terminal using `curses`.
- If on macOS, it also speaks the message aloud.

### `countdown_timer(stdscr, seconds)`

- Performs the countdown given an initial number of seconds.
- Displays the countdown in the enlarged pixel format and refreshes the screen each second without clearing the scrollback history.

### `pomodoro_timer_with_curses(stdscr)`

- The main function that executes the Pomodoro timer logic for the `curses` version.
- Provides voice prompts and manages the sequence of work and break timers.
- After 4 Pomodoros, suggests a 15-minute break instead of the standard 5-minute one.
- Gives the user the option to skip breaks or exit.

## Main Functions in `pomodoro.py`

### `display_enlarged_pixel_time(minutes, seconds)`

- Displays the countdown in an enlarged pixel format in the terminal.
  
### `say_and_print(message)`

- Prints the provided message to the terminal and speaks it aloud on macOS.

### `clear_terminal()`

- Clears the terminal screen each second for the original version, causing terminal history warnings on some systems.

### `countdown_timer(seconds)`

- Performs the countdown and clears the terminal screen each second for a clean update.
  
### `pomodoro_timer_with_speech()`

- Manages the Pomodoro workflow with voice prompts and user interaction options.

## Pixel Graphics

Both versions use the same enlarged pixel graphics for numbers (0-9) and colon (:) stored in a dictionary named `enlarged_pixel_numbers`. Each entry represents a number or symbol and its corresponding 7-row pixel graphic.

## Usage

To use either version:

1. **pomodoro.py**: Run `python3 pomodoro.py` for the original version.
2. **pomodoro_curses.py**: Run `python3 pomodoro_curses.py` for the updated version with `curses`.

The program will guide you through the Pomodoro process with voice prompts and printed messages.

**Note**: Some functionalities (like voice prompts) are OS-specific. Ensure compatibility or modify the script accordingly to cater to your environment.

Thank you for using the Pomodoro Timer with Speech and Visual Countdown!