import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
import re
import os

def analyze_log():
    """
    Loads log file, filters failed logins, extracts timestamp/user/IP, displays results.
    """
    file_path = filedialog.askopenfilename(title="Select Log File", filetypes=[("Log files", "*.log")])
    if not file_path:
        return
    
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()

        failed_attempts = []
        pattern = r'(\w+ \d+ \d+:\d+:\d+) .*?sshd\[\d+\]: Failed password for (?:invalid user )?(\w+) from (\d+\.\d+\.\d+\.\d+)'

        for line in lines:
            match = re.search(pattern, line)
            if match:
                timestamp, user, ip = match.groups()
                failed_attempts.append(f"Timestamp: {timestamp}, User: {user}, IP: {ip}")

            result_text.delete(1.0, tk.END)
            if failed_attempts:
                result_text.insert(tk.END, "Failed Login Attempts:\n\n" + "\n".join(failed_attempts))
            else:
                result_text.insert(tk.END, "No failed attempts found.")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to analyze log: {str(e)}")

# GUI Setup
root = tk.Tk()
root.title("Log File Filter and Extractor")
root.geometry("500x400")

tk.Button(root, text="Load and Analyze Log File", command=analyze_log, bg="lightgreen", font=("Arial", 12)).pack(pady=20)

result_text = scrolledtext.ScrolledText(root, width=60, height=20, font=("Courier", 10))
result_text.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

root.mainloop()