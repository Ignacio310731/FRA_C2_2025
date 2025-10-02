MAX = 10
lista_nombres = [""] * MAX
lista_libros_leidos = [0] * MAX
lista_comentarios = [""] * MAX

def ingresar_datos(nombres, libros, comentarios, cantidad):
    while cantidad < MAX:
        print(f"------ Participante {cantidad + 1} ------")
        nombres[cantidad] = texto("Ingrese nombre: ")
        libros[cantidad] = puntaje("Ingrese puntuación (1-20): ")
        comentarios[cantidad] = texto("Ingrese comentario: ")
        cantidad += 1
        continuar = input("Desea continuar cargando personas? (s/n)").lower()
        if continuar != "s":
            break
    return cantidad

def texto(mensaje):
    texto = ""
    while texto == "":
        texto = input(mensaje)
        if texto == "":
            print("No puede quedar en blanco...!")
    return texto


def puntaje(mensaje):
    while True:
        numero = int(input(mensaje))
        if numero < 1 or numero > 20:
            print("Debe ingresar un número entre 1 y 20!")
        else:
            return numero




def mostrar_datos(nombres, libros, comentarios, cantidad):
    if cantidad == 0:
        print("No hay datos cargados...")
        return
    suma = 0
    for i in range(cantidad):
        print(f"{i + 1}. {nombres[i]} - Libros leidos: {libros[i]} - Comentario: {comentarios[i]}")
        suma += libros[i]
    promedio = suma / cantidad
    print(f"Promedio de libros leidos en total: {promedio}")


def ordenar(nombres, libros, comentarios, cantidad):
    for i in range(cantidad - 1):
        for j in range(cantidad - 1 - i):
            if libros[j] < libros[j + 1]:
                libros[j], libros[j + 1] = libros[j + 1], libros[j]
                nombres[j], nombres[j + 1] = nombres[j + 1], nombres[j]
                comentarios[j], comentarios[j + 1] = comentarios[j + 1], comentarios[j]
    for i in range(cantidad):
        print(f"{i + 1}. {nombres[i]} - Libros leidos: {libros[i]} - Comentario: {comentarios[i]}")


cantidad = 0

while True:
    print("=== MENÚ PRINCIPAL ===")
    print("1. Ingresar datos de participantes")
    print("2. Mostrar los datos de las personas ingresadas")
    print("3. Ordenar participantes (mayor a menor)")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        cantidad = ingresar_datos(lista_nombres, lista_libros_leidos, lista_comentarios, cantidad)
    elif opcion == "2":
        mostrar_datos(lista_nombres, lista_libros_leidos, lista_comentarios, cantidad)
    elif opcion == "3":
        ordenar(lista_nombres, lista_libros_leidos, lista_comentarios, cantidad)
    elif opcion == "4":
        print("Gracias por participar en la encuesta )")
        break
    else:
        print("Opción inválida, intente nuevamente.")