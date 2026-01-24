import tkinter as tk
from tkinter import ttk, scrolledtext
from tkinter import messagebox
import random
import string
import hashlib
from datetime import datetime
import re

class WebSecurityTool:
    def __init__(self):
        # Import Week 1 + Week 2 functions
        self.password_assessor = evaluate_password # From assessor
        self.password_generator = generate_secure_password # From generator
        self.hash_function = hash_password # From generator
    
    def create_test_credentials(self):
        """Generate strong test password + hash for web form testing."""
        pw = self.password_generator()
        pw_hash = self.hash_function(pw)
        self.log_security_event(f"Generated test credential: {pw[:8]}...")
        return pw, pw_hash
    
    def validate_web_form_password(self, captured_pw):
        """Combined assessment + hashing for captured for data."""
        strength = self.password_assessor(captured_pw)
        secure_hash = self.hash_function(captured_pw)
        return {"strength": strength, "hash": secure_hash}
