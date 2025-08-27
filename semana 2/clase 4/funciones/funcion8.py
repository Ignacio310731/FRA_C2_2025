# 8. Crear una función llamada calcular_edad(anio_nacimiento) que reciba el año de nacimiento y
# devuelva la edad actual (sin considerar el mes de nacimiento). Luego, el programa debe pedir el
# año de nacimiento del usuario y mostrar la edad calculada.

def calcular_edad(anio_nacimiento):
    edad = 2025 - anio_nacimiento
    print(f"Tu edad es {edad} y naciste en {anio_nacimiento}")


ingreso = int(input("Ingrese el anio que naciste: "))
calcular_edad(ingreso)