import random
import string

def generate_random_password(length=10):
    """Generate a random password with the given length."""
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def generate_custom_password():
    """Generate a custom password based on user specifications."""
    length = int(input("Enter the desired password length: "))
    use_lowercase = input("Use lowercase letters? (y/n): ").lower() == "y"
    use_uppercase = input("Use uppercase letters? (y/n): ").lower() == "y"
    use_digits = input("Use digits? (y/n): ").lower() == "y"
    use_symbols = input("Use symbols? (y/n): ").lower() == "y"
    
    chars = ""
    if use_lowercase:
        chars += string.ascii_lowercase
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation
        
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

# Prompt the user to generate either a random or custom password
print("Select an option to generate a password:")
print("1. Generate random 10-digit password")
print("2. Generate custom password")
option = int(input("Enter an option number (1 or 2): "))

if option == 1:
    password = generate_random_password(length=10)
    print("Your random 10-digit password is:", password)
elif option == 2:
    password = generate_custom_password()
    print("Your custom password is:", password)
else:
    print("Invalid option. Please select 1 or 2.")

