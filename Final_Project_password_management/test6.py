# My Super Secret Password Manager!

def make_secret(password):
    secret = ""
    for letter in password:
        secret = secret + str(ord(letter))
    return secret

def find_secret(secret):
    password = ""
    for i in range(0, len(secret), 3):
        number = int(secret[i:i+3])
        password = password + chr(number)
    return password

print("Welcome to My Super Secret Password Manager!")

while True:
    print("\nWhat do you want to do?")
    print("1. Make a secret password")
    print("2. Find out a secret password")
    print("3. Stop playing")

    choice = input("Type 1, 2, or 3: ")

    if choice == "1":
        password = input("Type your secret password: ")
        secret = make_secret(password)
        print("Your super secret password is:", secret)
    elif choice == "2":
        secret = input("Type the secret code: ")
        password = find_secret(secret)
        print("The secret password is:", password)
    elif choice == "3":
        print("Bye bye! Thanks for playing!")
        break
    else:
        print("Oops! I don't understand. Try again!")