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
        self.menu = Array(data_type=Drink, starting_sequence=[Drink(i[0], i[1]) for i in json.load(open("menu.json", "r")).values()])

if __name__ == "__main__":
    bs = BistroSystem()
    print(bs.menu)