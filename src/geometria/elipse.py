import math
from geometria.geometria import Geometria
from geometria.punto import Punto

class Elipse(Geometria):
    def __init__(self, p, semieje_mayor, semieje_menor, borde="black", relleno=""):
        self.punto = p
        self.semieje_mayor = semieje_mayor
        self.semieje_menor = semieje_menor
        self.borde = borde
        self.relleno = relleno

    def calcular_area(self):
        # El área de una elipse es π * semieje_mayor * semieje_menor
        return math.pi * self.semieje_mayor * self.semieje_menor

    def calcular_perimetro(self):
        # Fórmula aproximada de Ramanujan para el perímetro de una elipse
        a = self.semieje_mayor
        b = self.semieje_menor
        h = ((a - b)**2) / ((a + b)**2)
        return math.pi * (a + b) * (1 + (3 * h) / (10 + math.sqrt(4 - 3 * h)))

    def dibujar(self, canvas):
        # Dibuja la elipse utilizando las coordenadas de los extremos de los semiejes
        canvas.create_oval(
            self.punto.x - self.semieje_mayor, self.punto.y - self.semieje_menor,
            self.punto.x + self.semieje_mayor, self.punto.y + self.semieje_menor,
            outline=self.borde, fill=self.relleno
        )
