# Example secure coding practices

# 1. Input Validation
def validate_input(user_input):
    if not isinstance(user_input, str):
        raise TypeError("Input must be a string")
    if len(user_input) > 100:
        raise ValueError("Input too long")
    return user_input.strip()

# 2. Secure Password Storage
import hashlib
import os

def hash_password(password):
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        100000  # Number of iterations
    )
    return salt + key

# 3. SQL Injection Prevention
def safe_sql_query(user_input):
    # Use parameterized queries instead of string concatenation
    query = "SELECT * FROM users WHERE username = ?"
    params = (validate_input(user_input),)
    # Execute with params...

# 4. File Path Validation
# This section imports the os.path module which provides functions for working with file paths
# os.path is used to safely handle file paths across different operating systems
# It helps prevent directory traversal attacks by normalizing and validating paths
# The module will be used by safe_file_access() below to ensure secure file operations
import os.path

def safe_file_access(filename):
    # Normalize path and check if it's within allowed directory
    safe_path = os.path.normpath(filename)
    if not safe_path.startswith("/allowed/path"):
        raise ValueError("Access denied")
    return safe_path

# 5. Secure Random Numbers
import secrets

def generate_token(length=32):
    """Generate a secure random token for streaming chat sessions.
    Args:
        length (int): Length of token in bytes. Defaults to 32 bytes (64 hex chars).
    Returns:
        str: Secure random hex token string
    """
    return secrets.token_hex(length)

# Example usage
try:
    user_input = validate_input("   test input   ")
    secure_token = generate_token()
    hashed_pass = hash_password("mypassword123")
except (ValueError, TypeError) as e:
    print(f"Security error: {e}")
testtesttest
