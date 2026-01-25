"""
MO-IT142 Week 3 Homework: GUI Web Form Input Validator & Sanitizer
Validates + sanitizes 4 web form fields per exact requirements
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import re
import html

class WebFormValidator:
    def __init__(self):
        # SQLi/XSS dangerous patterns
        self.dangerous_patterns = [
            r'<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>',
            r'<img\b[^<]*(?:(?!<\/img>)<[^<]*)*<\/img>',
            r'(?i)(union|select|drop|insert|delete|update).*?(from|where)',
            r'javascript:',
            r'on\w+\s*='
        ]
    
    def validate_full_name(self, name):
        """No numbers, only letters/spaces/hyphens/apostrophes, min 2 chars."""
        if len(name) < 2:
            return False, "Must be at least 2 characters long"
        if re.search(r'\d', name):
            return False, "Must not contain numbers"
        if not re.fullmatch(r"^[a-zA-Z\s'-]+$", name):
            return False, "Only letters, spaces, hyphens, apostrophes allowed"
        return True, "Valid"
    
    def validate_email(self, email):
        """Contains @, domain (.com/.org), no spaces, no special start."""
        if not re.search(r'@', email):
            return False, "Must contain @ symbol"
        if re.search(r'\s', email):
            return False, "Cannot contain spaces"
        if re.search(r'^[^a-zA-Z0-9]', email):
            return False, "Cannot start with special character"
        if not re.search(r'\.(com|org|edu|gov|net|ph|)$', email, re.IGNORECASE):
            return False, "Must have valid domain (.com, .org, etc.)"
        return True, "Valid"
    
    def validate_username(self, username):
        """Letters/numbers/underscores only, 4-16 chars, no number start."""
        if not 4 <= len(username) <= 16:
            return False, f"Must be 4-16 characters (got {len(username)})"
        if re.match(r'^\d', username):
            return False, "Cannot begin with a number"
        if not re.fullmatch(r'^[a-zA-Z0-9_]+$', username):
            return False, "Only letters, numbers, underscores allowed"
        return True, "Valid"
    
    def validate_message(self, message):
        """Not empty, max 250 chars, no dangerous patterns."""
        if len(message) == 0:
            return False, "Cannot be empty"
        if len(message) > 250:
            return False, f"Cannot exceed 250 characters (got {len(message)})"
        for pattern in self.dangerous_patterns:
            if re.search(pattern, message):
                return False, "Contains prohibited patterns (script/SQL)"
        return True, "Valid"
    
    def sanitize_field(self, field, value, field_type):
        """Sanitize based on field type."""
        # Remove/escape dangerous patterns
        cleaned = value
        for pattern in self.dangerous_patterns:
            cleaned = re.sub(pattern, '[SANITIZED]', cleaned, flags=re.IGNORECASE)
        cleaned = html.escape(cleaned)

        # Field-specific cleaning
        if field_type == 'full_name':
            cleaned = re.sub(r'[^a-zA-Z\s\'-]', '', cleaned)
        elif field_type == 'username':
            cleaned = re.sub(r'[^a-zA-Z0-9_]', '', cleaned)
        
        sanitized = len(cleaned) != len(value)
        return cleaned, sanitized
    
def validate_form():
    """Main validation + sanitization workflow."""
    form_data = {
        'full_name': name_entry.get().strip(),
        'email': email_entry.get().strip(),
        'username': username_entry.get().strip(),
        'message': message_text.get(1.0, tk.END).strip()
    }

    validator = WebFormValidator()
    results = []
    sanitized_data = {}

    # Validate each field
    for field, value in form_data.items():
        if field == 'full_name':
            valid, msg = validator.validate_full_name(value)
        elif field == 'email':
            valid, msg = validator.validate_email(value)
        elif field == 'username':
            valid, msg = validator.validate_username(value)
        else: # message
            valid, msg = validator.validate_message(value)
        
        results.append(f"{field.replace('_', ' ').title()}: {'Valid' if valid else 'Invalid'} - {msg}")

        # Sanitize
        cleaned, was_sanitized = validator.sanitize_field(field, value, field)
        sanitized_data[field] = cleaned
        if was_sanitized:
            results.append(f" → Sanitized: {cleaned[:50]}...")
    
    # Display results
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "VALIDATION RESULTS:\n" + "="*50 + "\n")
    for result in results:
        result_text.insert(tk.END, f". {result}\n")
    
    result_text.insert(tk.END, f"\nSANITIZED OUTPUT:\n{'='*50}\n")
    for field, cleaned in sanitized_data.items():
        result_text.insert(tk.END, f"{field.replace('_', ' ').title()}: {cleaned}\n")
    
    result_text.insert(tk.END, f"\n✓ Process Complete.")

# GUI Setup
root = tk.Tk()
root.title("Web Form Input Validator & Sanitizer")
root.geometry("700x650")

# Header
tk.Label(root, text="🔐 Web Form Security Validator",
         font=("Arial", 18, "bold")).pack(pady=15)

# Form inputs
fields_frame = ttk.LabelFrame(root, text="Simulate Web Form", padding=15)
fields_frame.pack(pady=10, padx=20, fill="x")

ttk.Label(fields_frame, text="Full Name:").grid(row=0, column=0, sticky="w", pady=5)
name_entry = ttk.Entry(fields_frame, width=40)
name_entry.grid(row=0, column=1, pady=5, padx=(10,0))

ttk.Label(fields_frame, text="Email:").grid(row=1, column=0, sticky="w", pady=5)
email_entry = ttk.Entry(fields_frame, width=40)
email_entry.grid(row=1, column=1, pady=5, padx=(10,0))

ttk.Label(fields_frame, text="Username:").grid(row=2, column=0, sticky="w", pady=5)
username_entry = ttk.Entry(fields_frame, width=40)
username_entry.grid(row=2, column=1, pady=5, padx=(10,0))

ttk.Label(fields_frame, text="Message:").grid(row=3, column=0, sticky="nw", pady=5)
message_text = tk.Text(fields_frame, height=4, width=38)
message_text.grid(row=3, column=1, pady=5, padx=(10,0))

# Validate button
ttk.Button(root, text="Validate & Sanitize Form",
           command=validate_form, style="Accent.TButton").pack(pady=20)

# Results
ttk.Label(root, text="Results:", font=("Arial", 12, "bold")).pack(pady=(20,5))
result_text = scrolledtext.ScrolledText(root, height=18, width=85, font=("Consolas", 10))
result_text.pack(pady=10, padx=20, fill="both", expand=True)

root.mainloop()
