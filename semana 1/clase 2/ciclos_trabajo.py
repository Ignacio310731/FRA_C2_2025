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

print("Bienvenido al Parque PythonLand 🎢")

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
pregunta = int(input("¿Cuántas atracciones desea usar? (máx. 3): "))

costo_entradas = 0
lista_atracciones = ""   

for i in range(pregunta):
    atraccion = input("Ingrese el tipo de atracción (Montaña Rusa / Casa del Terror / Carrusel): ")

    if edad >= 12:
        if atraccion == "Montaña Rusa":
            costo_entradas += 1500
            lista_atracciones += "Montaña Rusa ✅\n"
        elif atraccion == "Casa del Terror":
            costo_entradas += 1200
            lista_atracciones += "Casa del Terror ✅\n"
        elif atraccion == "Carrusel":
            costo_entradas += 800
            lista_atracciones += "Carrusel ✅\n"

    elif edad < 6:
        if atraccion != "Carrusel":
            print("⚠️ Solo podés subirte al Carrusel.")
            lista_atracciones += atraccion + " ❌\n"
        else:
            costo_entradas += 800
            lista_atracciones += "Carrusel ✅\n"

    else:
        if atraccion == "Casa del Terror":
            costo_entradas += 1200
            lista_atracciones += "Casa del Terror ✅\n"
        elif atraccion == "Carrusel":
            costo_entradas += 800
            lista_atracciones += "Carrusel ✅\n"
        else:
            print("⚠️ No podés subirte a la Montaña Rusa.")
            lista_atracciones += "Montaña Rusa ❌\n"

print("------------ Factura ------------")
print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print("Atracciones elegidas:")
print(lista_atracciones)
print(f"Subtotal: ${costo_entradas}")
print("Que disfrute de las atracciones!")
print("---------------------------------")



# if atracciones == "Montaña":
#     costo_entradas += 1500
# elif atracciones == "Casa del Terror":
#     costo_entradas += 1200
# else:
#     costo_entradas += 800









# for i in range(1):



