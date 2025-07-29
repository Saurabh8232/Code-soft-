import random
import string

def generate_password():
    print("=== Password Generator ===")

    try:
        length = int(input("Enter password length (minimum 4): "))
        if length < 4:
            print("Password length must be at least 4.")
            return
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    char_set = ""
    if use_upper:
        char_set += string.ascii_uppercase
    if use_lower:
        char_set += string.ascii_lowercase
    if use_digits:
        char_set += string.digits
    if use_symbols:
        char_set += string.punctuation

    if not char_set:
        print("You must select at least one character type!")
        return

    # Guarantee at least one of each selected type
    guaranteed = []
    if use_upper:
        guaranteed.append(random.choice(string.ascii_uppercase))
    if use_lower:
        guaranteed.append(random.choice(string.ascii_lowercase))
    if use_digits:
        guaranteed.append(random.choice(string.digits))
    if use_symbols:
        guaranteed.append(random.choice(string.punctuation))

    remaining = [random.choice(char_set) for _ in range(length - len(guaranteed))]
    password_list = guaranteed + remaining
    random.shuffle(password_list)
    password = ''.join(password_list)

    print(f"\nGenerated Password: {password}")

# Run the program
generate_password()
