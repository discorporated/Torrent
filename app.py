"""Torrent: A simple Python program to print 'Hello World'."""
import sys

def hello_world():
    """Function printing python version."""
    version_string="Running Python Version "+sys.version
    print(version_string)
    return "Hello World"

def test_hello_world():
    """Function testing hellow_world()."""
    # Assertion to verify the behavior of hello_world function
    assert hello_world() == "Hello World", "The function did not return 'Hello World' as expected."

# Run the test (optional in local development; pytest will handle this in CI)
if __name__ == "__main__":
    print(hello_world())


# End-of-file (EOF)
