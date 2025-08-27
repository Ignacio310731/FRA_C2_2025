# 2. Escribir una función operaciones(num1, num2) que reciba dos números y muestre su suma,
# resta y multiplicación. Luego, el programa debe pedir dos números al usuario y llamar a la
# función.

def operaciones(num1, num2):
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    print(f"La suma es {suma}\n La resta es {resta} \n La multiplicacion {multiplicacion} ")
    # return suma, resta, multiplicacion

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
operaciones(numero1, numero2)