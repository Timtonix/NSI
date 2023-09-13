from turtle import Turtle, done, update, tracer, Screen, screensize, window_width, window_height
import random
import time


class Dé(Turtle):
    def __init__(self, coté_carré, x, y, calculer_pos: bool = True):
        super().__init__(visible=False)
        screensize(1900, 980)

        # On fait en sorte que le traçage soit instantané
        Screen()
        tracer(0)

        self.coté_carré = coté_carré
        self.rayon_cercle = coté_carré / 10

        self.x = x
        self.y = y

        # Si on ne passe pas les positions déja calculés
        if calculer_pos:
            print(calculer_pos)
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


def dessiner_un_max_de_carrés():
    coté_carré = 100
    dédebase = Dé(coté_carré, 0, 0, calculer_pos=False)
    width, height = screensize()

    # Les coordonées du repère orthonormé
    repere = {"x": (-(width // 2), width // 2), "y": (-(height // 2), height // 2)}
    print(repere)

    nombre_colonne, nombre_ligne = colonnes_et_lignes(coté_carré, width, height)

    for i in range(nombre_ligne):
        premiere_pos = (repere["x"][0] + coté_carré // 2 + (coté_carré + (coté_carré // 10) // 2)*i,
                        repere["y"][1] - coté_carré // 2 - (coté_carré + (coté_carré // 10) // 2)*i)
        print(premiere_pos)

        x, y = ((premiere_pos[0] - coté_carré / 2), (premiere_pos[1] - coté_carré / 2))

        pos_premiere_ligne = pos_début_ligne(premiere_pos, coté_carré, nombre_ligne - i)
        pos_premiere_colonne = pos_début_colonne(premiere_pos, coté_carré, nombre_colonne - i)


        dessiner_dé(coté_carré, pos_premiere_colonne)
        dessiner_dé(coté_carré, pos_premiere_ligne)



def colonnes_et_lignes(coté_carré, width, height):
    nombre_colonne = width // (coté_carré + (coté_carré // 10) // 2)
    nombre_ligne = height // (coté_carré + (coté_carré // 10) // 2)
    return (nombre_colonne, nombre_ligne)

def pos_début_ligne(premiere_pos, coté_carré, nombre_ligne):
    pos_début_ligne_list = []
    for point in range(nombre_ligne):
        pos_début_ligne_list.append(
            (premiere_pos[0], premiere_pos[1] - point * (coté_carré + (coté_carré // 10) // 2)))

    return pos_début_ligne_list

def pos_début_colonne(premiere_pos, coté_carré, nombre_ligne):
    pos_début_colonne_list = []
    for point in range(nombre_ligne):
        pos_début_colonne_list.append(
            (premiere_pos[0]  + point * (coté_carré + (coté_carré // 10) // 2), premiere_pos[1]))

    return pos_début_colonne_list


def dessiner_dé(coté_carré, pos_list):
    for pos in pos_list:
        x, y = pos
        x, y = ((x - coté_carré / 2), (y - coté_carré / 2))
        dé = Dé(coté_carré, x, y, False)
        dé.face_vide()
        dé.calcule(random.randint(1, 6))


if __name__ == "__main__":
    dessiner_un_max_de_carrés()
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
