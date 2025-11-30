# funciones_dados.py
import random


def tirar_cinco_dados():
    dados = []
    indice_dado = 0
    while indice_dado < 5:
        numero_aleatorio = random.randint(1, 6)
        dados.append(numero_aleatorio)
        indice_dado = indice_dado + 1
    return dados

def mostrar_cabecera_posiciones():
    print("Posición:  ", end="")
    indice_posicion = 0
    while indice_posicion < 5:
        numero_posicion = indice_posicion + 1
        print(f"({numero_posicion})\t", end="")
        indice_posicion = indice_posicion + 1
    print()

def mostrar_fila_numeros(lista_dados):
    print("Número:    ", end="")
    for valor_dado in lista_dados:
        print(f"{valor_dado}\t", end="")
    print()

def mostrar_fila_simbolos(lista_dados, lista_caras_dado):
    print("Símbolo:   ", end="")
    for valor_dado in lista_dados:
        simbolo = lista_caras_dado[valor_dado - 1]
        print(f"{simbolo}\t", end="")
    print()

def mostrar_dados_tematicos(lista_dados, lista_caras_dado):
    print("\n--- DADOS ACTUALES ---")
    mostrar_cabecera_posiciones()
    mostrar_fila_numeros(lista_dados)
    mostrar_fila_simbolos(lista_dados, lista_caras_dado)

def esta_en_lista(numero, lista):
    indice = 0
    while indice < len(lista):
        if lista[indice] == numero:
            return True
        indice = indice + 1
    return False

def posiciones_son_validas(partes):
    posiciones = []
    indice_parte = 0
    posiciones_validas = True
    while indice_parte < len(partes):
        parte_actual = partes[indice_parte]
        if parte_actual.isdigit():
            numero_posicion = int(parte_actual)
            if numero_posicion >= 1 and numero_posicion <= 5:
                if esta_en_lista(numero_posicion, posiciones) == False:
                    posiciones.append(numero_posicion)
            else:
                posiciones_validas = False
        else:
            posiciones_validas = False
        indice_parte = indice_parte + 1
    return posiciones_validas, posiciones

def pedir_posiciones_conservar():
    texto = input("Ingresá las posiciones de los dados que querés conservar (ej: 1 3 5) o ENTER para tirar todos de nuevo: ")
    if texto == "":
        return []
    partes = texto.split()
    posiciones_validas = False
    while posiciones_validas == False:
        posiciones_validas, posiciones = posiciones_son_validas(partes)
        if posiciones_validas == False:
            print("Entrada inválida. Deben ser números del 1 al 5 separados por espacio.")
            texto = input("Ingresá las posiciones de los dados que querés conservar (ej: 1 3 5) o ENTER para tirar todos: ")
            if texto == "":
                return []
            partes = texto.split()
    return posiciones

def preguntar_si_vuelve_a_tirar():
    respuesta = input("¿Querés volver a tirar algunos dados? (S/N): ")
    respuesta = respuesta.upper()
    while respuesta != "S" and respuesta != "N":
        print("Respuesta inválida.")
        respuesta = input("¿Querés volver a tirar algunos dados? (S/N): ")
        respuesta = respuesta.upper()
    return respuesta

def generar_nuevos_dados(dados_actuales, posiciones_conservar):
    nuevos_dados = []
    indice_dado = 0
    while indice_dado < 5:
        posicion_actual = indice_dado + 1
        if posicion_actual in posiciones_conservar:
            nuevos_dados.append(dados_actuales[indice_dado])
        else:
            nuevos_dados.append(random.randint(1, 6))
        indice_dado = indice_dado + 1
    return nuevos_dados
