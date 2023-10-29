import os
import time
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
def display_enlarged_pixel_time(minutes, seconds):
    """Display the time in enlarged pixel graphics."""
    # Convert minutes and seconds to strings
    min_str = str(minutes).zfill(2)
    sec_str = str(seconds).zfill(2)
    
    # Combine the strings with a colon in between
    time_str = min_str + ":" + sec_str
    
    # Loop over each row of the pixel graphics
    for row in range(7):  # 7 rows for the enlarged numbers
        for char in time_str:
            # Print each character's pixel graphic side by side
            print(enlarged_pixel_numbers[char][row], end=" ")
        print()  # Move to the next line after each row

def say_and_print(message):
    """Prints the message and speaks it aloud if on macOS."""
    print(message)
    if os.name != 'nt':  # Not Windows, so likely macOS or Linux. This will use say command on macOS.
        os.system(f'say "{message}"')
def clear_terminal():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def beep_alert():
    if os.name == 'nt':  # Windows
        import winsound  # Import winsound only when in Windows
        winsound.Beep(1000, 1000)  # Frequency 1000 Hz, Duration 1 second
    else:
        # macOS and some Unix-based systems
        os.system('say "Time is up!"')

def countdown_timer(seconds):
    clear_terminal()  # Clear the terminal before starting the countdown
    while seconds:
        mins, secs = divmod(seconds, 60)
        display_enlarged_pixel_time(mins, secs)
        time.sleep(1)
        clear_terminal()  # Clear the terminal each second for a clean update
        seconds -= 1


def pomodoro_timer_with_speech():
    pomodoro_count = 0
    while True:
        message = f"Starting Pomodoro #{pomodoro_count + 1} ..."
        say_and_print(message)
        countdown_timer(25 * 60)  # 25 minutes
        beep_alert()
        pomodoro_count += 1
        
        if pomodoro_count % 4 == 0:
            message = "\nYou've completed 4 Pomodoros! Take a 15-minute break."
            say_and_print(message)
            user_input = input("Press 's' to start a 15-minute break, or 'q' to quit: ").lower()
            if user_input == 's':
                countdown_timer(15 * 60)  # 15 minutes
                beep_alert()
            elif user_input == 'q':
                break
        else:
            message = "\nPomodoro complete! Take a 5-minute break."
            say_and_print(message)
            user_input = input("Press 's' to start a 5-minute break, or 'q' to quit: ").lower()
            if user_input == 's':
                countdown_timer(5 * 60)  # 5 minutes
                beep_alert()
            elif user_input == 'q':
                break
        
        clear_terminal()

    message = "Thank you for using the Pomodoro Timer!"
    say_and_print(message)

# Commented out for this environment.
pomodoro_timer_with_speech()
