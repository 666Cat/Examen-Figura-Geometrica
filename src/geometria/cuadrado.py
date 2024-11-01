# src/geometria/cuadrado.py

from geometria.geometria import Geometria
from geometria.punto import Punto

class Cuadrado(Geometria):
    def __init__(self, p1, lado, borde="black", relleno=""):
        self.punto_inicial = p1
        self.lado = lado
        self.borde = borde
        self.relleno = relleno

        # Calculamos el punto final basándonos en el lado, ya que es un cuadrado
        self.punto_final = Punto(self.punto_inicial.x + lado, self.punto_inicial.y + lado)

    def calcular_area(self):
        return self.lado ** 2

    def calcular_perimetro(self):
        return 4 * self.lado

    def dibujar(self, canvas):
        canvas.create_rectangle(self.punto_inicial.x, self.punto_inicial.y, self.punto_final.x, self.punto_final.y, outline=self.borde, fill=self.relleno)
