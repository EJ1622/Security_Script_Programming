"""
MO-IT142 Week 3 Practice Activity 1: GUI-Based Email Validator
Validates: 1 @ symbol, chars before/after, valid domain structure
"""

import tkinter as tk
from tkinter import messagebox
import re

def validate_email(email):
    """Strict email validation meeting all 3 criteria."""
    # Regex: local-part@domain.tld (1+ chars before/after @, valid domain)
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if not re.fullmatch(pattern, email):
        return False, "❌ Invalid format"
    
    # Double-check single @ symbol
    at_count = email.count('@')
    if at_count != 1:
        return False, "❌ Exactly 1 @ required"
    
    return True, "✅ Valid email address"

def check_email():
    """GUI validation handler."""
    email = email_entry.get().strip()

    if not email:
        result_label.config(text="Enter an email first!", fg="orange")
        return
    
    is_valid, message = validate_email(email)
    result_label.config(text=message, fg="green" if is_valid else "red")

    # Security context feedback
    if is_valid:
        status_label.config(text="✓ Safe for web form submission", fg="green")

# GUI Setup
root = tk.Tk()
root.title("Email Address Validator")
root.geometry("450x300")
root.configure(bg="#f5f5f5")

# Header
tk.Label(root, text="📧 Email Validator", font=("Arial", 18, "bold"),
         bg="#f5f5f5").pack(pady=20)

# Input
tk.Label(root, text="Enter email to validate:", font=("Arial", 12),
         bg="#f5f5f5").pack()
email_entry = tk.Entry(root, font=("Arial", 14), width=35, justify="center")
email_entry.pack(pady=10)

# Validate Button
validate_btn = tk.Button(root, text="Validate Email", command=check_email,
                         bg="#2196F3", fg="white", font=("Arial", 12, "bold"),
                         width=15, height=2)
validate_btn.pack(pady=20)

# Results
result_label = tk.Label(root, text="Enter email to validate...",
                        font=("Arial", 14, "bold"), bg="#f5f5f5")
result_label.pack(pady=10)

status_label = tk.Label(root, text="Ready to validate...",
                        font=("Arial", 11), bg="#f5f5f5")
status_label.pack()

root.mainloop()
