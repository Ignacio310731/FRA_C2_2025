# !1) pedir 5 personas
# 2) mostrar los datos
# 3) ordenar de forma ascendente
# 4) salir
MAX = 5
lista_persona = [""] * MAX
lista_compras = [0] * MAX
lista_comentarios = [""] * MAX
def datos_ingreso(personas,compras, comentarios, cantidad):
    while cantidad < MAX:
        print(f"Persona {cantidad + 1}")
        personas[cantidad] = persona_cometario("Ingrese el nombre: ")
        compras[cantidad] = cantidad_compras("Cuantas cosas compraste: ")
        comentarios[cantidad] = persona_cometario("Ingrese el comentario: ")
        cantidad += 1
        pregunta = input("Deseas seguir? s/n: ").lower()
        if pregunta != "s":
            break
    return cantidad



def persona_cometario(mensaje):
    texto = ""
    while True:
        texto = input(mensaje)
        if texto == "":
            print("No se puede dejar en blanco...")
        else:
            break
    return texto

def cantidad_compras(mensaje):
    compra = 0
    while True:
        compra = int(input(mensaje))
        if compra < 1 or compra > 50:
            print("Es entre 1 y 50!!\n Volver a ingresar...")
        else:
            break
    return compra


def mostrar_datos(personas, compras, comentarios, cantidad):
    if cantidad == 0:
        print("No se ingresaron datos...\n Ingresa la opcion 1!")
        return
    suma = 0 
    for i in range(cantidad):
        print(f"{i + 1}- Persona - {personas[i]}- Compra - {compras[i]}- Comentario - {comentarios[i]}")
        suma += compras[i]
    promedio = suma / cantidad
    print(f"EL promedio total es de: {promedio:.2f}")

def ordenar_menor(personas, compras, comentarios, cantidad):
    for i in range(cantidad -1):
        for j in range(cantidad -1 - i):
            if compras[j] > compras[j+1]:
                compras[j], compras[j+1] = compras[j+1], compras[j]
                personas[j], personas[j+1] = personas[j+1], personas[j]
                comentarios[j], comentarios[j+1] = comentarios[j+1], comentarios[j]
    for i in range(cantidad):
        print(f"{i + 1}- Persona - {personas[i]}- Compra - {compras[i]}- Comentario - {comentarios[i]}")

def ordenar_mayor(personas, compras, comentarios, cantidad):
    for i in range(cantidad -1):
        for j in range(cantidad -1 - i):
            if compras[j] < compras[j+1]:
                compras[j], compras[j+1] = compras[j+1], compras[j]
                personas[j], personas[j+1] = personas[j+1], personas[j]
                comentarios[j], comentarios[j+1] = comentarios[j+1], comentarios[j]
    for i in range(cantidad):
        print(f"{i + 1}- Persona - {personas[i]}- Compra - {compras[i]}- Comentario - {comentarios[i]}")




cantidad = 0

while True:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Ingresar datos de participantes")
    print("2. Mostrar todas las puntuaciones y comentarios")
    print("3. Ordenar participantes por puntuación (mayor) (Bubble Sort)")
    print("4. Ordenar participantes por puntuación (menor) (Bubble Sort)")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        cantidad = datos_ingreso(lista_persona,lista_compras,lista_comentarios,cantidad)
    elif opcion == "2":
        mostrar_datos(lista_persona, lista_compras, lista_comentarios, cantidad)
    elif opcion == "3":
        ordenar_mayor(lista_persona, lista_compras, lista_comentarios, cantidad)
    elif opcion == "4":
        ordenar_menor(lista_persona, lista_compras, lista_comentarios, cantidad)
    elif opcion == "5":
        print("Gracias por participar en la encuesta )")
        break
    else:
        print("Opción inválida, intente nuevamente.")
