# Práctica Semana 1: Inicio del sistema de gestión del Parque de Diversiones 🎢
# El Parque de Diversiones "PythonLand" necesita un programa inicial para registrar la entrada de visitantes.
# El sistema debe:

# 1. Ingreso de datos secuenciales
# ○ Pedir el nombre y edad de un visitante.
# ○ Pedir cuántas atracciones quiere usar (por ahora, el parque tiene solo 3 atracciones: Montaña
# Rusa, Casa del Terror y Carrusel).
# 2. Uso de condicionales
# ○ Determinar si el visitante puede subir a la Montaña Rusa (solo si tiene 12 años o más).
# ○ Si el visitante tiene menos de 6 años, solo puede subir al Carrusel.
# ○ Los demás pueden acceder a todas las atracciones.
# 3. Uso de ciclos
# ○ Preguntar por cada atracción que el visitante desea usar y mostrar si puede subir o no según
# su edad.
# ○ Calcular el costo total de las entradas (ejemplo: Montaña Rusa = $1500, Casa del Terror =
# $1200, Carrusel = $800).
# 4. Salida de resultados
# ○ Mostrar un resumen con el nombre del visitante, la lista de atracciones que eligió, cuáles pudo
# usar y el costo total a pagar.

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
pregunta = int(input("Cuantas atracciones desear usar? (Hay 3): "))
atracciones = input("Ingrese el tipo de atraccion que quiere usar! (Montaña Rusa, Casa del Terror y Carrusel): ")

costo_entradas = 0
for i in range(pregunta):
    while True:
        if edad >= 12:
            # atracciones = input("Ingrese el tipo de atraccion que quiere usar! (Montaña Rusa, Casa del Terror y Carrusel): ")
            if atracciones == "Montaña":
                costo_entradas += 1500
            elif atracciones == "Casa del Terror":
                costo_entradas += 1200
            else:
                costo_entradas += 800
            break
        elif edad >= 0 and edad <= 6:
                # atracciones = input("Ingrese el tipo de atraccion que quiere usar! (Montaña Rusa, Casa del Terror y Carrusel): ")
                print("Solo podes subirte al Carrusel")
                while atracciones != "Carrusel":
                    costo_entradas += 800
        elif edad > 7:
                # atracciones = input("Ingrese el tipo de atraccion que quiere usar! ( Casa del Terror y Carrusel): ")
                print("Podes Subir al Carrusel, y Casa del Terror!")
                while atracciones != "Casa del Terror" or atracciones != "Carrusel":
                    if atracciones == "Casa del Terror":
                        costo_entradas += 1200
                    elif atracciones == "Carrusel":
                        costo_entradas += 800
    print("----------Factura----------")
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Cantidad de atracciones: {pregunta}")
    print(f"Tipo de Atraccion: {atracciones}")
    print(f"Subtotal: {costo_entradas}")


# if atracciones == "Montaña":
#     costo_entradas += 1500
# elif atracciones == "Casa del Terror":
#     costo_entradas += 1200
# else:
#     costo_entradas += 800









# for i in range(1):



