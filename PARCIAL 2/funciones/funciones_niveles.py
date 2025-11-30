def mostrar_niveles(lista_niveles):
    print("\n--- SELECCIÓN DE NIVEL ---")
    cantidad_niveles = len(lista_niveles)
    indice_nivel = 0
    while indice_nivel < cantidad_niveles:
        nivel_actual = lista_niveles[indice_nivel]
        numero_mostrar = indice_nivel + 1
        print(f"[{numero_mostrar}] {nivel_actual['nombre_nivel']}")
        indice_nivel = indice_nivel + 1

def pedir_opcion_nivel(cantidad_niveles):
    opcion = input("Elegí un nivel: ")
    opcion_valida = False
    while opcion_valida == False:
        if opcion.isdigit():
            numero_opcion = int(opcion)
            if numero_opcion >= 1 and numero_opcion <= cantidad_niveles:
                opcion_valida = True
            else:
                print("Opción inválida.")
                opcion = input("Elegí un nivel: ")
        else:
            print("Opción inválida.")
            opcion = input("Elegí un nivel: ")
    return numero_opcion


def seleccionar_nivel(lista_niveles):
    cantidad_niveles = len(lista_niveles)
    if cantidad_niveles == 1:
        return lista_niveles[0]
    mostrar_niveles(lista_niveles)
    numero_opcion = pedir_opcion_nivel(cantidad_niveles)
    indice_elegido = numero_opcion - 1
    return lista_niveles[indice_elegido]
