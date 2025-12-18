import socket
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

s = socket.socket()
s.connect(("RECEIVER_IP", 9999))

s.send(key)

with open("data.txt", "rb") as f:
    encrypted = cipher.encrypt(f.read())
    s.send(encrypted)

print("Encrypted File Sent")
s.close()
