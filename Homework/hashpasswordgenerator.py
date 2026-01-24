"""
MO-IT142 Week 2 Homework: Random Hash Password Generator
Generates secure passwords (8-16 chars, mixed case/digits/special)
SHA-256 hashes them, saves timestamped entries to passwords.txt
"""

import tkinter as tk
from tkinter import messagebox
import random
import string
import hashlib
from datetime import datetime

def generate_secure_password():
    """Generates random 8-16 char password meeting all criteria."""
    length = random.randint(8, 16)
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + "!@#$%^&*()_+=[]{};:,.<>?"

    # Ensure at least one of each required type
    password_list = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice("!@#$%^&*()_+=[]{};:,.<>?")
    ]

    # Fill remaining length randomly
    password_list.extend(random.choice(chars) for _ in range(length - 4))
    random.shuffle(password_list) # Randomize order

    return ''.join(password_list)

def hash_password(password):
    """Returns SHA-256 hash of password."""
    return hashlib.sha256(password.encode()).hexdigest()

def generate_and_save():
    """Main function: generate -> hash -> save to passwords.txt."""
    try:
        password = generate_secure_password()
        pw_hash = hash_password(password)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Format entry exactly as specified
        entry = f"Timestamp: {timestamp}\nPassword: {password}\nHash: {pw_hash}\n\n"

        # Append to file ('a' mode preserves history)
        with open("passwords.txt", "a") as f:
            f.write(entry)
        
        # Update GUI displays
        password_label.config(text=f"Password: {password}")
        hash_label.config(text=f"SHA-256: {pw_hash[:32]}...")
        status_label.config(text=f"✓ Saved! File: passwords.txt ({get_entry_count()} entries)", fg="green")
    
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save: {str(e)}")

def get_entry_count():
    """Count password entries in file."""
    try:
        with open("passwords.txt", "r") as f:
            content = f.read()
            return content.count("Timestamp:")
    except FileNotFoundError:
        return 0

# === GUI SETUP ===
root = tk.Tk()
root.title("Random Hash Password Generator")
root.geometry("500x400")
root.configure(bg="#f0f0f0")

# Header
tk.Label(root, text="🔐 Secure Password Generator",
         font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=20)

# Generate button
generate_btn = tk.Button(root, text="Generate & Save Password",
                         command=generate_and_save, bg="#4CAF50", fg="white",
                         font=("Arial", 14, "bold"), width=22, height=2)
generate_btn.pack(pady=10)

# Results display
tk.Label(root, text="Latest Generation:", font=("Arial", 12, "bold"),
         bg="#f0f0f0").pack(pady=(20,5))

password_label = tk.Label(root, text="No password generated",
                          font=("Courier", 11), bg="white", relief="solid", padx=10)
password_label.pack(pady=5, fill="x")

hash_label = tk.Label(root, text="No hash generated",
                      font=("Courier", 10), bg="white", relief="solid", padx=10)
hash_label.pack(pady=5, fill="x")

status_label = tk.Label(root, text="Ready to generate...",
                        font=("Arial", 11), bg="#f0f0f0")
status_label.pack(pady=10)

root.mainloop()
