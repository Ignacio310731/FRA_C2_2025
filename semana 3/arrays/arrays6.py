# 6. Mayor y su posición:
# Cargar un array de 7 números enteros. Determinar el valor más alto y en qué posición se
# encuentra.

lista = [235,65,64,5,125,6,23]
mayor = 0
for i in range(len(lista)):
    if lista[i] > mayor:
        mayor = lista[i]
print(mayor)