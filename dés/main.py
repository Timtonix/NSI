from turtle import Turtle
import random
import time


class Dé(Turtle):
    def __init__(self, coté_carré, rayon_cercle, x, y):
        super().__init__()
        self.speed(0)
        self.coté_carré = coté_carré
        self.rayon_cercle = rayon_cercle

        self.x = x
        self.y = y

    def carré(self, x, y):
        self.seth(0)
        self.aller(x, y)

        i = 0
        while i != 4:
            i += 1
            self.forward(self.coté_carré)
            self.left(90)

    def cercle(self, x: float, y: float):
        self.seth(0)
        self.aller(x, y)
        self.fillcolor("purple")
        self.begin_fill()
        self.circle(self.rayon_cercle)
        self.end_fill()
    
    def aller(self, x, y):
        self.up()
        self.goto(x, y)
        self.down()

    def point(self, size, couleur: str):
        self.up()
        self.aller(self.x, self.y)
        self.down()
        self.dot(size, couleur)

    def diagonales(self):
        self.aller(self.x, self.y)
        self.down()
        self.goto(self.x + self.coté_carré, self.y + self.coté_carré)
        self.aller(self.x, self.y + self.coté_carré)
        self.down()
        self.goto(self.x + self.coté_carré, self.y)

    """
    Différentes faces du dé
    """

    def face_un(self):
        self.carré(self.x, self.y)
        self.cercle(self.x + self.coté_carré // 2, self.y + (self.coté_carré // 2) - self.rayon_cercle)

    def face_deux(self):
        self.carré(x, y)
        self.aller(x, y)
        self.cercle(x + self.coté_carré / 8 * 3, y + self.coté_carré / 8 * 3 - self.rayon_cercle)
        self.cercle(x + self.coté_carré / 8 * 5, y + self.coté_carré / 8 * 5 - self.rayon_cercle)

    def face_trois(self):
        self.carré(x, y)
        self.aller(x, y)
        self.cercle(self.x + self.coté_carré / 9 * 3, self.y + self.coté_carré / 9 * 3 - self.rayon_cercle)
        self.cercle(self.x + self.coté_carré // 2, self.y + (self.coté_carré // 2) - self.rayon_cercle)
        self.cercle(self.x + self.coté_carré / 9 * 6, self.y + self.coté_carré / 9 * 6 - self.rayon_cercle)
        print(f"premier cercle {self.x + self.coté_carré // 8 * 3} / {self.y + self.coté_carré // 8 * 3 - self.rayon_cercle}")
        print(f"deuxième cercle {self.x + self.coté_carré // 8 * 5} / {self.y + self.coté_carré // 8 * 5 - self.rayon_cercle}")

    def face_quatre(self):
        self.carré(self.x, self.y)
        self.aller(self.x, self.y)
        self.cercle(self.x + self.coté_carré / 6 * 2, self.y + (self.coté_carré / 6 * 2) - self.rayon_cercle)
        self.cercle(self.x + self.coté_carré / 6 * 4, self.y + (self.coté_carré / 6 * 4) - self.rayon_cercle)
        self.cercle(self.x + self.coté_carré / 6 * 2, self.y + (self.coté_carré / 6 * 4) - self.rayon_cercle)
        self.cercle(self.x + self.coté_carré / 6 * 4, self.y + (self.coté_carré / 6 * 2) - self.rayon_cercle)

    def face_cinq(self):
        self.carré(self.x, self.y)
        self.aller(self.x, self.y)
        self.cercle(self.x + self.coté_carré // 2, self.y + (self.coté_carré // 2) - self.rayon_cercle)
        self.cercle(self.x + self.coté_carré / 6 * 2, self.y + (self.coté_carré / 6 * 2) - self.rayon_cercle)
        self.cercle(self.x + self.coté_carré / 6 * 4, self.y + (self.coté_carré / 6 * 4) - self.rayon_cercle)
        self.cercle(self.x + self.coté_carré / 6 * 2, self.y + (self.coté_carré / 6 * 4) - self.rayon_cercle)
        self.cercle(self.x + self.coté_carré / 6 * 4, self.y + (self.coté_carré / 6 * 2) - self.rayon_cercle)

    def face_six(self):
        self.carré(self.x, self.y)
        self.aller(self.x, self.y)

        # Milieu
        self.cercle(self.x + self.coté_carré / 6 * 2, self.y + (self.coté_carré / 2) - self.rayon_cercle)
        self.cercle(self.x + self.coté_carré / 6 * 4, self.y + (self.coté_carré / 2) - self.rayon_cercle)

        # Bas
        self.cercle(self.x + self.coté_carré / 6 * 2, self.y + (self.coté_carré / 4) - self.rayon_cercle)
        self.cercle(self.x + self.coté_carré / 6 * 4, self.y + (self.coté_carré / 4) - self.rayon_cercle)

        # Haut
        self.cercle(self.x + self.coté_carré / 6 * 2, self.y + self.coté_carré / 4 * 3 - self.rayon_cercle)
        self.cercle(self.x + self.coté_carré / 6 * 4, self.y + self.coté_carré / 4 * 3 - self.rayon_cercle)





if __name__ == "__main__":
    dé = Dé(300, 25, -150, -150)
    dédeux = Dé(300, 300)

    number = random.randint(1, 6)

    if number == 1:
        dé.face_un()
    if number == 2:
        dé.face_deux()
    if number == 3:
        dé.face_trois()
    if number == 4:
        dé.face_quatre()
    if number == 5:
        dé.face_cinq()
    if number == 6:
        dé.face_six()

    time.sleep(10)
