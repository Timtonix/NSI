from turtle import *
import random
import time





class Dé():
    def __init__(self, coté_carré, rayon_cercle):
        speed(0)
        self.coté_carré = coté_carré
        self.rayon_cercle = rayon_cercle

    def carré(self, x, y):
        seth(0)
        up()
        goto(x, y)
        down()
        
        i = 0
        while i != 4:
            i += 1
            forward(self.coté_carré)
            left(90)

    def cercle(self, x: float, y: float):
        seth(0)
        up()
        goto(x, y)
        down()
        fillcolor("purple")
        begin_fill()
        circle(self.rayon_cercle)
        end_fill()
    
    def goto(self, x, y):
        up()
        goto(x, y)
        down()

    def dot(self, x, y, size, couleur: str):
        up()
        goto(x, y)
        down()
        dot(size, couleur)

    def diagonales(self, x, y):
        self.goto(x, y)
        down()
        goto(x + self.coté_carré, y + self.coté_carré)
        up()
        goto(x, y + self.coté_carré)
        down()
        goto(x + self.coté_carré, y)


def face_un(x=0, y=0):
    dé.carré(0, 0)
    dé.cercle(x + dé.coté_carré // 2, y + (dé.coté_carré // 2) - dé.rayon_cercle)
    dé.diagonales(x, y)


def face_deux(x, y):
    dé.carré(x, y)
    dé.goto(x, y)
    dé.cercle(x + dé.coté_carré / 8 * 3, y + dé.coté_carré / 8 * 3 - dé.rayon_cercle)
    dé.cercle(x + dé.coté_carré / 8 * 5, y + dé.coté_carré / 8 * 5 - dé.rayon_cercle)


def face_trois(x, y):
    dé.carré(x, y)
    dé.goto(x, y)
    dé.cercle(x + dé.coté_carré / 9 * 3, y + dé.coté_carré / 9 * 3 - dé.rayon_cercle)
    dé.cercle(x + dé.coté_carré // 2, y + (dé.coté_carré // 2) - dé.rayon_cercle)
    dé.cercle(x + dé.coté_carré / 9 * 6, y + dé.coté_carré / 9 * 6 - dé.rayon_cercle)
    print(f"premier cercle {x + dé.coté_carré // 8 * 3} / {y + dé.coté_carré // 8 * 3 - dé.rayon_cercle}")
    print(f"deuxième cercle {x + dé.coté_carré // 8 * 5} / {y + dé.coté_carré // 8 * 5 - dé.rayon_cercle}")

    dé.diagonales(x, y)


def croquis():
    dé.carré(-350, 0)
    down()
    i = 0
    while i != 3:
        i += 1
        seth(0)
        forward(dé.rayon_cercle*2)
        left(90)
        forward(dé.coté_carré)
        right(90)
        forward(dé.rayon_cercle*2)
        right(90)
        forward(dé.coté_carré)

    dé.goto(-350, 0)
    i = 0
    while i != 3:
        i += 1
        seth(0)
        left(90)
        forward(dé.rayon_cercle * 2)
        right(90)
        forward(dé.coté_carré)
        left(90)
        forward(dé.rayon_cercle * 2)
        left(90)
        forward(dé.coté_carré)


    seth(0)
    dé.cercle(-325, 0)




if __name__ == "__main__":
    dé = Dé(300, 25)
    face_un(0, 0)
    face_trois(0, -350)
    time.sleep(20)