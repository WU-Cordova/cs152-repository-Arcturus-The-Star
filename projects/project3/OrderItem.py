from Drink import Drink
from dataclasses import dataclass

@dataclass
class OrderItem:
    drink:Drink
    customization:str