#  Cargar y mostrar array:
# Declarar un array de 5 enteros. Cargarlo por teclado y mostrar su contenido por pantalla usando un
# ciclo for.

# lista = [0] * 5

# for i in range(len(lista)):
#     numeros = int(input("Ingrese numeros: "))
#     lista[i] += numeros
#     print(lista)

# 2. Sumar todos los elementos:
# Declarar un array de 10 enteros. Cargarlo por teclado. Calcular y mostrar la suma de todos los
# elementos.

# lista = [0] * 10
# acumulador = 0
# for i in range(len(lista)):
#     numeros = int(input("Ingrese numeros: "))
#     lista[i] += numeros
#     acumulador += numeros
# print(f"{lista}\nLa suma de los numeros ingresados es de: {acumulador}")


# lista = [1,2,3,4,5,6,7,8,9,10]
# acumulador = 0
# for i in range(len(lista)):
#     acumulador += lista[i]
# print(f"{lista}\nLa suma de los numeros ingresados es de: {acumulador}")

# 3. Promedio de valores:
# Declarar un array de 6 números reales (floats). Cargarlo por teclado. Calcular y mostrar el promedio
# de los valores.

# lista = [0] * 6
# acumulador = 0
# for i in range(len(lista)):
#     numeros = float(input("Ingrese numeros: "))
#     lista[i] += numeros
#     acumulador += numeros
#     promedio = acumulador / len(lista)
# print(f"{lista}\nEl promedio de los numeros ingresados es de: {promedio}")

# lista = [1.4,2.5,3.4,4.7,5.3,6.2]
# acumulador = 0
# for i in range(len(lista)):
#     acumulador += lista [i]
#     promedio = acumulador / len(lista)
# print(f"{lista}\nEl promedio de los numeros ingresados es de: {promedio}")

# 4. Contar mayores a un valor:
# Cargar un array de 8 enteros. Contar cuántos son mayores al valor 100 e informar el resultado.

# lista = [0] * 8
# contador = 0
# for i in range(len(lista)):
#     numeros = int(input("Ingrese numeros: "))
#     lista[i] += numeros
#     if numeros >= 100:
#         contador += 1
# print(f"{lista}\nSe encontraron {contador} numeros mayores a 100")

# lista = [100,2,300,4,5,600,7,8]
# contador = 0
# for i in range(len(lista)):
#     if lista[i] >= 100:
#         contador += 1
# print(f"{lista}\nSe encontraron {contador} numeros mayores a 100")

# 5. Buscar un valor:
# Cargar un array de 10 enteros. Solicitar al usuario un número y verificar si se encuentra en el array.
# Informar la posición en caso afirmativo, o indicar que no se encuentra.

# lista = [1,2,3,4,5,6,7,8,9,10]
# numeros = int(input("Ingrese numeros: "))
# bandera = False
# for i in range(len(lista)):
#     if lista[i] == numeros:
#         bandera = True
# print(bandera)


# 6. Mayor y su posición:
# Cargar un array de 7 números enteros. Determinar el valor más alto y en qué posición se
# encuentra.

# lista = [235,65,64,5,125,6,23]
# mayor = 0
# for i in range(len(lista)):
#     if lista[i] > mayor:
#         mayor = lista[i]
# print(mayor)


# 7. Invertir orden:
# Cargar un array de 6 enteros y mostrarlo invertido, es decir, desde el último al primero.

# lista = [1,2,3,4,5,6]

# for i in range(len(lista)-1,-1,-1):
#     print(lista[i])

# 8. Comparar dos arrays:
# Cargar dos arrays de 5 elementos cada uno. Comparar si ambos son iguales elemento a elemento
# y mostrar un mensaje indicando si son o no iguales.

# lista = [1,2,3,4,5]
# lista_2 = [1,2,3,4,5]
# bandera = True
# for i in range(len(lista)):
#         if lista[i] == lista_2[i]:
#             bandera = True
#         else:
#             bandera = False
#             break
#         print(bandera)

# 9. Intercambiar elementos pares por ceros:
# Cargar un array de 10 enteros. Reemplazar todos los elementos pares por cero y mostrar el array
# resultante.

# lista = [1,2,3,4,5,6,7,8,9,10]
# for i in range(len(lista)):
#     if lista[i] % 2 == 0:
#         lista[i] = 0
# print(lista)

# 10. Función para buscar la primera aparición de un valor:
# Escribir una función que reciba un array de enteros y un número a buscar. La función debe retornar
# la posición de la primera aparición de ese número o -1 si no se encuentra.

def array(vector, numero):
    for i in range(len(vector)):
        if vector[i] == numero:
            return i
    return -1
lista = [1,2,3,4,5]
print(array(lista,1))
print(array(lista,4))

