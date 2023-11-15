from PIL import Image

maison = Image.open("maison.jpg")
largeur = maison.width
hauteur = maison.height

calque = Image.new("RGB", (largeur, hauteur))
copie = maison.copy()


def filtre_couleur(couleur):
    for x in range(largeur):
        for y in range(hauteur):
            color = copie.getpixel((x, y))
            if couleur == "Rouge":
                copie.putpixel((x, y), (color[0], 0, 0))
                continue
            if couleur == "Vert":
                copie.putpixel((x, y), (0, color[1], 0))
                continue
            if couleur == "Bleu":
                copie.putpixel((x, y), (0, 0, color[2]))


copie.save("rouge.png")