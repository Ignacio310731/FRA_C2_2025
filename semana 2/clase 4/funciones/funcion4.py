# 4. Crear una función buscar_mayor que reciba tres números y devuelva los tres números
# ordenados de mayor a menor. Luego, el programa debe pedir los números y mostrar los números
# ordenados.

def buscar_mayor(num1, num2, num3):
    mayor = 0
    medio = 0
    menor = 0
    if num1 > num2:
        if num1 > num3:
            mayor = num1
            if num2 > num3:
                medio = num2
                menor = num3
            else:
                medio = num3
                menor = num2
        else:
            mayor = num3
            medio = num1
            menor = num2
    else:
        if num2 > num3:
            mayor = num2
            if num1 > num3:
                medio = num1
                menor = num3
            else:
                medio = num3
                menor = num1
        else:
            mayor = num3
            medio = num2
            menor = num1
    print(f"{mayor}, {medio}, {menor}")


numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
numero3 = int(input("Ingrese el tercer numero: "))

buscar_mayor(numero1, numero2, numero3)