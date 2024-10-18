"""Torrent: A simple Python program to build and break pytests."""
#importing the required libraries
import sys
import os
import time


##Variables
CURRENT_ROUND = 1
SCORE=0
## Function Definitions
def clear_terminal():
    """Clears the terminal screen."""
    # Clear command as per the operating system
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')

def hello_world():
    """Function returning 'Hello World' and printing Python version."""
    version_string = "Running Python Version " + sys.version
    print(version_string)
    return "Hello World"

def test_hello_world():
    """Function testing hello_world()."""
    # Assertion to verify the behavior of hello_world function
    assert hello_world() == "Hello World", "The function did not return 'Hello World' as expected."

def start_the_round(current_round):
    """Function to start the round."""
    print(f"Starting Round {current_round}...")
    time.sleep(1)
    clear_terminal()
    print("Round started!")
    time.sleep(1)
    clear_terminal()
    print("Round completed!")
    time.sleep(1)
    clear_terminal()
    current_round += 1
    if current_round > 3:
        print("You win, game over!")
        time.sleep(1)
        clear_terminal()
        print("Thank you for playing Torrent!")
        time.sleep(1)
        clear_terminal()
        print("Exiting the game...")
        time.sleep(1)
        clear_terminal()
        sys.exit()
    else:
        start_the_round(current_round)

def start_the_game():
    """Function to start the game."""
    print("Starting the game...")
    time.sleep(1)
    clear_terminal()
    input("Are you ready, type yes to play... \n")
    if input() == "yes":
        print("Let's play the game!")
        time.sleep(1)
        clear_terminal()
        start_the_round(CURRENT_ROUND)
    else:
        print("I'll ask again...")
        time.sleep(1)
        clear_terminal()
        start_the_game()
# return the results of the test_hello_world function
if __name__ == "__main__":
    clear_terminal()  # Clears the terminal screen
    try:
        # Run the test case directly when the script is executed
        test_hello_world()
        print("Welcome to Torrent!")
        print("All tests loaded and passed successfully!")
        print("\n")
        TIMER =3
        while TIMER > 0:
            print(f"Countdown: {TIMER}")
            TIMER -= 1
            print("\n")
            time.sleep(1)
        print("Cleaning up and starting the game...")
        time.sleep(1)
        clear_terminal()
        start_the_game()
    except AssertionError as e:
        print(f"Test failed: {e}")

# End-of-file (EOF)
