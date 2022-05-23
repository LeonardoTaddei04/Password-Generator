import string as s
import secrets


def generate_password(length: int, symbols: bool, uppercase: bool):
    combination = s.ascii_lowercase + s.digits

    if symbols:
        combination += s.punctuation

    if uppercase:
        combination += s.ascii_uppercase

    combination_length = len(combination)

    new_password = ""

    for _ in range(length):
        new_password += combination[secrets.randbelow(combination_length)]

    return new_password


for _, index in enumerate(range(1)):
    password = generate_password(length=10, symbols=True, uppercase=True)
    full_pw = password
    x="This is your password: "
    print( x , full_pw)
    
documento = open("pwgenerate.txt", "w")
documento.write(x)
documento.write(full_pw)
documento.close()
