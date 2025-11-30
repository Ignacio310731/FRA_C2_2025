# 2. Sumar todos los elementos:
# Declarar un array de 10 enteros. Cargarlo por teclado. Calcular y mostrar la suma de todos los
# elementos.

lista = [0] * 10
acumulador = 0
for i in range(len(lista)):
    numeros = int(input("Ingrese numeros: "))
    lista[i] += numeros
    acumulador += numeros
print(f"{lista}\nLa suma de los numeros ingresados es de: {acumulador}")


lista = [1,2,3,4,5,6,7,8,9,10]
acumulador = 0
for i in range(len(lista)):
    acumulador += lista[i]
print(f"{lista}\nLa suma de los numeros ingresados es de: {acumulador}")