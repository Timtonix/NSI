from turtle import Turtle, Screen, screensize, setup, tracer
import pyautogui


def get_screen_size():
    size = pyautogui.size()
    return size.width, size.height


class Dé(Turtle):
    def __init__(self, coté_carré, x, y, couleurs: tuple = ("white", "black"), calculer_pos: bool = True):
        super().__init__(visible=False)

        self.width, self.height = get_screen_size()
        screensize(self.width, self.height)

        # On fait en sorte que le traçage soit instantané
        Screen()
        tracer(0)
        setup(width=1.0, height=1.0, startx=None, starty=None)

        self.coté_carré = coté_carré
        self.rayon_cercle = coté_carré / 10

        self.couleurs = couleurs

        self.x = x
        self.y = y

        # Si on ne passe pas les positions déja calculés
        if calculer_pos:
            # X et Y, position du sommet gauche du bas du carré, ce qui permet d'avoir un carré centré
            self.x, self.y = (-(x + self.coté_carré / 2), -(y + self.coté_carré / 2))

    def carré(self):
        self.seth(0)
        self.aller(self.x, self.y)

        self.fillcolor(self.couleurs[0])
        self.begin_fill()
        for i in range(4):
            self.forward(self.coté_carré)
            self.left(90)
        self.end_fill()

    def cercle(self, x: float, y: float):
        # Dessiner un cercle, son centre se trouve sur les coordonnées données
        self.seth(0)
        self.aller(x, y - self.rayon_cercle)
        self.fillcolor(self.couleurs[1])
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
        """
        Dessine les points du milieu, pour les impairs et le six
        :param plusieurs:
        :return:
        """
        if plusieurs:
            # Les deux points du six
            self.cercle(self.x + self.coté_carré / 4, self.y + (self.coté_carré // 2))
            self.cercle(self.x + self.coté_carré / 4 * 3, self.y + (self.coté_carré // 2))
        else:
            # Le point central classique
            self.cercle(self.x + self.coté_carré // 2, self.y + (self.coté_carré // 2) )


    def points_cotés(self, invert: bool= False):
        """
        Dessine les points du 2, ou du 4
        :param invert:
        :return:
        """
        # Si on a invert, on fait l'inverse par rapport aux points pour un deux, ainsi on peut former un 4
        if invert:
            self.cercle(self.x + self.coté_carré / 4 * 3, self.y + self.coté_carré / 4 )
            self.cercle(self.x + self.coté_carré / 4, self.y + self.coté_carré / 4 * 3 )
        else:
            # points pour le 2 classique
            self.cercle(self.x + self.coté_carré / 4, self.y + self.coté_carré / 4 )
            self.cercle(self.x + self.coté_carré / 4 * 3, self.y + self.coté_carré / 4 * 3 )


    def calcule(self, nombre_points: int):
        """
        On décide quels points à dessiner sur le dés en fonction de `nombre_points`
        :param nombre_points:
        :return:
        """
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



