import tkinter as tk
from geometria.circulo import Circulo
from geometria.rectangulo import Rectangulo
from geometria.punto import Punto
from geometria.cuadrado import Cuadrado
from geometria.elipse import Elipse
from geometria.triangulo import Triangulo

def main():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Dibujo de Geometría")

    # Crear un lienzo
    canvas = tk.Canvas(root, width=900, height=700)
    canvas.pack()

    # Crear objetos geométricos
    circulo = Circulo(Punto(350, 500), 50, relleno="#367380")
    rectangulo = Rectangulo(Punto(100, 100), Punto(300, 400), "blue", "red")
    cuadrado = Cuadrado(Punto(600, 100), 150, "Blue", "black")
    elipse = Elipse(Punto(600, 400), semieje_mayor=120, semieje_menor=60, relleno="green", borde="black")
    triangulo = Triangulo(Punto(450, 300), Punto(550, 300), Punto(500, 200), borde="purple", relleno="pink")


    # Etiquetas para mostrar área y perímetro
    resultado_rect = tk.Label(root, text="", font=("Arial", 14))
    resultado_rect.pack(pady=2)
    resultado_rect.config(text=f"Área de Rectángulo: {rectangulo.calcular_area()}, Perímetro: {rectangulo.calcular_perimetro()}")

    resultado_cuadrado = tk.Label(root, text="", font=("Arial", 14))
    resultado_cuadrado.pack(pady=2)
    resultado_cuadrado.config(text=f"Área de Cuadrado: {cuadrado.calcular_area()}, Perímetro: {cuadrado.calcular_perimetro()}")

    resultado_elipse = tk.Label(root, text="", font=("Arial", 14))
    resultado_elipse.pack(pady=2)
    resultado_elipse.config(text=f"Área de Elipse: {elipse.calcular_area():.2f}, Perímetro: {elipse.calcular_perimetro():.2f}")

    resultado_circulo = tk.Label(root, text="", font=("Arial", 14))
    resultado_circulo.pack(pady=2)
    resultado_circulo.config(text=f"Área de Círculo: {circulo.calcular_area():.2f}, Perímetro: {circulo.calcular_perimetro():.2f}")

    resultado_triangulo = tk.Label(root, text="", font=("Arial", 14))
    resultado_triangulo.pack(pady=2)
    resultado_triangulo.config(text=f"Área de Triángulo: {triangulo.calcular_area():.2f}, Perímetro: {triangulo.calcular_perimetro():.2f}")

    # Dibujar en el lienzo
    circulo.dibujar(canvas)
    rectangulo.dibujar(canvas)
    cuadrado.dibujar(canvas)
    elipse.dibujar(canvas)
    triangulo.dibujar(canvas)

    # Iniciar el bucle principal
    root.mainloop()

if __name__ == "__main__":
    main()
