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
