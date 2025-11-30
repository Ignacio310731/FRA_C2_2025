# 3. Promedio de valores:
# Declarar un array de 6 números reales (floats). Cargarlo por teclado. Calcular y mostrar el promedio
# de los valores.

lista = [0] * 6
acumulador = 0
for i in range(len(lista)):
    numeros = float(input("Ingrese numeros: "))
    lista[i] += numeros
    acumulador += numeros
    promedio = acumulador / len(lista)
print(f"{lista}\nEl promedio de los numeros ingresados es de: {promedio}")

lista = [1.4,2.5,3.4,4.7,5.3,6.2]
acumulador = 0
for i in range(len(lista)):
    acumulador += lista [i]
    promedio = acumulador / len(lista)
print(f"{lista}\nEl promedio de los numeros ingresados es de: {promedio}")