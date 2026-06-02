import base64

def encrypt_file(input_file, encrypted_file):
    with open(input_file, "rb") as file:
        data = file.read()

    encrypted_data = base64.b64encode(data)

    with open(encrypted_file, "wb") as file:
        file.write(encrypted_data)

    print("File encrypted successfully!")

def decrypt_file(encrypted_file, output_file):
    with open(encrypted_file, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = base64.b64decode(encrypted_data)

    with open(output_file, "wb") as file:
        file.write(decrypted_data)

    print("File decrypted successfully!")

print("1. Encrypt File")
print("2. Decrypt File")

choice = input("Enter choice: ")

if choice == "1":
    input_file = input("Enter file name: ")
    encrypted_file = input("Enter encrypted file name: ")
    encrypt_file(input_file, encrypted_file)

elif choice == "2":
    encrypted_file = input("Enter encrypted file name: ")
    output_file = input("Enter output file name: ")
    decrypt_file(encrypted_file, output_file)

else:
    print("Invalid Choice")
