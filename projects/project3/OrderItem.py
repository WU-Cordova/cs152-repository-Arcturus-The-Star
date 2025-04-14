from Drink import Drink
from dataclasses import dataclass

@dataclass
class OrderItem:
    drink:Drink
    size:str
    customization:str