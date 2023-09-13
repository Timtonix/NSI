from turtle import Turtle, done, update, tracer, Screen
from turtle import *
import random
import time


class Dé(Turtle):
    def __init__(self, coté_carré, x, y):
        super().__init__(visible=False)
        screensize(1920, 1080)

        # On fait en sorte que le traçage soit instantané
        Screen()
        tracer(0)

        self.coté_carré = coté_carré
        self.rayon_cercle = coté_carré / 10

        # X et Y, position du sommet gauche du bas du carré, ce qui permet d'avoir un carré centré
        self.x, self.y = (-(x + self.coté_carré / 2), -(y + self.coté_carré / 2))

    def carré(self):
        self.seth(0)
        self.aller(self.x, self.y)

        for i in range(4):
            self.forward(self.coté_carré)
            self.left(90)

    def cercle(self, x: float, y: float):
        # Dessiner un cercle, son centre se trouve sur les coordonnées données
        self.seth(0)
        self.aller(x, y - self.rayon_cercle)
        self.fillcolor("purple")
        self.begin_fill()
        self.circle(self.rayon_cercle)
        self.end_fill()
    
    def aller(self, x, y):
        # Aller à un point en levant le stylo
        self.up()
        self.goto(x, y)
        self.down()

    def point(self, size, couleur: str):
        # Dessiner un point à partir de son centre
        self.up()
        self.aller(self.x, self.y)
        self.down()
        self.dot(size, couleur)

    def diagonales(self):
        # On dessine les diagonales du carré pour vérifier si le point est bien au centre
        # Fonction inutile car non mis à jour avec les nouvelles fonctions de calcule
        self.aller(self.x, self.y)
        self.down()
        self.goto(self.x + self.coté_carré, self.y + self.coté_carré)
        self.aller(self.x, self.y + self.coté_carré)
        self.down()
        self.goto(self.x + self.coté_carré, self.y)

    def face_vide(self):
        # On dessine la face sans les points
        self.carré()
        self.aller(self.x, self.y)


    """
    Différentes faces du dé
    """
    def point_milieu(self, plusieurs: bool= False):
        if plusieurs:
            # Les deux points du six
            self.cercle(self.x + self.coté_carré / 4, self.y + (self.coté_carré // 2))
            self.cercle(self.x + self.coté_carré / 4 * 3, self.y + (self.coté_carré // 2))
        else:
            # Le point central classique
            self.cercle(self.x + self.coté_carré // 2, self.y + (self.coté_carré // 2) )


    def points_cotés(self, invert: bool= False):
        # Si on a invert, on fait l'inverse par rapport aux pojnts pour un deux, ainsi on peut former un 4
        if invert:
            self.cercle(self.x + self.coté_carré / 4 * 3, self.y + self.coté_carré / 4 )
            self.cercle(self.x + self.coté_carré / 4, self.y + self.coté_carré / 4 * 3 )
        else:
            # points pour le 2 classique
            self.cercle(self.x + self.coté_carré / 4, self.y + self.coté_carré / 4 )
            self.cercle(self.x + self.coté_carré / 4 * 3, self.y + self.coté_carré / 4 * 3 )


    def calcule(self, nombre_points: int):
        # On vérifie que le nombre donné est paire
        if nombre_points % 2 == 0 :
            self.points_cotés()
        else:
            self.point_milieu()

        # Ensuite si il est plus grand que deux on met les 2 points sur les coté
        if nombre_points > 2:
            self.points_cotés()

        # Si il est plus grand que trois, on met les 2 autres points sur les cotés
        if nombre_points > 3:
            self.points_cotés(True)

        # eEt enfin si c'est un six, on met les deux points centraux à gauche et à droite
        if nombre_points == 6:
            # On spécifie que l'on veut plusieurs points, pas comme le simple point du milieu pour le 1, 3 et 5
            self.point_milieu(plusieurs=True)

    def combien_de_dés_max(self):
        nombre_colonne = window_height() // (self.coté_carré + (self.coté_carré // 10) // 2)
        nombre_ligne = window_width() // (self.coté_carré + (self.coté_carré // 10) // 2)

        premiere_pos = (self.coté_carré // 2, self.coté_carré // 2)
        pos_colonne = []
        for point in range(nombre_colonne):
            pos_colonne.append((self.coté_carré // 2, self.coté_carré // 2 + (self.coté_carré + (self.coté_carré // 10) // 2) * point))

        for pos in pos_colonne:
            print(pos)
            x, y = pos
            x, y = (-(x + self.coté_carré / 2), -(y + self.coté_carré / 2))
            print(f"x {x}, y {y}")
            self.aller(x, y)
            for _ in range(4):
                seth(0)
                forward(100)
                left(90)




if __name__ == "__main__":
    dé = Dé(100, 0, 0)
    dé.combien_de_dés_max()
    """nombre_dés = 1 # int(input("Combien de dés voulez-vous ?\n>").strip())
    taille_carré = 150 # int(input("La taille du dé [100; 350])\n>").strip())
    taille_par_dix = taille_carré / 10
    posx = 0
    posy = 0

    position_carré = [(posx, posy), (posx - taille_carré - taille_par_dix, posy), (posx + taille_carré + taille_par_dix, posy),
                      (posx, posy -taille_carré -taille_par_dix), (posx, posy + taille_carré + taille_par_dix )]
    if taille_carré < 100 or taille_carré > 350 :
        raise ValueError(f"La taille du carré {taille_carré} ne convient pas !")


    itération = 0
    for i in range(nombre_dés):
        if i < 5:
            dé = Dé(taille_carré, position_carré[i][0], position_carré[i][1])
        else:
            dé = Dé(taille_carré, position_carré[i][0], position_carré[i][1])
        dé.face_vide()
        dé.calcule(random.randint(1, 6))"""

    update()


    done()
