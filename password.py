import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 characters.")
        return None

    # Define the character sets to use
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Ensure the password includes at least one of each character type
    password_chars = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special),
    ]

    # Fill the remaining length with random choices from all character sets
    all_chars = lower + upper + digits + special
    password_chars += random.choices(all_chars, k=length - 4)

    # Shuffle the resulting password characters
    random.shuffle(password_chars)

    # Join the list into a string
    return ''.join(password_chars)

def main():
    print("Password Generator")
    try:
        length = int(input("Enter the desired password length (minimum 4): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    password = generate_password(length)
    if password:
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
