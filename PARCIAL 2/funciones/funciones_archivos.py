# funciones_archivos.py
import json
import csv
import os

RUTA_NIVELES = "niveles.json"
RUTA_PUNTAJES = "puntajes.csv"


def cargar_niveles():
    with open(RUTA_NIVELES, "r", encoding="utf-8") as archivo:
        niveles = json.load(archivo)
    return niveles


def ordenar_puntajes_desc(lista_puntajes):
    i = 0
    while i < len(lista_puntajes) - 1:
        j = 0
        while j < len(lista_puntajes) - 1 - i:
            if lista_puntajes[j][1] < lista_puntajes[j + 1][1]:
                auxiliar = lista_puntajes[j]
                lista_puntajes[j] = lista_puntajes[j + 1]
                lista_puntajes[j + 1] = auxiliar
            j = j + 1
        i = i + 1
    return lista_puntajes


def mostrar_estadisticas():
    if os.path.exists(RUTA_PUNTAJES) == False:
        print("\nNo hay estadísticas todavía. ¡Jugá una partida primero!")
        return

    print("\n--- TOP 10 PUNTAJES ---")
    lista_puntajes = []

    with open(RUTA_PUNTAJES, "r", encoding="utf-8", newline="") as archivo:
        lector = csv.reader(archivo, delimiter=";")
        for fila in lector:
            if len(fila) == 2 and fila[1].isdigit():
                nombre_jugador = fila[0]
                puntaje = int(fila[1])
                lista_puntajes.append((nombre_jugador, puntaje))

    if len(lista_puntajes) == 0:
        print("No hay puntajes cargados.")
        return

    lista_puntajes = ordenar_puntajes_desc(lista_puntajes)

    tope = 10
    if len(lista_puntajes) < 10:
        tope = len(lista_puntajes)

    indice_mostrar = 0
    while indice_mostrar < tope:
        nombre_jugador, puntaje = lista_puntajes[indice_mostrar]
        posicion = indice_mostrar + 1
        print(f"{posicion}. {nombre_jugador} - {puntaje} puntos")
        indice_mostrar = indice_mostrar + 1


def guardar_puntaje(nombre_jugador, puntaje):
    with open(RUTA_PUNTAJES, "a", encoding="utf-8", newline="") as archivo:
        escritor = csv.writer(archivo, delimiter=";")
        escritor.writerow([nombre_jugador, puntaje])
