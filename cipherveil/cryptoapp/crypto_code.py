from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from base64 import urlsafe_b64encode, urlsafe_b64decode
import os

# Function to derive a key from a password using PBKDF2

def derive_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        iterations=100000,
        salt=salt,
        length=32,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

# Function to encrypt a message using AES-GCM
def encrypt(message, key):
    iv = os.urandom(12)
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(message) + encryptor.finalize()
    return iv + encryptor.tag + ciphertext

# Function to decrypt a message using AES-GCM
# def decrypt(ciphertext, key, tag):
#     cipher = Cipher(algorithms.AES(key), modes.GCM(tag))
#     decryptor = cipher.decryptor()
#     return decryptor.update(ciphertext) + decryptor.finalize()

# def decrypt(ciphertext, key, tag, iv):
#     cipher = Cipher(algorithms.AES(key), modes.GCM(iv, tag), backend=default_backend())
#     decryptor = cipher.decryptor()
#     decrypted_message = decryptor.update(ciphertext) + decryptor.finalize()
#     return decrypted_message

def decrypt(ciphertext, key, tag, iv):
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv, tag), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_message = decryptor.update(ciphertext) + decryptor.finalize()
    return decrypted_message
