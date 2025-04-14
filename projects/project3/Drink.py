from dataclasses import dataclass

@dataclass
class Drink:
    name:str="Default"
    price:float=1
    large_constant:float = 1.10

    def __str__(self):
        return f"{self.name}- ${str(self.price)} small, ${str(round(self.price * self.large_constant, 2))} large"