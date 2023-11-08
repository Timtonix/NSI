from PIL import Image

maison = Image.open("maison.jpg")
largeur = maison.width
hauteur = maison.height

calque = Image.new("RGB", (largeur, hauteur))
copie = maison.copy()
maison.show()