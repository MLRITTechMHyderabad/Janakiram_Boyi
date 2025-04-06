import re

def is_strong_password(password):
    # Rule 1: At least 8 characters
    if len(password) < 8:
        return False
    # Rule 2: At least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False
    # Rule 3: At least one lowercase letter
    if not re.search(r'[a-z]', password):
        return False
    # Rule 4: At least one digit
    if not re.search(r'\d', password):
        return False
    # Rule 5: At least one special character
    if not re.search(r'[@$!%*?&#]', password):
        return False
    return True

# Test cases
passwords = ["WeakPass", "Str0ng@Pass", "NoSpecial1", "short!1", "Secure#123"]

# Check and print result for each password
for pwd in passwords:
    result = "Valid" if is_strong_password(pwd) else "Invalid"
    print(f"{pwd} -> {result}")
