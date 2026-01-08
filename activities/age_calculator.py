import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Function to calculate age from birthday input
def calculate_age():
    # Get birthday string from user input field
    birth_str = entry.get()
    try:
        # Parse birthday string into datetime objects using YYYY-MM-DD format
        birth_date = datetime.strptime(birth_str, '%Y-%m-%d')
        #Get current date for age calculation
        today = datetime.now()
        #Calculate age: subtract years, adjust if birthday hasn't occurred this year
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        
        #Update result label with calculated age
        result_label.config(text=f"Your age is {age} years")
    except ValueError:

        #Handle invalid date format input
        result_label.config(text="Invalid date format. Use YYYY-MM-DD")

# Create main application window
app = tk.Tk()
# Set window title
app.title("Age Calculator")
#Set window size (width x height)
app.geometry("300x150")

#Create and pack instruction label
tk.Label(app, text="Enter birthday (YYYY-MM-DD):").pack(pady=10)
#Create input entry field for birthday
entry = tk.Entry(app)
entry.pack(pady=5)
#Create calculate button linked to calculate_age function
tk.Button(app, text="Calculate Age", command=calculate_age).pack(pady=10)
#Create result label (initially empty)
result_label = tk.Label(app, text="")
result_label.pack()

#Start the GUI event loop
app.mainloop()