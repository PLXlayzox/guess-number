import random
import tkinter as tk
from tkinter import messagebox

def play_game():
    number = random.randint(1, 10)
    
    guess = int(entry.get())

    if guess == number:
        messagebox.showinfo("Result", "You won!")
    else:
        messagebox.showinfo("Result", "You lose")

    entry.delete(0, tk.END)

window = tk.Tk()
window.title("Guess the Number Game")

window.configure(bg='black')

entry = tk.Entry(window, width=20)
entry.pack(pady=10)

play_button = tk.Button(window, text="Play", command=play_game)
play_button.pack(pady=5)

window.mainloop()
