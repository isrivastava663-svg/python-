# ================================
#   Password Generator - Python
# ================================

import random
import string

def generate_password(length, use_upper, use_digits, use_symbols):
    characters = string.ascii_lowercase  # always include lowercase

    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def check_strength(password):
    score = 0
    if len(password) >= 12:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score == 4:
        return "💪 Strong"
    elif score == 3:
        return "👍 Medium"
    else:
        return "⚠️  Weak"

def get_yes_no(prompt):
    while True:
        ans = input(prompt).strip().lower()
        if ans in ['y', 'yes']:
            return True
        elif ans in ['n', 'no']:
            return False
        else:
            print("  Please enter Y or N.")

def main():
    print("=" * 40)
    print("     🔐 PASSWORD GENERATOR")
    print("=" * 40)

    while True:
        print()
        # Get password length
        while True:
            try:
                length = int(input("Enter password length (6-64): "))
                if 6 <= length <= 64:
                    break
                print("  ⚠️  Please enter a number between 6 and 64.")
            except ValueError:
                print("  ⚠️  Please enter a valid number.")

        # Options
        print()
        use_upper   = get_yes_no("Include UPPERCASE letters? (Y/N): ")
        use_digits  = get_yes_no("Include DIGITS (0-9)?         (Y/N): ")
        use_symbols = get_yes_no("Include SYMBOLS (!@#...)?     (Y/N): ")

        # Generate
        print()
        passwords = [generate_password(length, use_upper, use_digits, use_symbols) for _ in range(5)]

        print("\n🔑 Generated Passwords:")
        print("-" * 40)
        for i, pwd in enumerate(passwords, 1):
            strength = check_strength(pwd)
            print(f"  {i}. {pwd}  [{strength}]")
        print("-" * 40)

        # Let user pick one
        while True:
            try:
                pick = int(input("\nPick a password (1-5) to copy/use: "))
                if 1 <= pick <= 5:
                    chosen = passwords[pick - 1]
                    break
                print("  Please enter 1-5.")
            except ValueError:
                print("  Please enter a valid number.")

        print(f"\n✅ Your password: {chosen}")

        # Try clipboard copy
        try:
            pyperclip.copy(chosen)
            print("📋 Password copied to clipboard!")
        except Exception:
            print("💡 Tip: Install 'pyperclip' to auto-copy passwords.")

        print()
        again = get_yes_no("Generate another password? (Y/N): ")
        if not again:
            print("\n👋 Stay secure! Goodbye.")
            break

if __name__ == "__main__":
    main()
