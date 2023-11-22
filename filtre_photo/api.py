from PIL import Image
import time
import urllib



class Filtre:
    def __init__(self, image):
        # Classe Filtre qui prend en paramètre le lien de l'image
        self.image_name = image + ".png"
        f_image = Image.open(image)
        self.largeur = f_image.width
        self.hauteur = f_image.height

        self.calque = Image.new("RGB", (self.largeur, self.hauteur))
        self.copie = f_image.copy()
        self.blank = Image.new("RGB", (self.largeur, self.hauteur), (0, 0, 0))

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

        self.copie.save(f"{couleur}_{self.image_name}")
        end = time.time()
        print(f"Temps : {end - start} secondes")

    def filtre_gris(self):
        for x in range(self.largeur):
            for y in range(self.hauteur):
                r, g, b = self.copie.getpixel((x, y))
                moyenne = (r + b + g) // 3
                self.copie.putpixel((x, y), (moyenne, moyenne, moyenne))
        self.copie.save(f"gris_{self.image_name}")

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
        for x in range(self.largeur):
            for y in range(self.hauteur):
                r, g, b = self.copie.getpixel((x, y))
                # print(f"COULEURS : {r}, {g}, {b}\nPositions : {x, y}")
                self.blank.putpixel((self.largeur - x - 1, y), (r, g, b))
        self.blank.save(f"miroir_{self.image_name}")

    def pixeln(self, n):
        start = time.time()
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
                        self.blank.putpixel((x + i, y +j), (r, g, b))

        self.blank.save(f"pixel_{self.image_name}")
        end = time.time()
        print(f"TEMPS = {end - start}")

    def filtre_lum(self, lumiere):
        # Ajoute de la lumière (du blanc) à l'image
        for x in range(self.largeur):
            for y in range(self.hauteur):
                r, g, b = self.copie.getpixel((x, y))
                self.blank.putpixel((x, y), (r + lumiere, g + lumiere, b + lumiere))

        self.blank.save(f"lumiere_{self.image_name}")

    def inc_color(self, couleur, k):
        # Augmente la valeur d'une certaine couleur
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
                self.blank.putpixel((x, y), (r, g, b))
        self.blank.save(f"inc_color_{self.image_name}")

    def color512(self):
        # La couleur ne sera qu'un multiple de 8
        for x in range(self.largeur):
            for y in range(self.hauteur):
                couleurs = list(self.copie.getpixel((x, y)))
                rgb = []
                for couleur in couleurs:
                    rgb.append((couleur // 16) * 32)

                self.blank.putpixel((x, y), (rgb[0], rgb[1], rgb[2]))
        self.blank.save(f"512{self.image_name}")

if __name__ == "__main__":
    pass