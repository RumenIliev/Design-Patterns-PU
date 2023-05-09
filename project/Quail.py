from project.Egg_Factory import EggFactory
import random


class Quail(EggFactory):
    def __init__(self, basket):
        super().__init__(basket)

    def decoration_type(self) -> None:
        quail_egg_decoration_type = random.choice(["colors", "stickers"])

        if quail_egg_decoration_type == "colors":
            quail_egg_color = random.choice(EggFactory.COLORS)
            self.basket.append(f"{quail_egg_color} quail egg.")

        elif quail_egg_decoration_type == "stickers":
            quail_egg_sticker = random.choice(EggFactory.STICKERS)
            self.basket.append(f"Quail egg with {quail_egg_sticker} sticker.")

        return print(f"{self.basket[-1]} - created.")
