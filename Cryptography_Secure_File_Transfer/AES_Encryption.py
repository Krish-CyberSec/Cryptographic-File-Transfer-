from cryptography.fernet import Fernet

# Generate AES key
key = Fernet.generate_key()
cipher = Fernet(key)

# Save key
with open("aes_key.key", "wb") as f:
    f.write(key)

# Encrypt file
with open("data.txt", "rb") as f:
    encrypted = cipher.encrypt(f.read())

with open("data_encrypted.txt", "wb") as f:
    f.write(encrypted)

print("File Encrypted using AES")
