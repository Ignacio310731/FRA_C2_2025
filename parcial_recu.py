# CARGAR MAXIMO 15 PERSONAS(NOMBRE Y APELLIDO), CARGAR PUNTUACION HECHA (ENTRE 1 AL 50) Y COMENTARIOS,
#  EL NOMBRE NO PUEDE ESTAR EN BLANCO,
# ORDENAR DE MAYOR A MENOR, EL PROMEDIO
MAX = 10
lista_personas = [""] * MAX
lista_puntuacion = [0] * MAX
lista_comentarios = [""] * MAX

def ingresa_texto(mensaje):
    texto = ""
    while texto == "" or texto == " ":
        texto = input(mensaje)
        if texto == "" or texto == " ":
            texto = print("No puede quedar en blanco...")
    return texto

def ingresar_puntaje(mensaje):
    while True:
        numero = int(input(mensaje))
        if 1 <= numero <= 10:
            return numero
        else:
            print("Debe ingresar un número entre 1 y 10")



def ingresar_datos(nombres, puntajes, comentarios, cantidad):
    while cantidad < MAX:
        print(f"--------Persona {cantidad + 1}---------")
        nombres[cantidad] = ingresa_texto("Ingrese su nombre y apellido: ")
        puntajes[cantidad] = ingresar_puntaje("Ingrese su puntaje de desempeño(entre 0-10): ")
        comentarios[cantidad] = ingresa_texto("Ingrese un comentario del supervisor: ")
        cantidad += 1
        ingresar = input("Deseas ingresar otra persona? (s/n): ").lower()
        if ingresar != "s":
            break
    return cantidad

def mostrar_datos(persona,puntaje,comentario,cantidad):
    if cantidad == 0:
        print("No se cargaron datos...")
        return
    suma = 0
    for i in range(cantidad):
        print(f"{i + 1}.   {persona}:Nombre de Persona, {puntaje}: Puntaje obtenido, {comentario}: Comentario")
        suma += puntaje[i]
    promedio = suma / cantidad
    print(f"El promedio de los puntajes de desempeño obtuvidos fue de: {promedio}")
    return promedio

def ordenar_por_puntaje(persona, puntaje, comentario, cantidad):
    for i in range(cantidad - 1):
        for j in range(cantidad - 1 - i):
            if puntaje[j] > puntaje[j + 1]:
                puntaje[j], puntaje[j + 1] = puntaje[j + 1], puntaje[j]
                persona[j], persona[j + 1] = persona[j + 1], persona[j]
                comentario[j], comentario[j + 1] = comentario[j + 1], comentario[j]
                for i in range(cantidad):
                    print(f"{i + 1}.   {persona}:Nombre de Persona, {puntaje}: Puntaje obtenido, {comentario}: Comentario")

cantidad = 0

while True:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Ingresar datos de participantes")
    print("2. Mostrar todas las puntuaciones y comentarios")
    print("3. Ordenar participantes por puntuación (Bubble Sort)")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        cantidad = ingresar_datos(lista_personas, lista_puntuacion, lista_comentarios, cantidad)
    elif opcion == "2":
        mostrar_datos(lista_personas, lista_puntuacion, lista_comentarios, cantidad)
        pass
    elif opcion == "3":
        ordenar_por_puntaje(lista_personas, lista_puntuacion, lista_comentarios, cantidad)
        pass
    elif opcion == "4":
        print("Gracias por participar en la encuesta )")
        break
    else:
        print("Opción inválida, intente nuevamente.")














