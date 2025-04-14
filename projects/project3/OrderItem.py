from Drink import Drink
from dataclasses import dataclass

@dataclass
class OrderItem:
    drink:Drink
    size:str="small"
    customization:str=""

    def __str__(self):
        return f"{self.drink.name}: ${self.drink.price}\n{self.customization}"