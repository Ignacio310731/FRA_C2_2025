# 4. Contar mayores a un valor:
# Cargar un array de 8 enteros. Contar cuántos son mayores al valor 100 e informar el resultado.

lista = [0] * 8
contador = 0
for i in range(len(lista)):
    numeros = int(input("Ingrese numeros: "))
    lista[i] += numeros
    if numeros >= 100:
        contador += 1
print(f"{lista}\nSe encontraron {contador} numeros mayores a 100")

lista = [100,2,300,4,5,600,7,8]
contador = 0
for i in range(len(lista)):
    if lista[i] >= 100:
        contador += 1
print(f"{lista}\nSe encontraron {contador} numeros mayores a 100")