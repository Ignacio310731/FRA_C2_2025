from borrador import *

def menu():
    print("\n--- Biblioteca Escolar ---")
    print("1. Cargar títulos y ejemplares")
    print("2. Mostrar catálogo completo")
    print("3. Consultar disponibilidad de un libro")
    print("4. Listar títulos agotados")
    print("5. Agregar un nuevo título")
    print("6. Actualizar ejemplares (préstamo/devolución)")
    print("7. Salir")
    return input("Elige una opción: ")


def main():
    titulos = [""] * 20
    ejemplares = [0] * 20
    cantidad = 0  
    while True:
        opcion = menu()
        if opcion == "1":
            cantidad = cargar_catalogo(titulos, ejemplares, cantidad)
        elif opcion == "2":
            mostrar_catalogo(titulos, ejemplares, cantidad)
        elif opcion == "3":
            buscado = input("Ingrese el título a consultar: ")
            disponibles = consultar_disponibilidad(titulos, ejemplares, cantidad, buscado)
            if disponibles != -1:
                print(f"'{buscado}' tiene {disponibles} ejemplares.")
            else:
                print("El título no está en el catálogo.")
        elif opcion == "4":
            listar_agotados(titulos, ejemplares, cantidad)
        elif opcion == "5":
            cantidad = agregar_libro(titulos, ejemplares, cantidad)
        elif opcion == "6":
            buscado = input("Ingrese el título a actualizar: ")
            nuevo_valor = int(input("Ingrese el nuevo número de ejemplares: "))
            if actualizar_ejemplares(titulos, ejemplares, cantidad, buscado, nuevo_valor):
                print("Ejemplares actualizados correctamente.")
            else:
                print("No se encontró el título.")
        elif opcion == "7":
            print("Saliendo del sistema... ¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

main()