from cryptography.fernet import Fernet
import os

try: 
    if not os.path.exists("filekey.key"):
        print("Error: Encryption key file not found.")
        exit(1)

# Load the existing key from filekey.key
    with open("filekey.key", "rb") as filekey:
        key = filekey.read()

# using the genrated key
    fernet = Fernet(key)

# open the encrypted file:
    with open("key_log.txt", "rb") as enc_file:
        encrypted = enc_file.read()

# decrypting file
    decrypted = fernet.decrypt(encrypted)

# open file in write mode and put in decrypted data (overwrites file)
    with open("decrypted_log.txt", "wb") as dec_file:
        dec_file.write(decrypted)

except FileNotFoundError as e:
    print(f"Error: {e}")

except Exception as e:
    print(f"Decryption failed: {e}")