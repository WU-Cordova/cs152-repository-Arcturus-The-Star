from OrderItem import  OrderItem
from dataclasses import dataclass
from datastructures.array import Array

@dataclass
class CustomerOrder:
    name:str
    order:Array[OrderItem]
    status:bool