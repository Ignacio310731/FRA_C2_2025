# 9. Intercambiar elementos pares por ceros:
# Cargar un array de 10 enteros. Reemplazar todos los elementos pares por cero y mostrar el array
# resultante.

lista = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(lista)):
    if lista[i] % 2 == 0:
        lista[i] = 0
print(lista)