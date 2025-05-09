from .Drink import Drink
from .OrderItem import OrderItem
from .CustomerOrder import  CustomerOrder
from datastructures.deque import Deque
from datastructures.linkedlist import LinkedList
from datastructures.hashmap import HashMap
from datetime import datetime
import json
import copy
import pickle


class BistroSystem:
    def __init__(self):
        self.__open_orders:Deque = Deque(data_type=CustomerOrder)
        self.__closed_orders:LinkedList = LinkedList(data_type=CustomerOrder)
        with open("misc_files/menu.bin", "rb") as file:
            self.__menu:HashMap = pickle.loads(file.read())
        self.__report_viewed:bool = False

    def start(self):
        """
        Starts the Bistro Ordering System
        :return:
        """
        print("Welcome to the Bistro Ordering System")
        while True:
            print("Dashboard:\n\n1. Display Menu\n2. Take New Order\n3. View Open Orders\n4. Mark Next Order as Complete\n5. View End-of-Day Report\n6. Exit")
            while inp := input(">"):
                match inp.strip():
                    case "1":
                        self.__display_menu()
                        break
                    case "2":
                        self.__new_order()
                        break
                    case "3":
                        self.__view_open()
                        break
                    case "4":
                        self.__mark_next_complete()
                        break
                    case "5":
                        self.__report()
                        break
                    case "6":
                        self.__exit()
                    case _:
                        print("Input not recognized, please try again")

    def __display_menu(self):
        """
        Displays the current menu
        :return:
        """
        print(f"Menu:\n{"\n".join([str(self.__menu[i]) for i in self.__menu])}")
        input("Press enter to return\n")

    def __new_order(self):
        """
        Creates a new order and adds it to the open orders queue
        :return:
        """
        order = True
        while order:
            current = CustomerOrder(LinkedList())
            cont = True
            while cont :
                item = input("Enter the name of the desired drink\n>")
                if item.strip().lower() in self.__menu:
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
            while i := input(f"{str(current)}\n1. Confirm order\n2. Start over\n>"):
                match i.strip():
                    case "1":
                        self.__open_orders.enqueue(current)
                        order = False
                        break
                    case "2":
                        break
                    case _:
                        print("Input not recognized, please try again")

    def __view_open(self):
        """
        Prints the open orders to the console
        :return:
        """
        orders = copy.deepcopy(self.__open_orders)
        print(f"Open Orders:\n--------------------------------------------\n{"\n--------------------------------------------\n".join([f"{i + 1}. {(orders.dequeue())}" for i in range(len(orders))])}\n--------------------------------------------")
        input("Press enter to return\n")

    def __mark_next_complete(self):
        """
        Marks the next order in the queue as completed and moves it to completed_orders
        :return:
        """
        while i := input(f"The next order is:\n{str(self.__open_orders.front())}\n1. Confirm completion\n2. Cancel and return\n>"):
            match i.strip().lower():
                case "1" | "confirm":
                    self.__closed_orders.append(self.__open_orders.dequeue())
                    break
                case "2" | "cancel" | "exit":
                    break
                case _:
                    print("Input not recognized, please try again")

    def __exit(self):
        """
        Exits the program after a few checks
        :return:
        """
        if len(self.__open_orders):
            while i := input("There are still open orders. Do you want to exit?\n1. Confirm exit\n2. Return to dashboard\n>"):
                match i.strip().lower():
                    case "1" | "exit" | "confirm":
                        break
                    case "2" | "return":
                        return
                    case _:
                        print("Input not recognized, please try again\n")
        if not self.__report_viewed:
            while i := input("You have not viewed an end of day report. Do you want to exit?\n1. Confirm exit\n2. Return to dashboard\n>"):
                match i.strip().lower():
                    case "1" | "exit" | "confirm":
                        break
                    case "2" | "return":
                        return
                    case _:
                        print("Input not recognized, please try again\n")
        quit()

    def __report(self):
        """
        Prints an end of day report
        :return:
        """
        drink_totals ={i:[0,0] for i in self.__menu} # name of drink:[total number of drinks sold, total drink revenue]
        date = datetime.today().strftime("%m-%d-%Y %H-%M")
        for order in self.__closed_orders:
            for item in order.order:
                drink_totals[item.drink.name][0] += 1
                drink_totals[item.drink.name][1] += item.price
        for total in drink_totals:
            drink_totals[total][1] = round(drink_totals[total][1], 2)
        print(f"Report for {date}:\nDrink - Total Sold - Total Revenue\n{"\n".join([f"{i.capitalize()} - {drink_totals[i][0]} - {drink_totals[i][1]}" for i in drink_totals])}\nTotal revenue: ${str(round(sum([drink_totals[i][1] for i in drink_totals]), 2))}")
        while i := input("1. Save to file\n2. Return without saving\n>"):
            match i.strip().lower():
                case "1" | "save":
                    with open(f"Reports/daily_report_{"_".join(date.split(" "))}.bin", "xb") as file:
                        file.write(pickle.dumps(drink_totals))
                        self.__report_viewed = True
                    return
                case "2" | "return":
                    self.__report_viewed = True
                    return
                case _:
                    print("Input not recognized, please try again")