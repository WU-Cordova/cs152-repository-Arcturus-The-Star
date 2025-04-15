import json

def main():
    while i := input("Welcome to the Bistro Menu Editor\n1. Add a new item\n2. Remove an old item\n3. Exit\n>"):
        match i.strip().lower():
            case "1" | "add":
                menudict = json.load(menu := open("misc_files/menu.json", "r"))
                menu.close()
                while True:
                    name = input("Enter the name of the new item\n>")
                    name = name.strip()
                    if name in menudict or name == "cancel":
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
                menudict = json.load(menu := open("misc_files/menu.json", "r"))
                menu.close()
                print(f"Menu:\n{"\n".join([i + ": " + str(menudict[i]) for i in menudict])}")
                while name := input("Enter the name of the item to remove or cancel to leave\n>"):
                    if name in menudict:
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
    menu = json.load(file := open("misc_files/menu.json", "r"))
    file.close()
    menu[name] = price
    json.dump(menu, file := open("misc_files/menu.json", "w"), indent=6)
    file.close()

def remove_item(name:str):
    """
    Removes an item from the menu
    :param name: The name of the item
    :return:
    """
    menu = json.load(file := open("misc_files/menu.json", "r"))
    file.close()
    del menu[name]
    json.dump(menu, file := open("misc_files/menu.json", "w"), indent=6)
    file.close()

if __name__ == "__main__":
    main()