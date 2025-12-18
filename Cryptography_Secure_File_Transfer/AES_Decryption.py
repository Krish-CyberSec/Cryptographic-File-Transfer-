from cryptography.fernet import Fernet

with open("aes_key.key", "rb") as f:
    key = f.read()

cipher = Fernet(key)

with open("data_encrypted.txt", "rb") as f:
    decrypted = cipher.decrypt(f.read())

with open("data_decrypted.txt", "wb") as f:
    f.write(decrypted)

print("File Decrypted")
