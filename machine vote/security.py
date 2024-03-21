import random

class Security:
    def __init__(self, nombre_candidat: int, niveau_securite: int, options):
        self.nombre_candidat = nombre_candidat
        self.niveau_securite = niveau_securite
        self.options = options



    def analyse(self, choice: int):
        # Systeme permettant d'éviter la triche
        if choice == self.niveau_securite:
            return str(choice)

        scope = random.randint(0, 100)
        target = 100 // self.nombre_candidat + random.randint(-10, 10)
        size = 100 // self.nombre_candidat + random.randint(5, 20)

        seed = ""
        for i in range(self.nombre_candidat):
            if i == self.niveau_securite:
                seed += str(i)*size
            elif i == choice:
                seed += str(i)*size
            else:
                seed += str(i)*target
        print(seed)
        return random.choice(seed)