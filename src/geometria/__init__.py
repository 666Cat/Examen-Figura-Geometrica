from geometria.geometria import Geometria
from geometria.punto import Punto
import math

class Triangulo(Geometria):
    def __init__(self, p1, p2, p3, borde="blue", relleno=""):
        self.punto1 = p1
        self.punto2 = p2
        self.punto3 = p3
        self.borde = borde
        self.relleno = relleno

        # Calcular las longitudes de los lados
        self.lado1 = self._calcular_distancia(self.punto1, self.punto2)
        self.lado2 = self._calcular_distancia(self.punto2, self.punto3)
        self.lado3 = self._calcular_distancia(self.punto3, self.punto1)

    def _calcular_distancia(self, punto_a, punto_b):
        """Calcula la distancia entre dos puntos."""
        return math.sqrt((punto_a.x - punto_b.x) ** 2 + (punto_a.y - punto_b.y) ** 2)

    def calcular_area(self):
        """Calcula el área del triángulo usando la fórmula de Herón."""
        s = (self.lado1 + self.lado2 + self.lado3) / 2
        return math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))

    def calcular_perimetro(self):
        """Calcula el perímetro sumando las longitudes de los lados."""
        return self.lado1 + self.lado2 + self.lado3

    def dibujar(self, canvas):
        """Dibuja el triángulo en el canvas proporcionado."""
        canvas.create_polygon(
            self.punto1.x, self.punto1.y,
            self.punto2.x, self.punto2.y,
            self.punto3.x, self.punto3.y,
            outline=self.borde, fill=self.relleno
        )
