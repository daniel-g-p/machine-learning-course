username = input("Username: ")

while len(username) < 6:
    print("Please enter a username that's at least 6 characters long")
    username = input("Username: ")

password = input("Password: ")

while len(password) < 8:
    password = input(
        "Please enter a password that's at least 8 characters long: ")

confirm_password = input("Confirm password: ")

if password != confirm_password:
    print("Passwords don't match")
else:
    password_length = len(password)
    print(f"Hi @{username}, your password {'*' * password_length} is {password_length} characters long.")
