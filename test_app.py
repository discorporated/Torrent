"""
Torrent: A simple Python program that simulates a terminal-based game
where the player and AI move around a 10x10 checkerboard in a turn-based fashion.
"""
from collections import namedtuple
import sys
import os
import time
import random
import keyboard  # External library to capture arrow keys (install using `pip install keyboard`)


# Constants
MIN_TERMINAL_HEIGHT = 25
MIN_TERMINAL_WIDTH = 60
PLAYER_POS = [0, 0]
AI_POS = [9, 9]
CURRENT_ROUND = 1

# Clear terminal function
def clear_terminal():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

# Get terminal size
def get_terminal_size():
    """Get the current terminal size."""
    return os.get_terminal_size().lines, os.get_terminal_size().columns

# Check terminal size
def check_terminal_size():
    """Check if the terminal size is big enough for the game."""
    height, width = get_terminal_size()
    if height < MIN_TERMINAL_HEIGHT or width < MIN_TERMINAL_WIDTH:
        print(f"Terminal size is too small! Requires at least {MIN_TERMINAL_HEIGHT} lines "
              f"and {MIN_TERMINAL_WIDTH} columns.")
        return False
    return True

# Drawing the checkerboard with player and AI
def draw_checkerboard(player_pos, ai_pos):
    """Function to draw a 10x10 checkerboard pattern in the terminal with player and AI."""
    square_size = 10  # Each square is 5x5 characters
    board_size = 10  # Number of squares along one side (10 squares = 50 characters)
    white_square = " "  # Use space for white
    black_square = "█"  # Use block character for black
    player_char = "P"  # Character to represent the player
    ai_char = "E"  # Character to represent the AI enemy
    for row in range(board_size):  # Loop over rows of squares
        for _ in range(square_size):  # Repeat each row 'square_size' times to create height
            row_pattern = ""
            for col in range(board_size):  # Loop over columns of squares
                if row == player_pos[0] and col == player_pos[1]:
                    row_pattern += player_char * square_size  # Place the player
                elif row == ai_pos[0] and col == ai_pos[1]:
                    row_pattern += ai_char * square_size  # Place the AI enemy
                elif (row + col) % 2 == 0:
                    row_pattern += white_square * square_size  # Add a white square
                else:
                    row_pattern += black_square * square_size  # Add a black square
            print(row_pattern)  # Print one row of the checkerboard

# Move the player based on arrow key input
def move_player(key, player_pos):
    """Update player position based on arrow key input."""
    if key == "up" and player_pos[0] > 0:
        player_pos[0] -= 1  # Move up
    elif key == "down" and player_pos[0] < 9:
        player_pos[0] += 1  # Move down
    elif key == "left" and player_pos[1] > 0:
        player_pos[1] -= 1  # Move left
    elif key == "right" and player_pos[1] < 9:
        player_pos[1] += 1  # Move right
    return player_pos

# AI movement
def move_ai(ai_pos):
    """AI movement: AI will move randomly but avoids moving off the board."""
    moves = ['up', 'down', 'left', 'right']
    valid_move = False

    while not valid_move:
        move = random.choice(moves)
        if move == 'up' and ai_pos[0] > 0:
            ai_pos[0] -= 1
            valid_move = True
        elif move == 'down' and ai_pos[0] < 9:
            ai_pos[0] += 1
            valid_move = True
        elif move == 'left' and ai_pos[1] > 0:
            ai_pos[1] -= 1
            valid_move = True
        elif move == 'right' and ai_pos[1] < 9:
            ai_pos[1] += 1
            valid_move = True
    return ai_pos

# Turn-based game loop
def game_loop(player_pos, ai_pos, current_round):
    """Main game loop to handle player and AI movement, and round progression."""
    while True:
        clear_terminal()

        # Draw the game board with player and AI positions
        draw_checkerboard(player_pos, ai_pos)

        # Display round and prompt below the board
        print(f"\nRound: {current_round}")
        print("Use arrow keys to move. Press 'q' to quit.")

        # Player's turn: wait for valid arrow key input
        moved = False
        while not moved:
            if keyboard.is_pressed('up'):
                player_pos = move_player("up", player_pos)
                moved = True
            elif keyboard.is_pressed('down'):
                player_pos = move_player("down", player_pos)
                moved = True
            elif keyboard.is_pressed('left'):
                player_pos = move_player("left", player_pos)
                moved = True
            elif keyboard.is_pressed('right'):
                player_pos = move_player("right", player_pos)
                moved = True
            elif keyboard.is_pressed('q'):
                print("Exiting the game...")
                time.sleep(1)
                return

            time.sleep(0.1)  # Short delay to avoid key over-triggers

        # AI's turn (after player moves)
        time.sleep(0.5)  # Pause before AI moves
        ai_pos = move_ai(ai_pos)

        # Update and display the round number after both movements
        current_round += 1

# Start the game
def start_the_game():
    """Function to start the game after terminal size check."""
    if not check_terminal_size():
        time.sleep(3)
        sys.exit()  # Exit if the terminal is too small
    print("Starting the game...")
    time.sleep(1)
    clear_terminal()

    player_pos = [0, 0]  # Reset player position
    ai_pos = [9, 9]  # Reset AI position
    current_round = 1  # Reset the round counter

    game_loop(player_pos, ai_pos, current_round)  # Start the game loop for player and AI movement

# Hello World function for basic test
def hello_world():
    """Function returning 'Hello World'."""
    return "Hello World"

# === TESTS SECTION ===
# These are pytest-compatible tests
def test_hello_world():
    """Test hello_world function."""
    assert hello_world() == "Hello World"

def test_move_player():
    """Test move_player function."""
    player_pos = [5, 5]
    # Move up
    new_pos = move_player("up", player_pos.copy())
    assert new_pos == [4, 5]
    # Move down
    new_pos = move_player("down", player_pos.copy())
    assert new_pos == [6, 5]
    # Move left
    new_pos = move_player("left", player_pos.copy())
    assert new_pos == [5, 4]
    # Move right
    new_pos = move_player("right", player_pos.copy())
    assert new_pos == [5, 6]

def test_move_ai():
    """Test move_ai function to ensure AI moves within boundaries."""
    ai_pos = [5, 5]
    new_pos = move_ai(ai_pos.copy())
    # Ensure AI has moved
    assert new_pos != [5, 5]
    # Ensure AI position is within boundaries
    assert 0 <= new_pos[0] <= 9
    assert 0 <= new_pos[1] <= 9

def test_check_terminal_size(monkeypatch):
    """Test check_terminal_size to handle different terminal sizes."""
    # Create a mock terminal size class similar to os.terminal_size
    MockTerminalSize = namedtuple('terminal_size', ['columns', 'lines'])
    # Mock a terminal size that is too small
    def mock_small_terminal():
        return MockTerminalSize(columns=40, lines=20)  # Too small
    monkeypatch.setattr(os, 'get_terminal_size', mock_small_terminal)
    assert not check_terminal_size()  # Check for falsiness

    # Mock a terminal size that is large enough
    def mock_large_terminal():
        return MockTerminalSize(columns=80, lines=30)  # Large enough
    monkeypatch.setattr(os, 'get_terminal_size', mock_large_terminal)
    assert check_terminal_size()  # Check for truthiness


# Entry point for running the game or tests
if __name__ == "__main__":
    clear_terminal()
    print("Welcome to Torrent!")
    time.sleep(1)
    start_the_game()

# EOF
