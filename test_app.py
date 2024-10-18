"""Torrent: A simple Python program to build and break pytests."""
import sys
import os
import time

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
        print("Cleaning up and exiting...")
        time.sleep(1)
        clear_terminal()
    except AssertionError as e:
        print(f"Test failed: {e}")

# End-of-file (EOF)
