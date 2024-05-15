import pyxel
import math

class Boule:
    def __init__(self) -> None:
        self.x = 0
        self.y = 128
        self.speed = 0
        self.vx = 0
        self.vy = 0
        self.gravity = 9.81
        self.mass = 0.6
        self.poids = self.gravity * self.mass
        self.epp = self.poids * self.y
        self.ec = 1/2 * self.mass * self.vx**2
        self.em = self.epp + self.ec

    def chute(self):
        self.vx = math.sqrt(self.vx**2 - 2*self.gravity*self.mass)


class App:
    def __init__(self):
        pyxel.init(128, 128)
        self.boule = Boule()
        pyxel.run(self.update, self.draw)

    def update(self):
        self.boule.chute()

    def draw(self):
        pyxel.cls(0)
        pyxel.circ(self.boule.x, self.boule.y, 4, 4)

App()