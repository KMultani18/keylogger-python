from cryptography.fernet import Fernet
import os

try:
    key = Fernet.generate_key()
    key_file = "filekey.key"

    if os.path.exists(key_file):
        confirm = input(f"{key_file} already exists. Overwrite? (y/n): ")
        if confirm.lower() != "y":
            print("Operation canceled.")
            exit()

    with open(key_file, "wb") as filekey:
        filekey.write(key)

    print("Key generated successfully and saved as filekey.key.")

except PermissionError:
    print("Permission denied: Unable to write key file. Try running as administrator.")

except Exception as e:
    print(f"Error generating key: {e}")
