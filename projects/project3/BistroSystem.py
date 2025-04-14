from Drink import Drink
from OrderItem import OrderItem
from CustomerOrder import  CustomerOrder
from datastructures.deque import Deque
from datastructures.array import Array
import json

class BistroSystem:
    def __init__(self):
        self.__open_orders:Deque = Deque(data_type=CustomerOrder)
        self.__closed_orders:Array = Array(data_type=CustomerOrder)
        menu_load = json.load(menu := open("menu.json", "r"))
        menu.close()
        self.__menu:dict = {i: Drink(name=i, price=menu_load[i]) for i in menu_load}

    def start(self):
        while True:
            print("Welcome to the Bearcat Bistro!\n\n1. Display Menu\n2. Take New Order\n3. View Open Orders\n4. Mark Next Order as Complete\n5. View End-of-Day Report\n6. Exit")
            while inp := input(">"):
                match inp.strip():
                    case "1":
                        self.__display_menu()
                        break
                    case "2":
                        self.__new_order()
                        break
                    case "3":
                        pass
                    case "4":
                        pass
                    case "5":
                        pass
                    case "6":
                        quit()
                    case _:
                        print("Input not recognized, please try again")

    def __display_menu(self):
        print(f"Menu:\n{"\n".join([str(self.__menu[i]) for i in self.__menu])}")
        input("Press enter to return\n")

    def __new_order(self):
        while item := input("Enter the name of the desired drink\n>"):
            pass



if __name__ == "__main__":
    bs = BistroSystem()
    bs.start()