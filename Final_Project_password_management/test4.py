import json
import os
from cryptography.fernet import Fernet

# กำหนดชื่อไฟล์ที่จะเก็บข้อมูลรหัสผ่าน
password_file = "soda.store"
key_file = "secret.key"

# ฟังก์ชันเพื่อสร้างและบันทึกกุญแจการเข้ารหัส
def generate_key():
    key = Fernet.generate_key()#สร้างกุญแจสำหรับการเข้ารหัส
    with open(key_file, 'wb') as keyfile:#ค้นหาไฟล์ใน key_file ถ้าไม่มีก็สร้างไฟล์ใหม่
        keyfile.write(key)#เขียนkey

# ฟังก์ชันเพื่อโหลดกุญแจการเข้ารหัส
def load_key():
    if not os.path.exists(key_file):#เช็กว่ามีkey_fileไหม
        generate_key()#รับมาจากอันบน
    with open(key_file, 'rb') as keyfile:# เปิดไฟล์ละก็อ่าน
        return keyfile.read()

# สร้าง Fernet ด้วยกุญแจที่โหลดมา
def get_cipher():
    key = load_key()
    return Fernet(key)

# ฟังก์ชันเพื่อเข้ารหัสข้อความ
def encrypt_data(data):
    cipher = get_cipher()
    return cipher.encrypt(data.encode())

# ฟังก์ชันเพื่อถอดรหัสข้อความ
def decrypt_data(encrypted_data):
    cipher = get_cipher()
    return cipher.decrypt(encrypted_data).decode()

# ฟังก์ชันเพื่อโหลดข้อมูลจากไฟล์ JSON
def load_passwords():
    if os.path.exists(password_file):
        with open(password_file, 'rb') as file:
            encrypted_data = file.read()
            decrypted_data = decrypt_data(encrypted_data)
            return json.loads(decrypted_data)
    else:
        return {}

# ฟังก์ชันเพื่อบันทึกข้อมูลลงในไฟล์ JSON
def save_passwords(passwords):
    with open(password_file, 'wb') as file:
        encrypted_data = encrypt_data(json.dumps(passwords, indent=4))
        file.write(encrypted_data)

# ฟังก์ชันเพื่อเพิ่มรหัสผ่านใหม่
def add_password(service, username, password):
    passwords = load_passwords()
    passwords[service] = {
        'username': username,
        'password': password
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
