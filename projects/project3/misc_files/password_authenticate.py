from pwinput import pwinput
import base64
import hashlib
import json


def authenticate():
    while True:
        print("Welcome to the Bistro Authentication System\nPlease log in")
        file = open("misc_files/passwords.json", "r")
        passwords = json.load(file)
        file.close()
        username = input("Username: ")
        password = pwinput().encode("utf-8")
        if username not in passwords:
            print("Username or password is incorrect, please try again\n")
            continue
        hash_fn = hashlib.sha256()
        salt = base64.b64decode(passwords[username][1].encode("utf-8"))
        pswd_hash = passwords[username][0]
        hash_fn.update(password + salt)
        check_hash = hash_fn.hexdigest()
        if check_hash != pswd_hash:
            print("Username or password is incorrect, please try again\n")
            continue
        else:
            print("Login successful")
            return
    