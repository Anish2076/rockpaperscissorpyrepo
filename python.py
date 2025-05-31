import tkinter as tk
from tkinter import messagebox
import random

class StylishRPSGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors")
        self.root.geometry("500x400")
        self.root.configure(bg="#1e1e1e")  # Dark background
        self.root.resizable(False, False)

        self.choices = ["rock", "paper", "scissors"]
        self.mode = tk.StringVar(value="PvC")
        self.player1_choice = None

        self.build_ui()

    def build_ui(self):
        title = tk.Label(self.root, text="Rock, Paper, Scissors Game", font=("Helvetica", 20, "bold"), bg="#1e1e1e", fg="#00d1b2")
        title.pack(pady=10)

        mode_frame = tk.Frame(self.root, bg="#1e1e1e")
        mode_frame.pack()

        tk.Label(mode_frame, text="Game Mode:", font=("Helvetica", 12), bg="#1e1e1e", fg="white").pack(side=tk.LEFT, padx=10)
        tk.Radiobutton(mode_frame, text="Player vs Computer", variable=self.mode, value="PvC", font=("Helvetica", 11), bg="#1e1e1e", fg="white", selectcolor="#1e1e1e", command=self.reset_game).pack(side=tk.LEFT)
        tk.Radiobutton(mode_frame, text="Player vs Player", variable=self.mode, value="PvP", font=("Helvetica", 11), bg="#1e1e1e", fg="white", selectcolor="#1e1e1e", command=self.reset_game).pack(side=tk.LEFT)

        self.status_label = tk.Label(self.root, text="Player 1: Choose your move", font=("Helvetica", 13), bg="#1e1e1e", fg="#f5f5f5")
        self.status_label.pack(pady=10)

        # Choice buttons
        self.button_frame = tk.Frame(self.root, bg="#1e1e1e")
        self.button_frame.pack(pady=10)

        for choice in self.choices:
            btn = tk.Button(self.button_frame, text=choice.capitalize(), width=10, height=2,
                            font=("Helvetica", 12, "bold"), bg="#333", fg="white", activebackground="#00d1b2",
                            command=lambda c=choice: self.make_choice(c))
            btn.pack(side=tk.LEFT, padx=15)

        # Result
        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 14), bg="#1e1e1e", fg="#ffd369")
        self.result_label.pack(pady=20)

        tk.Button(self.root, text="Play Again", command=self.reset_game,
                  font=("Helvetica", 11), bg="#444", fg="white", activebackground="#00d1b2").pack()

    def reset_game(self):
        self.player1_choice = None
        self.result_label.config(text="")
        self.status_label.config(text="Player 1: Choose your move")

    def make_choice(self, choice):
        if self.mode.get() == "PvC":
            computer_choice = random.choice(self.choices)
            result = self.get_result(choice, computer_choice)
            self.result_label.config(
                text=f"You chose {choice}, Computer chose {computer_choice}.\n{result}"
            )
        else:  # PvP
            if not self.player1_choice:
                self.player1_choice = choice
                self.status_label.config(text="Player 2: Choose your move")
            else:
                player2_choice = choice
                result = self.get_result(self.player1_choice, player2_choice)
                self.result_label.config(
                    text=f"Player 1 chose {self.player1_choice}, Player 2 chose {player2_choice}.\n{result}"
                )
                self.status_label.config(text="Player 1: Choose your move")
                self.player1_choice = None

    def get_result(self, p1, p2):
        if p1 == p2:
            return "It's a Tie!"
        elif (p1 == "rock" and p2 == "scissors") or \
             (p1 == "paper" and p2 == "rock") or \
             (p1 == "scissors" and p2 == "paper"):
            return "Player 1 Wins!"
        else:
            return "Player 2 Wins!" if self.mode.get() == "PvP" else "Computer Wins!"

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = StylishRPSGame(root)
    root.mainloop()
