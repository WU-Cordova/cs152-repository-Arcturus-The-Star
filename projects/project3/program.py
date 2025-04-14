import json

from Drink import Drink

def main():
    
    drinks = {"Mocha":("Mocha", 7.50), "Latte":("Latte", 6.25), "Espresso":("Espresso", 3.75),
              "Americano":("Americano", 5.25), "Cappuccino":("Cappuccino", 5.75)}
    out_file = open("menu.json", "w")
    json.dump(drinks, out_file, indent=6)



if __name__ == '__main__':
    main()
