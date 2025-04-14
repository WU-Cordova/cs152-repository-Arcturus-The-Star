import json

def main():
    menudict = json.load(menu := open("menu.json", "r"))
    menu.close()
    while i := input("Welcome to the Bistro Menu Editor\n1. Add a new item\n2. Remove an old item\n3. Exit\n>"):
        match i.strip():
            case "1":
                name = input("Enter the name of the new item\n>")
                while True:
                    try:
                        price = float(input("Enter the price of the new item\n>"))
                        break
                    except ValueError:
                        print("Please input a valid price")
                add_item(name, price)
            case "2":
                print(f"Menu:\n{"\n".join([str(menudict[i]) for i in menudict])}")
                while name := input("Enter the name of the item to remove\n>"):
                    if name in menudict:
                        remove_item(name)
                        break
                    else:
                        print("Name not recognized, please try again")
            case "3":
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
    menu = json.load(file := open("menu.json", "r"))
    menu[name] = price
    json.dump(file, menu)
    file.close()

def remove_item(name:str):
    """
    Removes an item from the menu
    :param name: The name of the item
    :return:
    """
    menu = json.load(file := open("menu.json", "w"))
    del menu[name]
    json.dump(file, menu)
    file.close()


if __name__ == "__main__":
    main()