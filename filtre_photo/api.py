from PIL import Image

maison = Image.open("maison.jpg")
largeur = maison.width
hauteur = maison.height

calque = Image.new("RGB", (largeur, hauteur))
copie = maison.copy()

for x in range(largeur):
    for y in range(hauteur):
        color = copie.getpixel((x, y))
        copie.putpixel((x, y), (color[0], 0, 0))

copie.save("rouge.png")