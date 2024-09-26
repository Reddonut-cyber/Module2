def password_decode():
    decode_password = ""
    for i in range(0, len(str), 2):
         find_in_decode_dict = deio[i]
         decode_password += decode_dict[str[i:i+2]]
    print(decode_password)