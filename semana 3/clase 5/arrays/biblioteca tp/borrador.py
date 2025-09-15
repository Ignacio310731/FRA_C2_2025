# Una biblioteca escolar necesita un pequeño sistema de gestión para su catálogo de libros.
# Se deben usar listas estáticas con un máximo de 20 títulos y sus respectivos ejemplares.
# Requerimientos:
# 1. Usar dos listas paralelas:
# 1. titulos[] → nombres de los libros.
# 2. ejemplares[] → cantidad de copias disponibles.
# Cada índice representa el mismo libro en ambas listas.
# 2. Implementar un menú de opciones utilizando un bucle while que se repita hasta que el usuario elija
# Salir.
# 3. Opciones del menú:
# 1. Cargar títulos y ejemplares
# Permitir al usuario ingresar hasta 20 títulos y la cantidad de ejemplares para cada uno.
# 2. Mostrar catálogo completo
# Listar cada título con su número de ejemplares.
# Ejemplo: El Señor de los Anillos → 5 copias
# 3. Consultar disponibilidad
# Pedir al usuario un título y mostrar cuántas copias tiene.
# 4. Listar títulos agotados
# Mostrar solo aquellos títulos que tengan 0 copias.
# 5. Agregar un nuevo título
# Permitir al usuario agregar un nuevo libro y su cantidad de ejemplares si no se superó el máximo
# de 20.
# 6. Actualizar ejemplares (préstamo / devolución)
# Permitir al usuario modificar el número de ejemplares de un libro existente.
# 7. Salir
# Ejemplo de listas paralelas:
# titulos = ["El Señor de los Anillos", "Orgullo y Prejuicio", "Matar un Ruiseñor"]
# ejemplares = [5, 3, 7]
# Puntos clave:
# ● Usar listas estáticas de tamaño fijo ([""] * 20 y [0] * 20).
# ● Manejar correctamente los índices para mantener sincronizados títulos y ejemplares.
# ● Evitar sobrepasar el límite de 20 elementos.
# ● Modularizar usando funciones para cada opción del menú.



def cargar_catalogo(titulos, ejemplares, cantidad):
    while cantidad < len(titulos):
        titulo = input("Ingrese el título del libro: ")
        copias = int(input("Ingrese la cantidad de ejemplares: "))

        titulos[cantidad] = titulo
        ejemplares[cantidad] = copias
        cantidad += 1

        seguir = input("¿Desea cargar otro libro? (si/no): ")
        if seguir == "no":
            break
    return cantidad


def mostrar_catalogo(titulos, ejemplares, cantidad):
    if cantidad == 0:
        print("No hay libros cargados.")
    else:
        for i in range(cantidad):
            print(f"{titulos[i]} → {ejemplares[i]} copias")


def consultar_disponibilidad(titulos, ejemplares, cantidad, buscado):
    for i in range(cantidad):
        if titulos[i] == buscado:
            return ejemplares[i]
    return -1


def listar_agotados(titulos, ejemplares, cantidad):
    agotados = False
    for i in range(cantidad):
        if ejemplares[i] == 0:
            print(f"{titulos[i]} está agotado.")
            agotados = True
        else:
            print("No hay libros agotados.")


def agregar_libro(titulos, ejemplares, cantidad):
    if cantidad >= len(titulos):
        print("No se pueden agregar más libros, el catálogo está lleno.")
        return cantidad
    titulo = input("Ingrese el nuevo título: ")
    copias= int(input("Ingrese la cantidad de ejemplares: "))
    titulos[cantidad] = titulo
    ejemplares[cantidad] = copias
    cantidad += 1
    return cantidad


def actualizar_ejemplares(titulos, ejemplares, cantidad, buscado, nuevo_valor):
    for i in range(cantidad):
        if titulos[i] == buscado:
            ejemplares[i] = nuevo_valor
            return True
    return False