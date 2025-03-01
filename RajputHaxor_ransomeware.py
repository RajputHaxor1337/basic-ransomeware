import os
from cryptography.fernet import Fernet


def generate_key():
    key = Fernet.generate_key()
    with open("key.txt", "wb") as key_file:
        key_file.write(key)
    return key

def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        original_data = file.read()
    encrypted_data = fernet.encrypt(original_data)
    with open(file_path + ".rjhx", "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)


def encrypt_files_in_directory():
    key = generate_key()
    for file_name in os.listdir():
        if os.path.isfile(file_name) and not file_name.endswith(".rjhx") and file_name != "key.txt":
            print(f"Encrypting {file_name}...")
            encrypt_file(file_name, key)
            print(f"Encrypted {file_name} and saved as {file_name}.rjhx")
    print("Encryption completed. Key saved to key.txt.")


if __name__ == "__main__":
    encrypt_files_in_directory()
