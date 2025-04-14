from dataclasses import dataclass

@dataclass
class Drink:
    name:str
    price:float
    size:int=0

    def price_from_size(self):
        match self.size:
            case 0:
                self.price = self.price
            case 1:
                self.price *= 1.10
            case _:
                raise ValueError("Size is invalid")