# Simple Password Strength Checker
# Author: Shannel Segwabe

import re

def check_password(password):
    if len(password) < 8:
        return "Weak: Too short"
    if not re.search(r"[A-Z]", password):
        return "Weak: Add uppercase letter"
    if not re.search(r"[a-z]", password):
        return "Weak: Add lowercase letter"
    if not re.search(r"[0-9]", password):
        return "Weak: Add number"
    if not re.search(r"[!@#$%^&*()_+]", password):
        return "Weak: Add special character"
    return "Strong Password"

if __name__ == "__main__":
    password = input("Enter password to check: ")
    print(check_password(password))
