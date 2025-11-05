# insecure_code.py
import hashlib

# Security issue: Hardcoded password
PASSWORD = "admin123"

# Security issue: Weak hash
def hash_password(pwd):
    return hashlib.md5(pwd.encode()).hexdigest()

# Security issue: Using eval
def calculate(expression):
    return eval(expression)
