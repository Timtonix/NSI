from turtle import Turtle, done
import random
import time


class Dé(Turtle):
    def __init__(self, coté_carré, rayon_cercle, x, y):
        super().__init__()
        self.speed(0)
        self.coté_carré = coté_carré
        self.rayon_cercle = rayon_cercle
        self.x, self.y = (-(x + self.coté_carré / 2), -(y + self.coté_carré / 2))

    def carré(self):
        self.seth(0)
        self.aller(self.x, self.y)

        for i in range(4):
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

    def face_vide(self):
        self.carré()
        self.aller(self.x, self.y)


    """
    Différentes faces du dé
    """
    def point_milieu(self, plusieurs: bool= False):
        if plusieurs:
            self.cercle(self.x + self.coté_carré / 4, self.y + (self.coté_carré // 2) - self.rayon_cercle)
            self.cercle(self.x + self.coté_carré / 4 * 3, self.y + (self.coté_carré // 2) - self.rayon_cercle)
        else:
            self.cercle(self.x + self.coté_carré // 2, self.y + (self.coté_carré // 2) - self.rayon_cercle)


    def points_cotés(self, invert: bool= False):
        if invert:
            self.cercle(self.x + self.coté_carré / 4 * 3, self.y + self.coté_carré / 4 - self.rayon_cercle)
            self.cercle(self.x + self.coté_carré / 4, self.y + self.coté_carré / 4 * 3 - self.rayon_cercle)
        else:
            self.cercle(self.x + self.coté_carré / 4, self.y + self.coté_carré / 4 - self.rayon_cercle)
            self.cercle(self.x + self.coté_carré / 4 * 3, self.y + self.coté_carré / 4 * 3 - self.rayon_cercle)


    def calcule(self, nombre_points: int):
        if nombre_points % 2 == 0 :
            self.points_cotés()
        else:
            self.point_milieu()

        if nombre_points > 2:
            self.points_cotés()

        if nombre_points > 3:
            self.points_cotés(True)

        if nombre_points == 6:
            self.point_milieu(True)



if __name__ == "__main__":
    nombre_dés = int(input("Combien de dés voulez-vous ?\n>").strip())
    posx = 0
    posy = 0
    for i in range(nombre_dés):
        dé = Dé(250, 25, posx, posy)
        dé.face_vide()
        dé.calcule(6)
        posx += 275


    done()
