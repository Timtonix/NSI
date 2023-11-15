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
        self.copie.save(f"noir_blanc.png")

    def filtre_miroir(self):
        blank = Image.new("RGB", (self.largeur, self.hauteur), (0, 0, 0))
        for x in range(self.largeur):
            for y in range(self.hauteur):
                r, g, b = self.copie.getpixel((x, y))
                # print(f"COULEURS : {r}, {g}, {b}\nPositions : {x, y}")
                blank.putpixel((self.largeur - x - 1, y), (r, g, b))
        blank.save(f"miroir.png")


    def filtre_pixel3(self):
        blank = Image.new("RGB", (self.largeur, self.hauteur), (0, 0, 0))
        tmp = []
        pixels = []
        i = 0
        for x in range(self.largeur):
            for y in range(self.hauteur):
                r, g, b = self.copie.getpixel((x, y))
                if i == 0:
                    tmp = [r, g, b]
                    i += 1
                    continue
                tmp[0] += r
                tmp[1] += g
                tmp[2] += b

                if i == 2:
                    pixels.append((tmp[0] // 3, tmp[1] // 3, tmp[2] // 3))
                    tmp[0] = 0
                    tmp[1] = 0
                    tmp[2] = 0
                    i = 0
                    continue
                i += 1

        block = 0
        i = 0
        print(len(pixels))
        for x in range(self.largeur):
            for y in range(self.hauteur):
                if i == 3:
                    i = 0
                    block += 1

                blank.putpixel((x, y), (pixels[block][0], pixels[block][1], pixels[block][2]))
                i += 1
        blank.save("pixel.png")




if __name__ == "__main__":
    filtre = Filtre()
    filtre.filtre_pixel3()