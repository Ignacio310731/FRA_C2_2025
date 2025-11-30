# funciones_planilla.py
from funciones_dados import *
from funciones_puntaje import *
from funciones_archivos import guardar_puntaje

def inicializar_planilla(nivel):
    planilla = {}
    for clave_categoria in nivel["categorias"]:
        planilla[clave_categoria] = None
    return planilla

def obtener_texto_valor_planilla(valor_categoria):
    if valor_categoria == None:
        return "-"
    else:
        return str(valor_categoria)

def mostrar_planilla(planilla, nivel):
    print("\n--- PLANILLA DE PUNTAJES ---")
    for clave_categoria in nivel["categorias"]:
        nombre_categoria = nivel["categorias"][clave_categoria]
        valor_categoria = planilla[clave_categoria]
        texto_valor = obtener_texto_valor_planilla(valor_categoria)
        print(f"{nombre_categoria}: {texto_valor}")
    print()

def mostrar_categorias_disponibles(planilla, nivel, claves_disponibles):
    print("\nCategorías disponibles:")
    numero_opcion = 1
    for clave_categoria in nivel["categorias"]:
        if planilla[clave_categoria] == None:
            nombre_categoria = nivel["categorias"][clave_categoria]
            print(f"{numero_opcion}) {nombre_categoria}")
            claves_disponibles.append(clave_categoria)
            numero_opcion = numero_opcion + 1

def pedir_opcion_categoria(cantidad_opciones):
    opcion = input("Elegí una categoría: ")
    opcion_valida = False
    while opcion_valida == False:
        if opcion.isdigit():
            numero_elegido = int(opcion)
            if numero_elegido >= 1 and numero_elegido <= cantidad_opciones:
                opcion_valida = True
            else:
                print("Opción inválida.")
                opcion = input("Elegí una categoría: ")
        else:
            print("Opción inválida.")
            opcion = input("Elegí una categoría: ")
    return numero_elegido

def elegir_categoria(planilla, nivel):
    claves_disponibles = []
    mostrar_categorias_disponibles(planilla, nivel, claves_disponibles)
    numero_elegido = pedir_opcion_categoria(len(claves_disponibles))
    indice_categoria = numero_elegido - 1
    return claves_disponibles[indice_categoria]

def sumar_puntaje_total(planilla):
    total = 0
    for clave_categoria in planilla:
        if planilla[clave_categoria] != None:
            total = total + planilla[clave_categoria]
    return total

def jugar_turno(nivel, planilla):
    dados = tirar_cinco_dados()
    cantidad_tiros = 1
    seguir_tirando = True
    while seguir_tirando == True:
        print(f"\n--- Tiro {cantidad_tiros} ---")
        mostrar_dados_tematicos(dados, nivel["caras_dado"])
        if cantidad_tiros == 3:
            seguir_tirando = False
        else:
            respuesta = preguntar_si_vuelve_a_tirar()
            if respuesta == "N":
                seguir_tirando = False
            else:
                posiciones_conservar = pedir_posiciones_conservar()
                dados = generar_nuevos_dados(dados, posiciones_conservar)
                cantidad_tiros = cantidad_tiros + 1
    generala_servida = determinar_generala_servida(cantidad_tiros)
    categoria_elegida = elegir_categoria(planilla, nivel)
    puntaje_obtenido = calcular_puntaje_categoria(categoria_elegida,dados,nivel,generala_servida)
    planilla[categoria_elegida] = puntaje_obtenido
    nombre_categoria = nivel["categorias"][categoria_elegida]
    print(f"Puntaje obtenido en {nombre_categoria}: {puntaje_obtenido}")
    return planilla

def jugar_generala(nivel):
    print("\n--- INICIO DEL PARTIDO ---")
    print(f"Nivel: {nivel['nombre_nivel']}")
    print(f"Puntaje objetivo: {nivel['puntaje_objetivo']} puntos\n")
    planilla = inicializar_planilla(nivel)
    rondas_totales = len(nivel["categorias"])
    ronda_actual = 0
    while ronda_actual < rondas_totales:
        numero_ronda_mostrar = ronda_actual + 1
        print(f"\n===== RONDA {numero_ronda_mostrar} / {rondas_totales} =====")
        mostrar_planilla(planilla, nivel)
        jugar_turno(nivel, planilla)
        ronda_actual = ronda_actual + 1
    mostrar_planilla(planilla, nivel)
    puntaje_total = sumar_puntaje_total(planilla)
    print(f"\nPUNTAJE FINAL: {puntaje_total}")
    print(f"Puntaje objetivo del nivel: {nivel['puntaje_objetivo']}")
    if puntaje_total >= nivel["puntaje_objetivo"]:
        print("¡Ganaste el partido!")
    else:
        print("No llegaste al puntaje objetivo. ¡A entrenar más!")
    nombre_jugador = input("\nIngresá tu nombre para guardar el puntaje: ")
    while nombre_jugador.strip() == "":
        print("El nombre no puede estar vacío.")
        nombre_jugador = input("Ingresá tu nombre para guardar el puntaje: ")
    guardar_puntaje(nombre_jugador, puntaje_total)
    print("Puntaje guardado en el archivo de estadísticas.")
    input("Presioná ENTER para volver al menú...")