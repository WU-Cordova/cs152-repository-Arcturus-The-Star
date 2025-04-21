from pwinput import pwinput
from datastructures.hashmap import HashMap
import pickle
import hashlib


def authenticate():
    while True:
        print("Welcome to the Bistro Authentication System\nPlease log in")
        with open("misc_files/passwords.bin", "rb") as file:
            passwords:HashMap = pickle.loads(file.read())
        username = input("Username: ")
        password = pwinput().encode("utf-8")
        if username not in passwords:
            print("Username or password is incorrect, please try again\n")
            continue
        hash_fn = hashlib.sha256()
        salt = passwords[username][1]
        pswd_hash = passwords[username][0]
        hash_fn.update(password + salt)
        check_hash = hash_fn.digest()
        if check_hash != pswd_hash:
            print("Username or password is incorrect, please try again\n")
            continue
        else:
            print("Login successful")
            return

if __name__ == "__main__":
    ...