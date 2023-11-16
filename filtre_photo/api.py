from PIL import Image
import time

class Filtre:
    def __init__(self):
        maison = Image.open("sam.PNG")
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

    def pixeln(self, n):
        start = time.time()
        blank = Image.new("RGB", (self.largeur, self.hauteur), (0, 0, 0))
        for x in range(0, self.largeur - n, n):
            for y in range(0, self.hauteur - n, n):
                r_tot = 0
                g_tot = 0
                b_tot = 0
                for i in range(n):
                    for j in range(n):
                        r, g, b = self.copie.getpixel((x + i, y + j))
                        r_tot += r
                        g_tot += g
                        b_tot += b
                r = r_tot // n**2
                g = g_tot // n**2
                b = b_tot // n**2
                for i in range(n):
                    for j in range(n):
                        blank.putpixel((x + i, y +j), (r, g, b))

        blank.save("pixel.png")
        end = time.time()
        print(f"TEMPS = {end - start}")

    def filtre_lum(self, lumiere):
        blank = Image.new("RGB", (self.largeur, self.hauteur), (0, 0, 0))
        for x in range(self.largeur):
            for y in range(self.hauteur):
                r, g, b = self.copie.getpixel((x, y))
                blank.putpixel((x, y), (r + lumiere, g + lumiere, b + lumiere))

        blank.save("lumiere.png")

    def inc_color(self, couleur, k):
        blank = Image.new("RGB", (self.largeur, self.hauteur), (0, 0, 0))
        for x in range(self.largeur):
            for y in range(self.hauteur):
                r, g, b = self.copie.getpixel((x, y))
                match couleur:
                    case "rouge":
                        r += k
                        g -= k // 2
                        b -= k // 2
                    case "bleu":
                        b += k
                        g -= k // 2
                        r -= k // 2
                    case "vert":
                        g += k
                        r -= k // 2
                        b -= k // 2
                blank.putpixel((x, y), (r, g, b))
        blank.save("inc_color.png")


    def color512(self):
        colors = [8, 16, 32, 64, 128, 256]
        blank = Image.new("RGB", (self.largeur, self.hauteur), (0, 0, 0))
        for x in range(self.largeur):
            for y in range(self.hauteur):
                couleurs = list(self.copie.getpixel((x, y)))
                rgb = []
                for color in colors:
                    for couleur in couleurs:
                        if couleur < color:
                            rgb.append(color)
                        continue
                blank.putpixel((x, y), (rgb[0], rgb[1], rgb[2]))
        blank.save("512.png")

if __name__ == "__main__":
    filtre = Filtre()
    filtre.color512()