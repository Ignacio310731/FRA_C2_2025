# main.py
from funciones_archivos import cargar_niveles, mostrar_estadisticas
from funciones_planilla import jugar_generala
from funciones_niveles import seleccionar_nivel

def pedir_opcion_menu():
    print("\n===== GENERALA FUTBOLERA =====")
    print("1) Jugar")
    print("2) Estadísticas")
    print("3) Créditos")
    print("4) Salir")
    opcion = input("Elegí una opción (1-4): ")
    while opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4":
        print("Opción inválida, intentá de nuevo.")
        opcion = input("Elegí una opción (1-4): ")
    return opcion

def mostrar_creditos():
    print("\n--- CRÉDITOS ---")
    print("Generala Futbolera - Versión Consola")
    print("Autor/a: [Ignacio Andrada y Roman Bustamante]")
    print("Materia: Programación I - Tecnicatura Universitaria en Programación")
    print("Docente: [Martin Alejandro Garcia]")
    print("Año: 2025")
    print("Contacto: nacho2007clubtucuman@gmail.com")
    print("-----------------\n")

lista_niveles = cargar_niveles()
salir = False

while salir == False:
    opcion = pedir_opcion_menu()
    if opcion == "1":
        nivel_elegido = seleccionar_nivel(lista_niveles)
        jugar_generala(nivel_elegido)
    elif opcion == "2":
        mostrar_estadisticas()
    elif opcion == "3":
        mostrar_creditos()
    elif opcion == "4":
        print("\nGracias por jugar a la Generala Futbolera. ¡Nos vemos!")
        salir = True
