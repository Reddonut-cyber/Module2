import json
import os

# กำหนดชื่อไฟล์ที่เก็บ
file_key = "store.key"

# ฟังก์ชันเพื่อโหลดข้อมูลจากไฟล์ JSON
def load_passwords():
    if os.path.exists(file_key):
        with open(file_key, 'r') as file:
            return json.load(file)
    else:
        return {}

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

# ตัวใช้ในการ decode
decode_dict = {str(v): k for k, v in encode_dict.items()}

# ฟังก์ชันเข้ารหัส
def password_encode(password):
    encode_password = ""
    for char in password:
        encode_password += str(encode_dict[char]) + " "     
    print(encode_password)
    
    # เขียนพาสเวิร์ดที่เข้ารหัสลงไฟล์
    with open(file_key, "w") as f:
        f.write(encode_password.strip())  # ตัดช่องว่างท้ายออก
    print(f"Password encoded and saved to {file_key}")



# ฟังก์ชันถอดรหัส
def password_decode():
    decode_password = ""
    
    # อ่านไฟล์ที่เข้ารหัส
    with open(file_key, "r") as f:
        encoded_content = f.read().split()
    
    # ถอดรหัสจากค่าตัวเลขที่เก็บไว้
    for item in encoded_content:
        decode_password += decode_dict[item]
    
    print("Your password:", decode_password)

# ใช้งาน
while True:
    print("1.Add password: ")
    print("2.Get password: ")
    print("3.Exist: ")
    action = input("What do you want to do:")

    if action == '1':
        username = input("Your user name: ")
        app_name = input("App name: ")
        password = input("Password: ")
        password_encode(password)

    elif action == '2':
        password_decode()
    elif action == '3':
        print("CU")
        break
    else:
        print("We doesn't have that:")


