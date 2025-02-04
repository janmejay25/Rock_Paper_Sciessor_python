
import tkinter as tk
from tkinter import messagebox

# Variables to store player choices
player1_choice = None
player2_choice = None

def play_game():
    global player1_choice, player2_choice
    result = ""

    if player1_choice == player2_choice:
        result = "It's a tie!"
    elif (player1_choice == "Rock" and player2_choice == "Scissors") or \
         (player1_choice == "Paper" and player2_choice == "Rock") or \
         (player1_choice == "Scissors" and player2_choice == "Paper"):
        result = "Player 1 Wins!"
    else:
        result = "Player 2 Wins!"
    
    # Show the result
    messagebox.showinfo("Result", f"Player 1 chose: {player1_choice}\n"
                                  f"Player 2 chose: {player2_choice}\n"
                                  f"{result}")
    
    # Reset choices for next round
    reset_game()

def reset_game():
    """Reset the game to allow a new round."""
    global player1_choice, player2_choice
    player1_choice = None
    player2_choice = None
    update_status()
    show_player2_buttons(False)  # Hide Player 2 buttons

def update_status():
    """Update the status label."""
    if player1_choice and not player2_choice:
        status_text.set("Player 2: Choose an option!")
    elif not player1_choice:
        status_text.set("Player 1: Choose an option!")
    else:
        status_text.set("Waiting for both players...")

def set_choice(player, choice):
    """Set the choice for a player and proceed."""
    global player1_choice, player2_choice

    if player == 1:
        player1_choice = choice
        update_status()
        show_player2_buttons(True)  # Show Player 2 buttons
    elif player == 2:
        player2_choice = choice
        play_game()

def show_player2_buttons(show):
    """Show or hide Player 2's buttons."""
    if show:
        player2_label.pack(pady=5)
        for btn in player2_buttons:
            btn.pack(pady=2)
    else:
        player2_label.pack_forget()
        for btn in player2_buttons:
            btn.pack_forget()

# Tkinter setup
root = tk.Tk()
root.title("Rock Paper Scissors - 2 Player")

# Status label to show progress
status_text = tk.StringVar()
status_text.set("Player 1: Choose an option!")
tk.Label(root, textvariable=status_text, font=("Arial", 12)).pack(pady=10)

# Player 1 choices
tk.Label(root, text="Player 1, choose an option:", font=("Arial", 14)).pack(pady=5)
for choice in ["Rock", "Paper", "Scissors"]:
    tk.Button(root, text=choice, font=("Arial", 12), 
              command=lambda c=choice: set_choice(1, c)).pack(pady=2)

# Player 2 buttons (initially hidden)
player2_label = tk.Label(root, text="Player 2, choose an option:", font=("Arial", 14))
player2_buttons = [tk.Button(root, text=choice, font=("Arial", 12), 
                             command=lambda c=choice: set_choice(2, c)) 
                   for choice in ["Rock", "Paper", "Scissors"]]

# Initially hide Player 2 buttons
show_player2_buttons(False)

root.mainloop()
