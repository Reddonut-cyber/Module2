import json
import os

# กำหนดชื่อไฟล์ที่จะเก็บข้อมูลรหัสผ่าน
password_file = "key_store.key"

# ตัวใช้ในการ encode
encode_dict = {
 'a': -1, 'b': -2, 'c': -3, 'd': -4, 'e': -5, 'f': -6, 'g': -7, 'h': -8, 'i': -9, 
 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 
 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 
 'z': 26, 'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 
 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41, 
 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 
 'X': 50, 'Y': 51, 'Z': 52, '0': 53, '1': 54, '2': 55, '3': 56, '4': 57, 
 '5': 58, '6': 59, '7': 60, '8': 61, '9': 62, '!': 63, '"': 64, '#': 65, 
 '$': 66, '%': 67, '&': 68, "'": 69, '(': 70, ')': 71, '*': 72, '+': 73, 
 ',': 74, '-': 75, '.': 76, '/': 77, ':': 78, ';': 79, '<': 80, '=': 81, 
 '>': 82, '?': 83, '@': 84, '[': 85, '\\': 86, ']': 87, '^': 88, '_': 89, 
 '`': 90, '{': 91, '|': 92, '}': 93, '~': 94, ' ': 95
}

decode_dict = {}
for k, v in encode_dict.items():
    decode_dict[str(v)] = k


# ฟังก์ชันเพื่อโหลดข้อมูลจากไฟล์ JSON
def load_passwords():
    if os.path.exists(password_file):
        with open(password_file, 'r') as file:
            return json.load(file)
    else:
        return {}

# ฟังก์ชันเพื่อบันทึกข้อมูลลงในไฟล์ JSON
def save_passwords(passwords):
    with open(password_file, 'w') as file:
        json.dump(passwords, file, indent=4)

#encode
def password_encode(password):
    encode_password = "" 
    for i in range(len(password)):
        find_in_encode_dict = password[i]
        encode_password += str(encode_dict[find_in_encode_dict])
    return encode_password 

#decode
def password_decode(password):
    num_of_decode_loop = len(password) // 2
    stock = ""
    for i in range(num_of_decode_loop):
         i = i * 2
         find_in_decode_dict = password[i : i+2]
         stock += str(decode_dict[find_in_decode_dict])
    return stock

# ฟังก์ชันเพื่อเพิ่มรหัสผ่านใหม่
def add_password(service, username, password):
    passwords = load_passwords()
    passwords[service] = {
        'username': username,
        'password': password_encode(password)
    }
    save_passwords(passwords)
    print(f"Password for {service} saved successfully!")

# ฟังก์ชันเพื่อดึงรหัสผ่าน
def get_password(service):
    passwords = load_passwords()
    if service in passwords:
        username = passwords[service]['username']
        password = passwords[service]['password']
        decode = password_decode(password)
        print(f"Service: {service}\nUsername: {username}\nPassword: {decode}")
    else:
        print(f"No password found for {service}")

# ฟังก์ชันเพื่อแสดงบริการที่เก็บรหัสผ่านไว้ทั้งหมด
def list_services():
    """
    List all services and passwords that has been recorded to the system.

    Args: None

    Return: None
    """
    passwords = load_passwords() 
    if passwords:
        print("Stored services:")
        for service in passwords:
            print(f"- {service}")
    else:
        print("No passwords stored yet.")

# เมนูหลักของโปรแกรม
def main():
    while True:
        print("\nPassword Manager")
        print("1. Add new password")
        print("2. Get password")
        print("3. List all services")
        print("4. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            service = input("Enter the service name: ")
            username = input("Enter the username: ")
            password = input("Enter the password: ")
            add_password(service, username, password)
        elif choice == '2':
            service = input("Enter the service name: ")
            get_password(service)
        elif choice == '3':
            list_services()
        elif choice == '4':
            break
        else:
            print("Invalid option. Please choose again.")

# เริ่มโปรแกรม
if __name__ == '__main__':
    main()
