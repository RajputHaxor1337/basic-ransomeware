import os
from cryptography.fernet import Fernet


def decrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()
    try:
        decrypted_data = fernet.decrypt(encrypted_data)
        original_file_name = file_path[:-5]  
        with open(original_file_name, "wb") as decrypted_file:
            decrypted_file.write(decrypted_data)
        print(f"Decrypted {file_path} and saved as {original_file_name}")
    except Exception as e:
        print(f"Failed to decrypt {file_path}: {e}")


def decrypt_files_in_directory():
    key = input("Enter the decryption key: ").strip().encode()
    for file_name in os.listdir():
        if os.path.isfile(file_name) and file_name.endswith(".rjhx"):
            print(f"Decrypting {file_name}...")
            decrypt_file(file_name, key)
    print("Decryption completed.")


if __name__ == "__main__":
    decrypt_files_in_directory()
