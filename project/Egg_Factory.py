from abc import ABC, abstractmethod


class EggFactory(ABC):

    COLORS = ["Red", "Pink", "Orange", "Blue", "Green", "Yellow", "Purple", "Golden", "White", "Cyan"]
    STICKERS = ["flower", "tree", "bunnie", "cloud", "rainbow", "triangle", "square", "car", "rocket", "ice cream"]

    @abstractmethod
    def __init__(self, basket: list):
        self.basket = basket

    @abstractmethod
    def decoration_type(self):
        ...
