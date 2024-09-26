import json
import os

# กำหนดชื่อไฟล์ที่จะเก็บข้อมูลรหัสผ่าน
password_file = "store.key"

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

#ตัวใช้ในการdecode
decode_dict = {
 '-1': 'a', '-2': 'b', '-3': 'c', '-4': 'd', '-5': 'e', '-6': 'f', '-7': 'g', '-8': 'h', '-9': 'i',
 '10': 'j', '11': 'k', '12': 'l', '13': 'm', '14': 'n', '15': 'o', '16': 'p', '17': 'q',
 '18': 'r', '19': 's', '20': 't', '21': 'u', '22': 'v', '23': 'w', '24': 'x', '25': 'y',
 '26': 'z', '27': 'A', '28': 'B', '29': 'C', '30': 'D', '31': 'E', '32': 'F', '33': 'G',
 '34': 'H', '35': 'I', '36': 'J', '37': 'K', '38': 'L', '39': 'M', '40': 'N', '41': 'O',
 '42': 'P', '43': 'Q', '44': 'R', '45': 'S', '46': 'T', '47': 'U', '48': 'V', '49': 'W',
 '50': 'X', '51': 'Y', '52': 'Z', '53': '0', '54': '1', '55': '2', '56': '3', '57': '4',
 '58': '5', '59': '6', '60': '7', '61': '8', '62': '9', '63': '!', '64': '"', '65': '#',
 '66': '$', '67': '%', '68': '&', '69': "'", '70': '(', '71': ')', '72': '*', '73': '+',
 '74': ',', '75': '-', '76': '.', '77': '/', '78': ':', '79': ';', '80': '<', '81': '=',
 '82': '>', '83': '?', '84': '@', '85': '[', '86': '\\', '87': ']', '88': '^', '89': '_',
 '90': '`', '91': '{', '92': '|', '93': '}', '94': '~', '95': ' '
}


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
        finde_in_encode_dict = password[i]
        encode_password += str(encode_dict[finde_in_encode_dict])
    return encode_password 


#decode  
def password_decode():
    decode_password = ""
    for i in range(0, len(str), 2):
         find_in_decode_dict = [i]
         decode_password += decode_dict[str[i:i+2]]
    return decode_password

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
        print(f"Service: {service}\nUsername: {username}\nPassword: {password}")
    else:
        print(f"No password found for {service}")

# ฟังก์ชันเพื่อแสดงบริการที่เก็บรหัสผ่านไว้ทั้งหมด
def list_services():
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
            password_encode(password)
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