from project.Egg_Factory import EggFactory
import random


class Chicken(EggFactory):
    def __init__(self, basket):
        super().__init__(basket)

    def decoration_type(self) -> None:
        chicken_egg_decoration_type = random.choice(["colors", "stickers"])

        if chicken_egg_decoration_type == "colors":
            chicken_egg_color = random.choice(EggFactory.COLORS)
            self.basket.append(f"{chicken_egg_color} chicken egg.")

        elif chicken_egg_decoration_type == "stickers":
            chicken_egg_sticker = random.choice(EggFactory.STICKERS)
            self.basket.append(f"Chicken egg with {chicken_egg_sticker} sticker.")

        return print(f"{self.basket[-1]} - created.")
