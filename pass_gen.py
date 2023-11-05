import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    characters = ""
    
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        print("Please select at least one character set (letters, numbers, or symbols).")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_valid_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input.lower() == "yes":
            return True
        elif user_input.lower() == "no":
            return False
        else:
            print("Please enter 'yes' or 'no'.")

def main():
    print("Command-line Password Generator")
    
    while True:
        try:
            length = int(input("Enter the password length: "))
            if length <= 0:
                print("Password length must be a positive number. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for password length.")
    
    use_letters = get_valid_input("Include letters (yes/no): ")
    use_numbers = get_valid_input("Include numbers (yes/no): ")
    use_symbols = get_valid_input("Include symbols (yes/no): ")

    password = generate_password(length, use_letters, use_numbers, use_symbols)
    
    if password:
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
