from project.Egg_Factory import EggFactory
import random


class Dinosaur(EggFactory):
    def __init__(self, basket):
        super().__init__(basket)

    def decoration_type(self) -> None:
        dinosaur_egg_decoration_type = random.choice(["colors", "stickers"])

        if dinosaur_egg_decoration_type == "colors":
            dinosaur_egg_color = random.choice(EggFactory.COLORS)
            self.basket.append(f"{dinosaur_egg_color} dinosaur egg.")

        elif dinosaur_egg_decoration_type == "stickers":
            dinosaur_egg_sticker = random.choice(EggFactory.STICKERS)
            self.basket.append(f"Dinosaur egg with {dinosaur_egg_sticker} sticker.")

        return print(f"{self.basket[-1]} - created.")
