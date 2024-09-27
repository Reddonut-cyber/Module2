import json
import os

# Specify the file name to store the password data.
password_file = "key_store.key"

# Dict for use in encoding
encode_dict = {
    'a': -1, 'b': -2, 'c': -3, 'd': -4, 'e': -5, 
    'f': -6, 'g': -7, 'h': -8, 'i': -9, 'j': 10, 
    'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 
    'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 
    'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 
    'z': 26, 'A': 27, 'B': 28, 'C': 29, 'D': 30, 
    'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 
    'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40, 
    'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 
    'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 
    'Y': 51, 'Z': 52, '0': 53, '1': 54, '2': 55, 
    '3': 56, '4': 57, '5': 58, '6': 59, '7': 60, 
    '8': 61, '9': 62, '!': 63, '"': 64, '#': 65, 
    '$': 66, '%': 67, '&': 68, "'": 69, '(': 70, 
    ')': 71, '*': 72, '+': 73, ',': 74, '-': 75, 
    '.': 76, '/': 77, ':': 78, ';': 79, '<': 80, 
    '=': 81, '>': 82, '?': 83, '@': 84, '[': 85, 
    '\\': 86, ']': 87, '^': 88, '_': 89, '`': 90, 
    '{': 91, '|': 92, '}': 93, '~': 94, ' ': 95
}

# Dict for use in decoding
decode_dict = {str(v): k for k, v in encode_dict.items()}

# The function to load data from a JSON file
def load_passwords() -> dict:
    """
    Find the file named key_store.key. 
    If it doesn't exist, create the file. 
    If it exists, use it right away.
    """
    if os.path.exists(password_file):
        with open(password_file, 'r') as file:
            return json.load(file)
    else:
        return {}

# The function to save data into a JSON file
def save_passwords(passwords: dict) -> None:
    """
    Save the password to the key_store.key file
    """
    with open(password_file, 'w') as file:
        json.dump(passwords, file, indent=4)

# Encode function
def password_encode(password: str) -> str: 
    """
    Get the password from the app_password function, 
    enter a for loop to read each character, 
    and compare it with encode_dict
    """
    encode_password = ""
    for char in password:
        encode_password += str(encode_dict[char])
    return encode_password

# Decode function
def password_decode(password: str) -> str:
    """
    Get the password from the get_password function, then count the number of characters in it. 
    Divide the count by 2 (since we will be decoding 2 characters at a time).  
    Then, loop through the password by selecting 2 characters at a time and compare them with decode_dict
      
    """
    num_of_decode_loop = len(password) // 2
    stock = ""
    for i in range(num_of_decode_loop):
         i = i * 2
         find_in_decode_dict = password[i:i+2]
         stock += str(decode_dict[find_in_decode_dict])
    return stock

# Add a new password
def add_password(username: str, appname: str, password: str) -> None:
    """
    Receive the values for username, appname, and 
    password from the menu function and add them to the key_store.key file
    """
    passwords = load_passwords()
    passwords[username] = {
        'appname': appname,
        'password': password_encode(password)
    }
    save_passwords(passwords)
    print(f"Password for {username} saved successfully!")

# Function to retrieve a password
def get_password(username: str) -> None:
    """
    Load the password from the file key_store.key using the key, which is the username.
    Then, decrypt the password and print it out.
    return None
    """
    passwords = load_passwords()
    if username in passwords:
        appname = passwords[username]['appname']
        password = passwords[username]['password']
        decoded_password = password_decode(password)
        print(f"Username: {username}\nAppname: {appname}\nPassword: {decoded_password}")
    else:
        print(f"No password found for {username}")

# Function to display all services where passwords are stored
def list_usernames() -> None:
    """
    List all services and passwords that have been recorded in the system.

    Args: None
    Return: None
    """
    passwords = load_passwords()
    if passwords:
        print("Stored usernames:")
        for username in passwords:
            print(f"- {username}")
    else:
        print("No passwords stored yet.")

# Menu
def main() -> None:
    """
    Send the input to various functions.
    """
    while True:
        print("\nPassword Manager")
        print("1. Add new password")
        print("2. Get password")
        print("3. List all services")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            username = input("Enter the username: ")
            while " " or "" in username:
                print("Do not put ' ' Change your it now!")
                username = input("Enter the username: ")
            appname = input("Enter the appname: ")
            while " " or "" in appname:
                print("Do not put ' ' Change your it now!")
                appname = input("Enter the appname: ")
            password = input("Enter the password: ")
            while " " or "" in password:
                print("Do not put ' ' Change your it now!")
                password = input("Enter the password: ")
            add_password(username, appname, password)
        elif choice == '2':
            username = input("Enter the username: ")
            get_password(username)
        elif choice == '3':
            list_usernames()
        elif choice == '4':
            break
        else:
            print("Invalid option. Please choose again.")

# Start program
if __name__ == '__main__':
    main()
