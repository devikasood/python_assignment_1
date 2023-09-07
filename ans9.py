def is_valid_password(password):
    if len(password) < 5:
        return False

    if '&' not in password:
        return False

    if not any(char.isupper() for char in password):
        return False

    if not any(char.islower() for char in password):
        return False

    return True

def main():
    while True:
        password = input("Enter a password: ")
        if is_valid_password(password):
            print("Password is valid. It meets all requirements.")
            break
        else:
            print("Password does not meet the requirements. Please try again.")

if __name__ == "__main__":
    main()
