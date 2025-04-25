from dataclasses import dataclass

@dataclass
class Drink:
    """
    Stores a drink from menu.bin
    """
    name:str="Default"
    price:float=1
    large_constant:float = 1.10 # What to multiply the price by if the drink is large

    def __str__(self):
        return f"{self.name.capitalize()}- ${str(self.price)} small, ${str(round(self.price * self.large_constant, 2))} large"