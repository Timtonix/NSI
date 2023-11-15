from PIL import Image
import time

class Filtre:
    def __init__(self):
        maison = Image.open("maison.jpg")
        self.largeur = maison.width
        self.hauteur = maison.height

        self.calque = Image.new("RGB", (self.largeur, self.hauteur))
        self.copie = maison.copy()

    def filtre_couleur(self, couleur):
        start = time.time()
        print(f"Filtre appliqué : {couleur}")
        for x in range(self.largeur):
            for y in range(self.hauteur):
                r, g, b = self.copie.getpixel((x, y))
                if couleur == "Rouge":
                    self.copie.putpixel((x, y), (r, 0, 0))
                    continue
                if couleur == "Vert":
                    self.copie.putpixel((x, y), (0, g, 0))
                    continue
                if couleur == "Bleu":
                    self.copie.putpixel((x, y), (0, 0, b))
                    continue

        self.copie.save(f"{couleur}.png")
        end = time.time()
        print(f"Temps : {end - start} secondes")

    def filtre_gris(self):
        for x in range(self.largeur):
            for y in range(self.hauteur):
                r, g, b = self.copie.getpixel((x, y))
                moyenne = (r + b + g) // 3
                self.copie.putpixel((x, y), (moyenne, moyenne, moyenne))
        self.copie.save(f"gris.png")

    def filtre_noir_blanc(self):
        self.filtre_gris()
        for x in range(self.largeur):
            for y in range(self.hauteur):
                r, g, b = self.copie.getpixel((x, y))
                if r < 128:
                    self.copie.putpixel((x, y), (0, 0, 0))
                    continue
                if r >= 128:
                    self.copie.putpixel((x, y), (255, 255, 255))
