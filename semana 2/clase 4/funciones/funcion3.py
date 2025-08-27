# 3. Definir una función area_triangulo que reciba la base y la altura de un triángulo y
# devuelva su área. Luego, el programa debe pedir los valores y mostrar el resultado.
# Fórmula: area = (b * h) / 2.

def area_triangulo(base, altura):
    area = (base * altura) / 2
    print(f"El area es {area}")

base = int(input("Ingrese la base: "))
altura = int(input("Ingrese la altura: "))
area_triangulo(base, altura)