

# Mostrar 10 repeticiones de números ascendentes desde el 1 al 10.
# contador = 0
# while contador < 10:
#     contador += 1
#     print(contador)

# Mostrar 10 repeticiones de números descendentes desde el 10 al 1.
# contador = 11
# while contador > 1:
#     contador -= 1
#     print(contador)


# Mostrar la suma de los números desde el 1 hasta el 10.
# numero = 0
# suma = 0 
# while numero < 10:
#     numero += 1
#     suma += numero
#     print(suma)

# Mostrar la suma de los números pares desde el 1 hasta el 10.
# numero = 0
# while numero < 10:
#     numero += 1
#     if numero % 2 == 0:
#         print(numero)


# Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. Mostrar la suma y el promedio por pantalla.
# acumulador = 0
# numeros = 0
# while acumulador <= 5:
#     ingresos = int(input("Ingrese un numero: "))
#     numeros += ingresos
#     acumulador += 1
#     # if acumulador == 5:
#     promedio = numeros / 5
# print(f"El total de numeros es de {numeros}\n El promedio es de {promedio}")
#         # break


# Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números ingresados y
#  el promedio de los mismos.

# suma = 0
# # promedio = 0
# acumulador = 0
# pregunta = True
# while pregunta != "No":
#     numeros = int(input("Ingrese un numero: "))
#     pregunta = input("Deseas ingresar numeros? (Si / No): ")
#     acumulador += 1
#     suma += numeros
#     promedio = suma / acumulador

# print(f"La suma es: {suma}\n El promedio es de: {promedio}")


# Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). 
# Calcular la suma de los números positivos y el producto de los negativos.

# suma = 0
# acumulador = 0
# pregunta = True
# producto = 1
# while pregunta != "No":
#     numeros = int(input("Ingrese un numero: "))
#     pregunta = input("Deseas ingresar numeros? (Si / No): ")
#     acumulador += 1
#     if numeros > 0:
#         suma += numeros
#         print(f"La suma es: {suma}")
#     elif numeros < 0:
#         suma += numeros
#         producto *= numeros
#     print(f"El producto es: {producto}")


# Ingresar 10 números enteros. Determinar el máximo y el mínimo.
# numero = int(input("Ingrese un numero: ")) 
numeros_ingresados = 0
# maximo = 1
# minimo = 1
while numeros_ingresados < 10:
    numero = int(input("Ingrese un numero: "))
    numeros_ingresados += 1
    minimo = 0
    maximo = 0
    if numero < minimo:
        minimo == numero
    elif numero > maximo:
        maximo == numero
    print(f"El maximo es: {maximo}\n El minimo es: {minimo}")






