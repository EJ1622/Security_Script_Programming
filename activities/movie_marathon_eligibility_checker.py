import tkinter as tk
from datetime import datetime

def check_eligibility():
    """
    Validates DOB input and checks if user is 18+.
    Updates result label with eligibility message.
    """
    dob_str = entry.get() # Get DOB from text entry
    try:
        birth_date = datetime.strptime(dob_str, '%Y-%m-%d') # Parse input as date
        today = datetime.now() # Current date
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day)) # Calculate age
        if age >= 18:
            result_label.config(text="Eligible for Movie Marathon!", fg="green")
        else:
            result_label.config(text="Not Eligible (under 18).", fg="red")
    except ValueError:
        result_label.config(text="Invalid DOB. Use YYYY-MM-DD.", fg="orange")

# Create main window
root = tk.Tk()
root.title("Movie Marathon Eligility Checker")
root.geometry=("350x200")

# Instructions label
tk.Label(root, text="Enter DOB (YYYY-MM-DD):", font=("Arial", 12)).pack(pady=10)

# Input field
entry = tk.Entry(root, font=("Arial", 12), width=15)
entry.pack(pady=5)
entry.focus() # Auto-focus on input

# Check button
tk.Button(root, text="Check Eligibility", command=check_eligibility, bg="lightblue", font=("Arial", 12)).pack(pady=15)


# Result display
result_label = tk.Label(root, text="Enter DOB and click Check", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop() # Start GUI even loop