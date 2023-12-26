import string
import secrets

def generate_password(length=12, include_special=True, include_numbers=True, include_mixed_case=True):
    """
    Generate a random, secure password.

    Parameters:
    - length: Length of the password (default is 12).
    - include_special: Include special characters (default is True).
    - include_numbers: Include numbers (default is True).
    - include_mixed_case: Include mixed-case letters (default is True).

    Returns:
    A randomly generated password.
    """
    characters = string.ascii_letters
    if include_special:
        characters += string.punctuation
    if include_numbers:
        characters += string.digits

    if not include_mixed_case:
        characters = characters.lower()

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password
