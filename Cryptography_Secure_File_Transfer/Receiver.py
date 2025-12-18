import socket
from cryptography.fernet import Fernet

s = socket.socket()
s.bind(("0.0.0.0", 9999))
s.listen(1)

conn, addr = s.accept()
key = conn.recv(1024)
cipher = Fernet(key)

data = conn.recv(100000)
decrypted = cipher.decrypt(data)

with open("received.txt", "wb") as f:
    f.write(decrypted)

print("Encrypted File Received & Decrypted")
conn.close()
