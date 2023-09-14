from dé import Dé
from turtle import screensize, done, update, onkeypress, bgcolor
import random
import time


palette = {"red": "#ffb3ba", "orange": "#ffdfba", "yellow": "#ffffba", "green": "#baffc9", "blue": "#bae1ff",
           "purple": "#D2B3FF"}
palette_liste = [("red", "#ffb3ba"), ("orange", "#ffdfba"), ("yellow", "#ffffba"), ("green", "#baffc9"),
                 ("blue", "#bae1ff"),
                 ("purple", "#D2B3FF")]


def dessiner_un_max_de_dés():

    coté_carré = 100
    print(coté_carré)

    dédebase = Dé(coté_carré, 0, 0, calculer_pos=False)
    # On récupère la taille de l'écran
    width, height = dédebase.width, dédebase.height

    # Les coordonées du repère orthonormé
    repere = {"x": (-(width // 2), width // 2), "y": (-(height // 2), height // 2)}
    print(repere)

    # On récupère le nombre de lignes et de colonnes que l'on va pouvoir dessiner
    nombre_colonne, nombre_ligne = colonnes_et_lignes(coté_carré, width, height)

    for i in range(nombre_ligne):
        # On recalcule la position du premier dé à chaque fois
        premiere_pos = (repere["x"][0] + coté_carré // 2 + (coté_carré + (coté_carré // 10) // 2)*i,
                        repere["y"][1] - coté_carré // 2 - (coté_carré + (coté_carré // 10) // 2)*i)
        print(premiere_pos)

        pos_premiere_ligne = pos_début_ligne(premiere_pos, coté_carré, nombre_ligne - i)
        pos_premiere_colonne = pos_début_colonne(premiere_pos, coté_carré, nombre_colonne - i)

        dessiner_dé(coté_carré, [premiere_pos], 0)
        dessiner_dé(coté_carré, pos_premiere_colonne, 1)
        dessiner_dé(coté_carré, pos_premiere_ligne, 1)


def colonnes_et_lignes(coté_carré, width, height):
    nombre_colonne = width // (coté_carré + (coté_carré // 10) // 2)
    nombre_ligne = height // (coté_carré + (coté_carré // 10) // 2)
    return nombre_colonne, nombre_ligne


def pos_début_ligne(premiere_pos, coté_carré, nombre_ligne):
    pos_début_ligne_list = []
    for point in range(1, nombre_ligne):
        pos_début_ligne_list.append(
            (premiere_pos[0], premiere_pos[1] - point * (coté_carré + (coté_carré // 10) // 2)))

    return pos_début_ligne_list


def pos_début_colonne(premiere_pos, coté_carré, nombre_ligne):
    pos_début_colonne_list = []
    for point in range(1, nombre_ligne):
        pos_début_colonne_list.append(
            (premiere_pos[0]  + point * (coté_carré + (coté_carré // 10) // 2), premiere_pos[1]))

    return pos_début_colonne_list


def dessiner_dé(coté_carré, pos_list, couleur):
    for pos in pos_list:
        if couleur == 6:
            couleur = 0

        x, y = pos
        x, y = ((x - coté_carré / 2), (y - coté_carré / 2))
        dé = Dé(coté_carré, x, y, couleurs=(palette_liste[couleur][1], "black"),calculer_pos=False)
        dé.face_vide()
        dé.calcule(random.randint(1, 6))
        couleur += 1
        time.sleep(0.005)
        update()


def choix():
    tous_les_dés = input("Voulez vous afficher un maximum de dés selon la taille de l'écran et de votre dé ? "
                         "\n[y/n] >").strip()

    if "y" in tous_les_dés:
        nombre_dés = "all"
        taille_dé = 100
    else:
        nombre_dés = int(input("Combien de dés voulez-vous ?\n>").strip())
        taille_dé = int(input("La taille du dé [100; 350])\n>").strip())

        if taille_dé < 100 or taille_dé > 350 :
            raise ValueError(f"La taille du carré {taille_dé} ne convient pas !")

    return nombre_dés, taille_dé


if __name__ == "__main__":
    nombre_dés, taille_carré = choix()
    bgcolor("black")
    if nombre_dés == "all":
        dessiner_un_max_de_dés()
    else:
        taille_par_dix = taille_carré / 10
        posx = 0
        posy = 0

        # Position des 5 dés
        position_carré = [(posx, posy), (posx - taille_carré - taille_par_dix, posy), (posx + taille_carré + taille_par_dix, posy),
                          (posx, posy -taille_carré -taille_par_dix), (posx, posy + taille_carré + taille_par_dix )]

        for i in range(nombre_dés):
            if i < 5:
                dé = Dé(taille_carré, position_carré[i][0], position_carré[i][1])
            else:
                dé = Dé(taille_carré, position_carré[i][0], position_carré[i][1])
            dé.face_vide()
            dé.calcule(random.randint(1, 6))

    update()
    done()