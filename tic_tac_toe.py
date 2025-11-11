# Author: Gogo, with assistence from ChatGPT
# Date: 11.11.2025


import tkinter as tk  # Imports the tkinter module for GUI creation and aliases it as 'tk'
import random  # Imports the random module for generating random choices
from tkinter import messagebox  # Imports the messagebox module from tkinter for pop-up alerts

# Simple Tic Tac Toe - Play vs Friend or Easy AI
# Many comments for learning and understanding
# No scharfes s used (only ss)

root = tk.Tk()  # Creates the main application window
root.title("Tic Tac Toe")  # Sets the title of the window

player = "X"  # Initializes the first player as "X"
buttons = []  # List to store the 9 button widgets (the game board)
mode = None  # Game mode: either "friend" (2 players) or "ai" (vs computer)

# Check for winner
def check_winner(sym):  # Function to check if a player with symbol 'sym' has won
    wins = [(0,1,2),(3,4,5),(6,7,8),  # All possible winning combinations (rows)
            (0,3,6),(1,4,7),(2,5,8),  # All possible winning combinations (columns)
            (0,4,8),(2,4,6)]          # All possible winning combinations (diagonals)
    for a,b,c in wins:  # Loop through each winning combination
        if buttons[a]["text"] == buttons[b]["text"] == buttons[c]["text"] == sym:
            return True  # Return True if all three positions have the same symbol
    return False  # Return False if no winning combination is found

# Check for draw
def is_draw():  # Function to check if the game is a draw
    return all(btn["text"] != "" for btn in buttons)  # Returns True if all buttons are filled

# Player move
def click(i):  # Function called when a button is clicked; i is the index of the button
    global player
    if buttons[i]["text"] == "":  # Only allow move if the button is empty
        buttons[i]["text"] = player  # Set the button text to the current player's symbol
        if check_winner(player):  # Check if the current player has won
            messagebox.showinfo("Game Over", f"Player {player} wins!")  # Show win message
            reset()  # Reset the game board
            return
        elif is_draw():  # Check for draw
            messagebox.showinfo("Game Over", "Draw!")  # Show draw message
            reset()
            return
        if mode == "friend":  # If playing with a friend, switch player
            player = "O" if player == "X" else "X"  # Toggle between X and O
        else:
            ai_move()  # If playing vs AI, let AI make a move

# Mid AI (random)
def ai_move():  # Function for AI's move
    free = [i for i in range(9) if buttons[i]["text"] == ""]  # List of empty positions
    if not free:  # If no free positions, return
        return

    # 1. Try to win
    for i in free:
        buttons[i]["text"] = "O"  # Temporarily place "O"
        if check_winner("O"):  # Check if this move wins
            move = i
            buttons[i]["text"] = ""  # Undo move
            break
        buttons[i]["text"] = ""  # Undo move if not winning
    else:
        # 2. Try to block player
        move = None
        for i in free:
            buttons[i]["text"] = "X"  # Temporarily place "X"
            if check_winner("X"):  # Check if player would win
                move = i
                buttons[i]["text"] = ""  # Undo move
                break
            buttons[i]["text"] = ""  # Undo move if not blocking
        # 3. If nothing to block or win, random
        if move is None:
            move = random.choice(free)  # Choose a random free position

    buttons[move]["text"] = "O"  # Make the actual move
    if check_winner("O"):  # Check if AI wins
        messagebox.showinfo("Game Over", "AI wins!")  # Show win message
        reset()
    elif is_draw():  # Check for draw
        messagebox.showinfo("Game Over", "Draw!")  # Show draw message
        reset()

# Reset the board
def reset():  # Function to reset the game board
    global player
    player = "X"  # Reset player to "X"
    for b in buttons:
        b["text"] = ""  # Clear all button texts

# Create the board
def start_game(selected_mode):  # Function to start the game with selected mode
    global mode
    mode = selected_mode  # Set the game mode
    mode_frame.pack_forget()  # Hide the mode selection menu
    board_frame.pack()  # Show the game board
    for i in range(9):  # Create 9 buttons for the board
        btn = tk.Button(board_frame, text="", font=("Arial", 20), width=5, height=2,
                        command=lambda i=i: click(i))  # Each button calls click(i)
        btn.grid(row=i//3, column=i%3)  # Arrange buttons in 3x3 grid
        buttons.append(btn)  # Add button to the list

# Menu to choose mode
mode_frame = tk.Frame(root)  # Frame for the mode selection menu
tk.Label(mode_frame, text="Choose Game Mode", font=("Arial", 14)).pack(pady=10)  # Title label
tk.Button(mode_frame, text="Play vs Friend", width=20, command=lambda: start_game("friend")).pack(pady=5)  # Button for friend mode
tk.Button(mode_frame, text="Play vs AI (Easy)", width=20, command=lambda: start_game("ai")).pack(pady=5)  # Button for AI mode
mode_frame.pack()  # Show the mode selection menu

board_frame = tk.Frame(root)  # Frame for the game board (initially hidden)
root.mainloop()  # Start the tkinter event loop (keeps the window open)