from OrderItem import  OrderItem
from dataclasses import dataclass
from datastructures.array import Array

@dataclass
class CustomerOrder:
    order:Array[OrderItem]
    name:str="Default"
    status:bool=False

    def __str__(self):
        return f"Order for {self.name}:\n{"\n".join([str(i) for i in self.order])}"