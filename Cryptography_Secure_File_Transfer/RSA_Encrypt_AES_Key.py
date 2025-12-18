from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, serialization

# Load public key
with open("public_key.pem", "rb") as f:
    public_key = serialization.load_pem_public_key(f.read())

# Load AES key
with open("aes_key.key", "rb") as f:
    aes_key = f.read()

# Encrypt AES key
encrypted_key = public_key.encrypt(
    aes_key,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

with open("encrypted_aes_key.bin", "wb") as f:
    f.write(encrypted_key)

print("AES Key Encrypted using RSA")
