import json
import os
import pwinput
import hashlib
import base64
from misc_files.password_authenticate import authenticate

def main():
    authenticate()
    print("Welcome to the Bistro User Management System")
    while i := input("Dashboard:\n1. Add User\n2. Remove User\n3. Change Password\n4. Exit\n>"):
        match i.strip().lower():
            case "1" | "add":
                file = open("misc_files/passwords.json", "r")
                passwords = json.load(file)
                file.close()
                while username := input("Adding New User:\nUsername:"):
                    if username in passwords:
                        print("Username already in use, please try again")
                    else:
                        break
                password = pwinput.pwinput().encode("utf-8")
                salt = os.urandom(16)
                hash_fn = hashlib.sha256()
                hash_fn.update(password + salt)
                passwords[username] = [hash_fn.hexdigest(), base64.b64encode(salt).decode("utf-8")]
                file = open("misc_files/passwords.json", "w")
                json.dump(passwords, file)
                file.close()
            case "2" | "remove":
                pass
            case "3" | "change":
                pass
            case "4" | "exit":
                quit()
            case _:
                print("Input not recognized, please try again")

if __name__ == "__main__":
    main()