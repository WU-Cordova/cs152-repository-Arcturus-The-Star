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
        order = True
        while order:
            current = CustomerOrder(Array())
            cont = True
            while cont :
                item = input("Enter the name of the desired drink\n>")
                if item in self.__menu:
                    while size := input("1. Small\n2. Large\n>"):
                        match size.strip():
                            case "1":
                                size = "small"
                                break
                            case "2":
                                size = "large"
                                break
                            case _:
                                print("Invalid input, please try again")
                    custom = input("Enter any other customization\n>")
                    current.order.append(OrderItem(self.__menu[item], size, custom))
                    while i := input("1. Add more items\n2. Continue to name selection\n>"):
                        match i.strip().lower():
                            case "1" | "add":
                                break
                            case "2" | "continue":
                                cont = False
                                break
                            case _:
                                print("Input not recognized")
                else:
                    print("Invalid item name, please try again")
            current.name = input("Enter the name of the customer\n>")
            print(current)
            while i := input("1. Confirm order\n2. Start over\n>"):
                match i.strip():
                    case "1":
                        self.__open_orders.enqueue(current)
                        order = False
                        break
                    case "2":
                        break
                    case _:
                        print("Input not recognized, please try again")



if __name__ == "__main__":
    bs = BistroSystem()
    bs.start()