from turtle import Turtle
import random
import time


class Dé(Turtle):
    def __init__(self, coté_carré, rayon_cercle):
        super().__init__()
        self.speed(0)
        self.coté_carré = coté_carré
        self.rayon_cercle = rayon_cercle

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

    def point(self, x, y, size, couleur: str):
        self.up()
        self.aller(x, y)
        self.down()
        self.dot(size, couleur)

    def diagonales(self, x, y):
        self.goto(x, y)
        self.down()
        self.goto(x + self.coté_carré, y + self.coté_carré)
        self.up()
        self.goto(x, y + self.coté_carré)
        self.down()
        self.goto(x + self.coté_carré, y)

    """
    Différentes faces du dé
    """

    def face_un(self, x=0, y=0):
        self.carré(x, y)
        self.cercle(x + self.coté_carré // 2, y + (self.coté_carré // 2) - self.rayon_cercle)

    def face_deux(self, x, y):
        self.carré(x, y)
        self.goto(x, y)
        self.cercle(x + self.coté_carré / 8 * 3, y + self.coté_carré / 8 * 3 - self.rayon_cercle)
        self.cercle(x + self.coté_carré / 8 * 5, y + self.coté_carré / 8 * 5 - self.rayon_cercle)

    def face_trois(self, x, y):
        self.carré(x, y)
        self.goto(x, y)
        self.cercle(x + self.coté_carré / 9 * 3, y + self.coté_carré / 9 * 3 - self.rayon_cercle)
        self.cercle(x + self.coté_carré // 2, y + (self.coté_carré // 2) - self.rayon_cercle)
        self.cercle(x + self.coté_carré / 9 * 6, y + self.coté_carré / 9 * 6 - self.rayon_cercle)
        print(f"premier cercle {x + self.coté_carré // 8 * 3} / {y + self.coté_carré // 8 * 3 - self.rayon_cercle}")
        print(f"deuxième cercle {x + self.coté_carré // 8 * 5} / {y + self.coté_carré // 8 * 5 - self.rayon_cercle}")

    def face_quatre(self, x, y):
        self.carré(x, y)
        self.goto(x, y)
        self.cercle(x + self.coté_carré / 6 * 2, y + (self.coté_carré / 6 * 2) - self.rayon_cercle)
        self.cercle(x + self.coté_carré / 6 * 4, y + (self.coté_carré / 6 * 4) - self.rayon_cercle)
        self.cercle(x + self.coté_carré / 6 * 2, y + (self.coté_carré / 6 * 4) - self.rayon_cercle)
        self.cercle(x + self.coté_carré / 6 * 4, y + (self.coté_carré / 6 * 2) - self.rayon_cercle)

    def face_cinq(self, x, y):
        self.carré(x, y)
        self.goto(x, y)
        self.cercle(x + self.coté_carré // 2, y + (self.coté_carré // 2) - self.rayon_cercle)
        self.cercle(x + self.coté_carré / 6 * 2, y + (self.coté_carré / 6 * 2) - self.rayon_cercle)
        self.cercle(x + self.coté_carré / 6 * 4, y + (self.coté_carré / 6 * 4) - self.rayon_cercle)
        self.cercle(x + self.coté_carré / 6 * 2, y + (self.coté_carré / 6 * 4) - self.rayon_cercle)
        self.cercle(x + self.coté_carré / 6 * 4, y + (self.coté_carré / 6 * 2) - self.rayon_cercle)

    def face_six(self, x, y):
        self.carré(x, y)
        self.goto(x, y)

        # Milieu
        self.cercle(x + self.coté_carré / 6 * 2, y + (self.coté_carré / 2) - self.rayon_cercle)
        self.cercle(x + self.coté_carré / 6 * 4, y + (self.coté_carré / 2) - self.rayon_cercle)

        # Bas
        self.cercle(x + self.coté_carré / 6 * 2, y + (self.coté_carré / 4) - self.rayon_cercle)
        self.cercle(x + self.coté_carré / 6 * 4, y + (self.coté_carré / 4) - self.rayon_cercle)

        # Haut
        self.cercle(x + self.coté_carré / 6 * 2, y + self.coté_carré / 4 * 3 - self.rayon_cercle)
        self.cercle(x + self.coté_carré / 6 * 4, y + self.coté_carré / 4 * 3 - self.rayon_cercle)


def croquis():
    self.carré(-350, 0)
    down()
    i = 0
    while i != 3:
        i += 1
        seth(0)
        forward(self.rayon_cercle*2)
        left(90)
        forward(self.coté_carré)
        right(90)
        forward(self.rayon_cercle*2)
        right(90)
        forward(self.coté_carré)

    self.goto(-350, 0)
    i = 0
    while i != 3:
        i += 1
        seth(0)
        left(90)
        forward(self.rayon_cercle * 2)
        right(90)
        forward(self.coté_carré)
        left(90)
        forward(self.rayon_cercle * 2)
        left(90)
        forward(self.coté_carré)


    seth(0)
    self.cercle(-325, 0)




if __name__ == "__main__":
    dé = Dé(300, 25)

    number = random.randint(1, 6)

    if number == 1:
        dé.face_un(-150, -150)
    if number == 2:
        dé.face_deux(-150, -150)
    if number == 3:
        dé.face_trois(-150, -150)
    if number == 4:
        dé.face_quatre(-150, -150)
    if number == 5:
        dé.face_cinq(-150, -150)
    if number == 6:
        dé.face_six(-150, -150)

    time.sleep(10)
