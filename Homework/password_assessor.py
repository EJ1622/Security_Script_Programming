import tkinter as tk
from tkinter import messagebox
import re

# Common passwords and dictionary words lists
COMMON_PASSWORDS = {"password", "123456", "qwerty", "admin", "letmein", "welcome"}
DICT_WORDS = {"apple", "computer", "dragon", "monkey"}

def evaluate_password(pw):
    """
    Evaluates password strength based on 7 criteria.
    Returns dict with met criteria count and details.
    """
    criteria_met = 0
    details = []
    
    # 1. Min. length 12
    if len(pw) >= 12:
        criteria_met += 1
        details.append("/ Min length (12+)")
    else:
        details.append("X Min length (<12)")

    # 2. Uppercase
    if re.search(r'[A-Z]', pw):
        criteria_met += 1
        details.append("/ Uppercase letter")
    else:
        details.append("X Uppercase letter")

    # 3. Lowercase
    if re.search(r'[a-z]', pw):
        criteria_met += 1
        details.append("/ Lowercase letter")
    else:
        details.append("X Lowercase letter")

    # 4. Numbers
    if re.search(r'\d', pw):
        criteria_met += 1
        details.append("/ Number")
    else:
        details.append("X Number")

    # 5. Special chars
    if re.search(r'[!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>/?]', pw):
        criteria_met += 1
        details.append("/ Special character")
    else:
        details.append("X Special character")

    # 6. Common passwords
    if pw.lower() in COMMON_PASSWORDS:
        details.insert(0, "X Common password!")
        return {"met": 0, "details": details} # Auto weak
    else:
        criteria_met += 1
        details.append("/ Not common password")

    # 7. Dictionary words
    has_dict_word = any(word in pw.lower() for word in DICT_WORDS)
    if not has_dict_word:
        criteria_met += 1
        details.append("/ No dictionary word")
    else:
        details.append("X Contains dictionary word")

    return {"met": criteria_met, "details": details}

def check_password():
    """ Handles button click: evaluates and displays strength. """
    pw = entry.get()
    if not pw:
        messagebox.showwarning("Input required", "Please enter a password before checking.")
        return
    
    result = evaluate_password(pw)

    # Determine rating
    met = result["met"]
    if met < 4 or "X Common password!" in result["details"]:
        rating = "Weak"
    elif met < 7:
        rating = "Moderate"
    else:
        rating = "Strong"

    # Update display
    details_text.delete(1.0, tk.END)
    details_text.insert(tk.END, f"{rating} Password\n\n" + "\n".join(result["details"]))

# GUI setup
root = tk.Tk()
root.title("Password Strength Assessor")
root.geometry("400x500")
root.configure(bg="lightgray")

# Title
tk.Label(root, text="Password Strength Checker", font=("Arial", 16, "bold"), bg="lightgray").pack(pady=10)

# Password Input
tk.Label(root, text="Enter Password:", font=("Arial", 12), bg="lightgray").pack()
entry = tk.Entry(root, font=("Arial", 12), width=30, show="*", justify="center")
entry.pack(pady=5)
entry.focus()

# Check button
tk.Button(root, text="Assess Strength", command=check_password, bg="lightblue", font=("Arial", 12), width=20).pack(pady=20)

# Results display
tk.Label(root, text="Results:", font=("Arial", 12, "bold"), bg="lightgray").pack(anchor="w", padx=20)
details_text = tk.Text(root, height=15, width=50, font=("Courier", 10), bg="white")
details_text.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

root.mainloop()