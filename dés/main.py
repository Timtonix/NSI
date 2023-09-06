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
    
    def goto(x, y):
        up()
        goto(x, y)
        down()

    
    
dé = Dé(300, 25)

def face_un():
    dé.carré(0, 0)
    dé.cercle(dé.coté_carré // 2, (dé.coté_carré // 2) - dé.rayon_cercle)


def face_deux(x, y):
    dé.carré(x, y)
    goto(x, y)
    dé.cercle(x + dé.coté_carré // 2, y + (dé.coté_carré // 2) - dé.rayon_cercle)


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



    seth(0)
    dé.cercle(-325, 0)




if __name__ == "__main__":
    face_un()
    croquis()
    face_deux(0, -350)
    time.sleep(10)