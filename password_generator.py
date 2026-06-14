# =========================================
# RANDOM PASSWORD GENERATOR
# DecodeLabs - Project 3
# =========================================

import string
import secrets
from datetime import datetime


history_file = "password_history.txt"


def get_password_length():

    while True:

        try:

            length = int(input("\nEnter password length: "))

            if length < 8:

                print("Password length must be at least 8 characters.")

            elif length > 64:

                print("Password length must not be greater than 64 characters.")

            else:

                return length

        except ValueError:

            print("Invalid input! Please enter a number only.")


def generate_password(length):

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    all_characters = lowercase + uppercase + digits + symbols

    password_list = []

    password_list.append(secrets.choice(lowercase))
    password_list.append(secrets.choice(uppercase))
    password_list.append(secrets.choice(digits))
    password_list.append(secrets.choice(symbols))

    remaining_length = length - 4

    for i in range(remaining_length):

        password_list.append(secrets.choice(all_characters))

    secrets.SystemRandom().shuffle(password_list)

    password = "".join(password_list)

    return password


def check_strength(password):

    score = 0

    has_lowercase = False
    has_uppercase = False
    has_digit = False
    has_symbol = False

    for character in password:

        if character in string.ascii_lowercase:

            has_lowercase = True

        elif character in string.ascii_uppercase:

            has_uppercase = True

        elif character in string.digits:

            has_digit = True

        elif character in string.punctuation:

            has_symbol = True

    if len(password) >= 8:

        score = score + 1

    if len(password) >= 12:

        score = score + 1

    if len(password) >= 16:

        score = score + 1

    if has_lowercase:

        score = score + 1

    if has_uppercase:

        score = score + 1

    if has_digit:

        score = score + 1

    if has_symbol:

        score = score + 1

    if score <= 3:

        return "Weak"

    elif score <= 5:

        return "Medium"

    else:

        return "Strong"


def save_password(password, strength):

    date_time = datetime.now().strftime("%d-%m-%Y %I:%M %p")

    with open(history_file, "a") as file:

        file.write(password + "," + strength + "," + date_time + "\n")


def view_history():

    print("\n========== PASSWORD HISTORY ==========")

    try:

        with open(history_file, "r") as file:

            lines = file.readlines()

        if len(lines) == 0:

            print("No password history found.")

        else:

            password_number = 1

            for line in lines:

                line = line.strip()

                if line != "":

                    data = line.split(",")

                    if len(data) == 3:

                        password = data[0]
                        strength = data[1]
                        date_time = data[2]

                        print("Password", password_number)
                        print("Generated Password:", password)
                        print("Strength:", strength)
                        print("Date/Time:", date_time)
                        print("------------------------------")

                        password_number = password_number + 1

    except FileNotFoundError:

        print("No password history found yet.")


def generate_new_password():

    print("\n========== GENERATE PASSWORD ==========")

    length = get_password_length()

    password = generate_password(length)

    strength = check_strength(password)

    print("\nGenerated Password:", password)
    print("Password Strength:", strength)

    save_password(password, strength)

    print("Password saved successfully!")


while True:

    print("\n================================")
    print("   RANDOM PASSWORD GENERATOR")
    print("================================")
    print("1. Generate Password")
    print("2. View Password History")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        generate_new_password()

    elif choice == "2":

        view_history()

    elif choice == "3":

        print("\nProgram Closed Successfully.")

        break

    else:

        print("Invalid Choice! Please select 1, 2, or 3.")
