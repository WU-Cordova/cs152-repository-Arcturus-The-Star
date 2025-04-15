from .OrderItem import  OrderItem
from dataclasses import dataclass
from datastructures.array import Array

@dataclass
class CustomerOrder:
    """
    Stores the entire order for a customer.
    :param order: An array of the items in the order
    """
    order:Array[OrderItem]
    name:str="Default"
    status:bool=False

    def __str__(self):
        total_price = 0
        for i in self.order:
            total_price += i.price
        return f"Order for {self.name}:\n{"\n".join([str(i) for i in self.order])}\nTotal price: ${round(total_price, 2)}"