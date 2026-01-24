"""
MO-IT142 Week 3 Practice Activity 2: MMDC Web Page Data Extractor
Fetches https://www.mmdc.mcl.edu.ph/college-programs/
Extracts ALL headings (h1-h6) + hyperlinks (a href)
"""

import tkinter as tk
from tkinter import scrolledtext, messagebox
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def extract_mmdc_data():
    """Fetch MMDC page → Extract headings + links."""
    try:
        url = "https://www.mmdc.mcl.edu.ph/college-programs/"
        status_label.config(text="Fetching MMDC page...", fg="orange")
        root.update()

        # HTTP GET request
        headers = {'User-Agent': 'WebScanner/1.0'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        # Parse HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract ALL headings h1-h6
        heading_tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
        headings = []
        for tag in heading_tags:
            for heading in soup.find_all(tag):
                headings.append(f"{tag.upper()}: {heading.get_text(strip=True)}")

        # Extract ALL hyperlinks
        links = []
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            text = a_tag.get_text(strip=True)[:50] # Truncate long text
            full_url = urljoin(url, href) # Handle relative URLs
            links.append(f"🔗 {full_url} → {text}")

        # Display results
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"MMDC Technology Page Analysis\n{'='*60}\n\n")

        result_text.insert(tk.END, f"📋 HEADINGS FOUND ({len(headings)}):\n")
        for i, heading in enumerate(headings[:20], 1): # First 20
            result_text.insert(tk.END, f"  {i}. {heading}\n")

        result_text.insert(tk.END, f"\n🔗 HYPERLINKS FOUND ({len(links)}):\n")
        for i, link in enumerate(links[:30], 1): # First 30
            result_text.insert(tk.END, f"  {i}. {link}\n")

        status_label.config(text=f"✓ Success! {len(headings)} headings + {len(links)} links", fg="green")

    except requests.RequestException as e:
        messagebox.showerror("Network Error", f"Failed to fetch MMDC page:\n{str(e)}")
        status_label.config(text="✗ Network error", fg="red")
    except Exception as e:
        messagebox.showerror("Parse Error", f"Parsing failed:\n{str(e)}")
        status_label.config(text="✗ Parse error", fg="red")

# GUI Setup
root = tk.Tk()
root.title("MMDC Web Page Data Extractor")
root.geometry("900x700")

# Header
tk.Label(root, text="🌐 MMDC Technology Page Parser",
         font=("Arial", 18, "bold")).pack(pady=20)

# Target URL display
url_frame = tk.Frame(root)
url_frame.pack(pady=10)
tk.Label(url_frame, text="Target:", font=("Arial", 11)).pack(side="left")
tk.Label(url_frame, text="https://www.mmdc.mcl.edu.ph/college-programs/",
         font=("Courier", 10), fg="blue").pack(side="left", padx=5)

# Extract button
extract_btn = tk.Button(root, text="🔍 Extract Headings & Links",
                        command=extract_mmdc_data,
                        bg="#2196F3", fg="white", font=("Arial", 14, "bold"),
                        width=25, height=2, pady=5)
extract_btn.pack(pady=20)

# Results display
tk.Label(root, text="Extracted Data:", font=("Arial", 14, "bold")).pack(pady=(30,10))
result_text = scrolledtext.ScrolledText(root, height=25, width=100,
                                        font=("Consoles", 10))
result_text.pack(pady=10, padx=10, fill="both", expand=True)

status_label = tk.Label(root, text="Click Extract to analyze MMDC page...",
                        font=("Arial", 11))
status_label.pack(pady=10)

root.mainloop()
