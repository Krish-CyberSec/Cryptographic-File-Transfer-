from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, serialization

# Load private key
with open("private_key.pem", "rb") as f:
    private_key = serialization.load_pem_private_key(
        f.read(),
        password=None
    )

# Load encrypted AES key
with open("encrypted_aes_key.bin", "rb") as f:
    encrypted_key = f.read()

# Decrypt AES key
decrypted_key = private_key.decrypt(
    encrypted_key,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

with open("aes_key_decrypted.key", "wb") as f:
    f.write(decrypted_key)

print("AES Key Decrypted using RSA")
