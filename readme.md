# Pomodoro Timer with Speech

This script provides a Pomodoro Timer with voice prompts and visual countdown, specially designed for use in terminal environments.

## Features

- Displays the countdown time using enlarged pixel graphics.
- Speaks out alerts for starting Pomodoro, taking breaks, and completing a cycle.
- Alert beep sounds at the end of each timer.
- After every 4 Pomodoros, suggests a longer 15-minute break.
- Clear visual countdown in the terminal for each minute and second.
- User can opt to skip breaks or exit the loop.

## Modules & Functions

- **os** and **time**: Used for system operations and time-based functions respectively.

### `display_enlarged_pixel_time(minutes, seconds)`

- This function takes minutes and seconds as arguments and displays them in an enlarged pixel format in the terminal.

### `say_and_print(message)`

- Prints the provided message to the terminal.
- If on macOS, it also speaks the message aloud.

### `clear_terminal()`

- Clears the terminal screen for clean timer updates.

### `beep_alert()`

- Produces a beep sound alert when called.
- It has platform-specific implementations for Windows (using `winsound`) and macOS (using the `say` command).

### `countdown_timer(seconds)`

- Performs the countdown, given an initial number of seconds.
- Displays the countdown in the enlarged pixel format and refreshes the terminal each second.

### `pomodoro_timer_with_speech()`

- The main function that executes the Pomodoro timer logic.
- Provides voice prompts and manages the sequence of work and break timers.
- After 4 Pomodoros, suggests a 15-minute break instead of the standard 5-minute one.
- Gives the user the option to skip breaks or exit.

## Pixel Graphics

The enlarged pixel graphics for numbers (0-9) and colon (:) are stored in a dictionary named `enlarged_pixel_numbers`. Each entry in the dictionary represents a number or symbol and its corresponding 7-row pixel graphic representation.

## Usage

Simply run the script in your preferred terminal or command prompt. The program will guide you through the process with voice prompts and printed messages.

**Note**: Some functionalities (like voice prompts) might be OS-specific. Ensure you're using a compatible OS or modify the script accordingly to cater to your specific environment.

Thank you for using the Pomodoro Timer with Speech!
