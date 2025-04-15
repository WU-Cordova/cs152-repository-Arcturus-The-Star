from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from pwinput import pwinput


def authenticate():
    print("Welcome to the Bistro Authentication System\nPlease log in")
    username = input("Username: ")
    password = pwinput()
    