# 5. Buscar un valor:
# Cargar un array de 10 enteros. Solicitar al usuario un número y verificar si se encuentra en el array.
# Informar la posición en caso afirmativo, o indicar que no se encuentra.

lista = [1,2,3,4,5,6,7,8,9,10]
numeros = int(input("Ingrese numeros: "))
bandera = False
for i in range(len(lista)):
    if lista[i] == numeros:
        bandera = True
        print(f"El numero {numeros}, se encuentra en la posicion {i}")
print(bandera)