import re

from django.contrib.staticfiles import finders

# Load common passwords list
COMMON_PASSWORDS_FILE = finders.find('10-million-password-list-top-1000.txt')
with open(COMMON_PASSWORDS_FILE, 'r') as file:
    COMMON_PASSWORDS = set(line.strip() for line in file)


def validate_password(password: str) -> bool:
    """
    Validate a password based on the updated requirements.

    Args:
        password (str): The password to validate.

    Returns:
        bool: True if the password is valid, False otherwise.
    """

    # Minimum length requirement of 10 characters
    min_length = 10
    if len(password) < min_length:
        return False

    # Check for commonly used passwords
    if password in COMMON_PASSWORDS:
        return False

    # Check for allowed characters (printing ASCII characters and spaces)
    if not re.match(r'^[\x20-\x7E]+$', password):
        return False

    return True
