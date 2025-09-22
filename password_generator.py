import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters."

    # Combine all character types
    characters = string.ascii_letters + string.digits + string.punctuation

    # Randomly choose characters from the combined list
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("=== Password Generator ===")
    
    try:
        length = int(input("Enter desired password length: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    password = generate_password(length)
    print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main()
