import tkinter as tk
from tkinter import messagebox
import random
from datetime import datetime
import os

def generate_number():
    """Generates random 1-100, displays, saves to log."""
    num = random.randint(1, 100)
    display_label.config(text=f"Random Number: {num}", fg="blue", font=("Arial", 16, "bold"))

    # Log with timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} - Generated: {num}\n"

    # Append to file
    with open("random_numbers.log", "a") as f:
        f.write(log_entry)

    status_label.config(text=f"/ Saved to random_numbers.log (Total lines: {get_log_count()})")

def get_log_count():
    """Count log entries for feedback."""
    try:
        with open("random_numbers.log", "r") as f:
            return sum(1 for _ in f)
    except FileNotFoundError:
        return 0
    
# GUI Setup
root = tk.Tk()
root.title("Random Number Generator - File Logger")
root.geometry("300x250")

tk.Label(root, text="Click to generate random number (1-100)", font=("Arial", 12)).pack(pady=20)

tk.Button(root, text="GENERATE", command=generate_number, 
          bg="lightgreen", fg="darkgreen", font=("Arial", 14, "bold"), width=15, height=2).pack(pady=10)

display_label = tk.Label(root, text="No number generated yet", font=("Arial", 14))
display_label.pack(pady=10)

status_label = tk.Label(root, text="Ready to generate...", fg="gray")
status_label.pack(pady=5)

root.mainloop()
