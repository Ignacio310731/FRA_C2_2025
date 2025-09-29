MAX = 10
lista_nombres = [""] * MAX
lista_puntajes = [0] * MAX
lista_comentarios = [""] * MAX


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


def ingresar_datos(nombres, puntajes, comentarios, cantidad):
    while cantidad < MAX:
        print(f"------ Participante {nombres + 1} ------")
        nombres[cantidad] = texto("Ingrese nombre: ")
        puntajes[cantidad] = puntaje("Ingrese puntuación (1-20): ")
        comentarios[cantidad] = texto("Ingrese comentario: ")
        cantidad += 1
        continuar = input("Desea continuar cargando personas? (s/n)").lower()
        if continuar != "s":
            break
    return cantidad


def mostrar_datos(nombres, puntajes, comentarios, cantidad):
    if cantidad == 0:
        print("No hay datos cargados...")
        return
    suma = 0
    for i in range(cantidad):
        print(f"{i + 1}. {nombres[i]} - Puntaje: {puntajes[i]} - Comentario: {comentarios[i]}")
        suma += puntajes[i]
    promedio = suma / cantidad
    print(f"Promedio de puntaje total: {promedio}")


def ordenar_por_puntaje(nombres, puntajes, comentarios, cantidad):
    for i in range(cantidad - 1):
        for j in range(cantidad - 1 - i):
            if puntajes[j] < puntajes[j + 1]:
                puntajes[j], puntajes[j + 1] = puntajes[j + 1], puntajes[j]
                nombres[j], nombres[j + 1] = nombres[j + 1], nombres[j]
                comentarios[j], comentarios[j + 1] = comentarios[j + 1], comentarios[j]
    for i in range(cantidad):
        print(f"{i + 1}. {nombres[i]} - Puntaje: {puntajes[i]} - Comentario: {comentarios[i]}")


cantidad = 0

while True:
    print("=== MENÚ PRINCIPAL ===")
    print("1. Ingresar datos de participantes")
    print("2. Mostrar todas las puntuaciones y comentarios")
    print("3. Ordenar participantes por puntuación")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        cantidad = ingresar_datos(lista_nombres, lista_puntajes, lista_comentarios, cantidad)
    elif opcion == "2":
        mostrar_datos(lista_nombres, lista_puntajes, lista_comentarios, cantidad)
    elif opcion == "3":
        ordenar_por_puntaje(lista_nombres, lista_puntajes, lista_comentarios, cantidad)
    elif opcion == "4":
        print("Gracias por participar en la encuesta )")
        break
    else:
        print("Opción inválida, intente nuevamente.")