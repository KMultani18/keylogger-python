from cryptography.fernet import Fernet
import os

# Load the existing key from filekey.key
with open("filekey.key", "rb") as filekey:
    key = filekey.read()

fernet = Fernet(key)

# Read the existing file
with open("key_log.txt", "rb") as file:
    original = file.read()

# Check if it's already encrypted
try:
    fernet.decrypt(original)  # Try decrypting to see if it's already encrypted
    print("File is already encrypted. Skipping encryption.")
except:
    encrypted = fernet.encrypt(original)
    with open("key_log.txt", "wb") as encrypted_file:
        encrypted_file.write(encrypted)
    print("Encryption successful.")
