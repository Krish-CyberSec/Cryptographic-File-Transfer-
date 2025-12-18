import hashlib

with open("data.txt", "rb") as f:
    file_hash = hashlib.sha256(f.read()).hexdigest()

print("SHA-256 Hash:", file_hash)
