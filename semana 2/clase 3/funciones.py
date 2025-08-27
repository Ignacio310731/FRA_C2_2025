# 1. Escribir una función llamada saludar(nombre) que reciba un nombre como parámetro e imprima
# un saludo. Luego, el programa debe pedir el nombre del usuario y llamar a la función.

# def saludar(nombre):
#     print(f"Hola {nombre}")

# usuario = input("Ingrese tu nombre: ")
# saludar(usuario)

# 2. Escribir una función operaciones(num1, num2) que reciba dos números y muestre su suma,
# resta y multiplicación. Luego, el programa debe pedir dos números al usuario y llamar a la
# función.

# def operaciones(num1, num2):
#     suma = num1 + num2
#     resta = num1 - num2
#     multiplicacion = num1 * num2
#     print(f"La suma es {suma}\n La resta es {resta} \n La multiplicacion {multiplicacion} ")
#     # return suma, resta, multiplicacion

# numero1 = int(input("Ingrese el primer numero: "))
# numero2 = int(input("Ingrese el segundo numero: "))
# operaciones(numero1, numero2)
# 3. Definir una función area_triangulo que reciba la base y la altura de un triángulo y
# devuelva su área. Luego, el programa debe pedir los valores y mostrar el resultado.
# Fórmula: area = (b * h) / 2.

# def area_triangulo(base, altura):
#     area = (base * altura) / 2
#     print(f"El area es {area}")

# base = int(input("Ingrese la base: "))
# altura = int(input("Ingrese la altura: "))
# area_triangulo(base, altura)

# 4. Crear una función buscar_mayor que reciba tres números y devuelva los tres números
# ordenados de mayor a menor. Luego, el programa debe pedir los números y mostrar los números
# ordenados.

# def buscar_mayor(num1, num2, num3):
#     mayor = 0
#     medio = 0
#     menor = 0
#     if num1 > num2:
#         if num1 > num3:
#             mayor = num1
#             if num2 > num3:
#                 medio = num2
#                 menor = num3
#             else:
#                 medio = num3
#                 menor = num2
#         else:
#             mayor = num3
#             medio = num1
#             menor = num2
#     else:
#         if num2 > num3:
#             mayor = num2
#             if num1 > num3:
#                 medio = num1
#                 menor = num3
#             else:
#                 medio = num3
#                 menor = num1
#         else:
#             mayor = num3
#             medio = num2
#             menor = num1
#     print(f"{menor}, {medio}, {mayor}")


# numero1 = int(input("Ingrese el primer numero: "))
# numero2 = int(input("Ingrese el segundo numero: "))
# numero3 = int(input("Ingrese el tercer numero: "))

# buscar_mayor(numero1, numero2, numero3)

# 5. Definir una función es_par(numero) que reciba un número y devuelva True si es par y False si
# es impar. Luego, el programa debe pedir un número y mostrar si es par o impar usando la función.

# def es_par(numero):
#     if numero % 2 == 0:
#         return True
#     else:
#         return False

# ingreso = int(input("Ingrese un numero: "))
# print(es_par(ingreso))

# 6. Crear una función convertir_minutos(minutos) que reciba una cantidad de minutos y devuelva
# cuántas horas y minutos sobran.

# def convertir_minutos(total_minutos):
#     horas = 0
#     minutos = total_minutos
#     print(f"Inicio: {horas} hora(s), {minutos} minuto(s)")
#     while minutos >= 60:
#         minutos -= 60
#         horas += 1
#     print(f" {total_minutos} minutos son {horas} hora(s) y {minutos} minuto(s)")

# entrada = int(input("Ingrese los minutos: "))
# convertir_minutos(entrada)
# 7. Escribir una función verificar_acceso(edad) que reciba la edad de una persona y determine si
# es mayor de edad (18 años o más) devolviendo un booleano. Luego, el programa debe pedir la
# edad al usuario y mostrar un mensaje apropiado.

def verificar_acceso(edad):
    if edad > 18:
        return True
    else:
        return False


ingreso = int(input("Ingrese tu edad: "))
print(verificar_acceso(ingreso))


# 8. Crear una función llamada calcular_edad(anio_nacimiento) que reciba el año de nacimiento y
# devuelva la edad actual (sin considerar el mes de nacimiento). Luego, el programa debe pedir el
# año de nacimiento del usuario y mostrar la edad calculada.

def calcular_edad(anio_nacimiento):
    edad = 2025 - anio_nacimiento
    print(f"Tu edad es {edad} y nacistes: {anio_nacimiento}")


ingreso = int(input("Ingrese el anio que naciste: "))
calcular_edad(ingreso)