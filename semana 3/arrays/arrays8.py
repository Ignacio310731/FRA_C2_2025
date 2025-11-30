# 8. Comparar dos arrays:
# Cargar dos arrays de 5 elementos cada uno. Comparar si ambos son iguales elemento a elemento
# y mostrar un mensaje indicando si son o no iguales.

lista = [1,2,3,4,5]
lista_2 = [1,2,3,4,5]
bandera = True
for i in range(len(lista)):
        if lista[i] == lista_2[i]:
            bandera = True
        else:
            bandera = False
            break
        print(bandera)