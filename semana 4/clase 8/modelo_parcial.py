MAX = 10
lista_nombres = [""] * MAX
lista_puntaje = [0] * MAX
lista_comentario = [""] * MAX

def ingresar_personas(lista_nombres, lista_puntaje, lista_comentario):
    acumulador = 0
    suma = 0
    for i in range(len(lista_nombres)):
        pregunta = input("¿Desea cargar un nuevo participante? (s/n):").lower()
        if pregunta == "s":
            while True:
                nombres = input("Ingrese un nombre: ")
                if nombres == "" or nombres == " ":
                    print("Error, ingrese de vuelta")
                else:
                    break
            while True:
                puntaje = int(input("Ingrese el puntaje obtenido: "))
                if puntaje <= 0 or puntaje > 10:
                    print("Es del 1 al 10!\n Volver a ingresar...")
                else:
                    suma += puntaje
                    break
            while True:
                comentario = input("Dejanos tu comentario!: ")
                if comentario == "" or comentario == " ":
                    print("Que no quede en blanco!!")
                else:
                    break
            acumulador += 1
        else:
            break
        lista_nombres[i] = nombres
        lista_puntaje[i] = puntaje
        lista_comentario[i] = comentario
    return lista_nombres, lista_puntaje, lista_comentario, acumulador, suma

def ordenar(lista_nombres, lista_puntaje, lista_comentario):
    n = len(lista_puntaje)
    for i in range(n):
        for j in range(0, n-1-i):
            if lista_puntaje[j] < lista_puntaje[j+1]:
                lista_puntaje[j], lista_puntaje[j+1] = lista_puntaje[j+1], lista_puntaje[j]
                lista_comentario[j], lista_comentario[j+1] = lista_comentario[j+1], lista_comentario[j]
                lista_nombres[j], lista_nombres[j+1] = lista_nombres[j+1], lista_nombres[j]
    return lista_nombres, lista_puntaje, lista_comentario

def mostrar_promedio(suma,acumulador):
    if acumulador == 0:
        return 0
    return suma / acumulador



print(lista_nombres)
print(lista_puntaje)
print(lista_comentario)
while True:
    print("--- Menú Encuesta de Satisfacción ---")
    print("1. Ingresar participantes")
    print("2. Mostrar participantes y promedio")
    print("3. Ordenar participantes por puntuación")
    print("4. Salir")
    seleccion = input("Seleccione una opción (1-4): ")
    if seleccion == "1":
        lista_nombres, lista_puntaje, lista_comentario, acumulador, suma = ingresar_personas(lista_nombres, lista_puntaje, lista_comentario)
    elif seleccion == "2":
        print("Nombres:", lista_nombres[:acumulador])
        print("Puntajes:", lista_puntaje[:acumulador])
        print("Comentarios:", lista_comentario[:acumulador])
    elif seleccion == "3":
        lista_nombres, lista_puntaje, lista_comentario = ordenar(lista_nombres, lista_puntaje, lista_comentario)
        print("Participantes ordenados de mayor a menor puntaje:")
        print("Nombres:", lista_nombres[:acumulador])
        print("Puntajes:", lista_puntaje[:acumulador])
        print("Comentarios:", lista_comentario[:acumulador])
    elif seleccion == "4":
        break
    else:
        print("Opción inválida. Intente nuevamente.")