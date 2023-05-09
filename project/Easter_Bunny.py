from project.Chicken import Chicken
from project.Dinosaur import Dinosaur
from project.Egg_Factory import EggFactory
from project.Quail import Quail
import random


class EasterBunny(EggFactory):
    def __init__(self, basket):
        super().__init__(basket)

    def choose_random_class_type(self):
        easter_bunny = random.choice([Quail, Chicken, Dinosaur])
        if len(self.basket) > 5:
            print(f"\n * Eggs are ready! * \nThis is all {len(self.basket)} eggs which are created:")
            [print(f" - {x}") for x in self.basket]
            exit()

        if easter_bunny == Quail:
            Quail(self.basket).decoration_type()
        elif easter_bunny == Chicken:
            Chicken(self.basket).decoration_type()
        elif easter_bunny == Dinosaur:
            Dinosaur(self.basket).decoration_type()

    def decoration_type(self):
        ...
