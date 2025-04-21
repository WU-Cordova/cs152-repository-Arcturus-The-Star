import pickle
import os
import pwinput
import hashlib
from misc_files.password_authenticate import authenticate
from datastructures.hashmap import HashMap

def main():
    authenticate()
    print("Welcome to the Bistro User Management System")
    while i := input("Dashboard:\n1. Add User\n2. Remove User\n3. Exit\n>"):
        match i.strip().lower():
            case "1" | "add":
                with open("misc_files/passwords.bin", "rb") as file:
                    passwords:HashMap = pickle.loads(file.read())
                while username := input("\nAdding New User:\nUsername:"):
                    if username in passwords:
                        print("Username already in use, please try again")
                    else:
                        break
                password = pwinput.pwinput().encode("utf-8")
                salt = os.urandom(16)
                hash_fn = hashlib.sha256()
                hash_fn.update(password + salt)
                passwords[username] = (hash_fn.digest(), salt)
                with open("misc_files/passwords.bin", "wb") as file:
                    file.write(pickle.dumps(passwords))
                print("\nUser successfully added\n")
            case "2" | "remove":
                with open("misc_files/passwords.bin", "rb") as file:
                    passwords = pickle.loads(file.read())
                while username := input("\nRemoving a User:\nUsername:"):
                    if username in passwords:
                        del passwords[username]
                        break
                    else:
                        print("User not found, please try again")
                with open("misc_files/passwords.bin", "wb") as file:
                    file.write(pickle.dumps(passwords))
                print("\nUser successfully removed\n")
            case "3" | "exit":
                quit()
            case _:
                print("Input not recognized, please try again")

if __name__ == "__main__":
    main()