"""Torrent: A simple Python program to print 'Hello World'."""
import sys

def hello_world():
    """Function returning 'Hello World' and printing Python version."""
    version_string = "Running Python Version " + sys.version
    print(version_string)
    return "Hello World"

def test_hello_world():
    """Function testing hello_world()."""
    # Assertion to verify the behavior of hello_world function
    assert hello_world() == "Hello World", "The function did not return 'Hello World' as expected."

# End-of-file (EOF)
