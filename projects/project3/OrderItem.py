from Drink import Drink


class OrderItem:
    """
    Stores a drink, its size, and any customization
    :param drink: The drink being modified
    :param size: The size of the drink
    :param customization: The other customization on the drink
    """

    def __init__(self, drink: Drink, size: str = "small", customization: str = ""):
        self.drink = drink
        self.size = size
        self.customization = customization
        self.__price = self.drink.price

    @property
    def price(self) ->float:
        return self.__price * self.drink.large_constant if self.size == "large" else self.__price

    def __str__(self):
        if self.size == "large":
            price = self.price * self.drink.large_constant
        else:
            price = self.price
        return f"{self.size.capitalize()} {self.drink.name}: ${price} - {self.customization}"
