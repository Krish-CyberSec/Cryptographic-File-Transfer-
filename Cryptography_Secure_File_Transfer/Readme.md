# Cryptography & Secure File Transfer Tool

## About This Project (My Perspective)

I developed this project to understand how cryptography is used to secure files during transmission.  
In this project, I implemented file encryption, secure key exchange, hashing, and digital signatures using Python.

The main goal was to securely encrypt a file, transfer it between two systems, and then decrypt it safely at the receiver side.

---

##  Objectives of the Project

- To understand symmetric and asymmetric encryption
- To implement AES for file encryption
- To implement RSA for secure key exchange
- To ensure file integrity using SHA-256 hashing
- To verify authenticity using digital signatures
- To securely transfer encrypted files between two systems

---

## Tools & Technologies Used

- Programming Language: Python 3
- Cryptography Library: cryptography
- Encryption Algorithms:
  - AES (Symmetric Encryption)
  - RSA (Asymmetric Encryption)
- Hash Algorithm: SHA-256
- Environment: Virtual Machines / Local System

---

##  Dependencies Required

Before running the project, I installed the required dependency using:

```bash
pip install -r requirements.txt
```
---
## Project file Structure

Cryptography_Secure_File_Transfer
│
├── AES_Encryption.py
├── AES_Decryption.py
├── RSA_Key_Generation.py
├── RSA_Encrypt_AES_Key.py
├── RSA_Decrypt_AES_Key.py
├── Hash_Generation_SHA256.py
├── Digital_Signature.py
├── Sender.py
├── Receiver.py
│
├── data.txt
├── requirements.txt
├── README.md

