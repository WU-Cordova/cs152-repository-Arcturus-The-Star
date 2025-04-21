from misc_files.password_authenticate import authenticate
from datastructures.hashmap import HashMap
from misc_files.Drink import Drink
import pickle
import json

def main():
    authenticate()
    print("Welcome to the Bistro Menu Editor")
    while i := input("Dashboard:\n1. Add a new item\n2. Remove an old item\n3. Exit\n>"):
        match i.strip().lower():
            case "1" | "add":
                with open("misc_files/menu.bin", "rb") as menu:
                    menumap:HashMap = pickle.loads(menu.read())
                while True:
                    name = input("Enter the name of the new item\n>")
                    name = name.strip()
                    if name in menumap or name == "cancel":
                        print("Name is already in use, please try again")
                    else:
                        break
                while True:
                    try:
                        price = float(input("Enter the price of the new item\n>"))
                        break
                    except ValueError:
                        print("Please input a valid price")
                add_item(name, price)
            case "2" | "remove":
                with open("misc_files/menu.bin", "rb") as file:
                    menumap:HashMap = pickle.loads(file.read())
                print(f"Menu:\n{"\n".join([str(menumap[i]) for i in menumap])}")
                while name := input("Enter the name of the item to remove or cancel to leave\n>"):
                    if name in menumap:
                        remove_item(name)
                        break
                    if name == "cancel":
                        break
                    else:
                        print("Name not recognized, please try again")
            case "3" | "exit":
                break
            case _:
                print("Input not recognized, please try again\n\n")

def add_item(name:str, price:float):
    """
    Adds an item to the menu with price
    :param name: The name of the item
    :param price: The price of the item
    :return:
    """
    with open("misc_files/menu.bin", "rb") as file:
        menu = pickle.loads(file.read())
    menu[name] = Drink(name, price)
    with open("misc_files/menu.bin", "wb") as file:
        file.write(pickle.dumps(menu))

def remove_item(name:str):
    """
    Removes an item from the menu
    :param name: The name of the item
    :return:
    """
    with open("misc_files/menu.bin", "rb") as file:
        menu = pickle.loads(file.read())
    del menu[name]
    with open("misc_files/menu.bin", "wb") as file:
        file.write(pickle.dumps(menu))

if __name__ == "__main__":
    main()