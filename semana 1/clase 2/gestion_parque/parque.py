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

# --------------------parte 2-----------------------
# 1. Refactorización en funciones
# ● Crear funciones para:
# ○ mostrar_atracciones() → muestra el menú de atracciones.
# ○ puede_subir(edad, atraccion) → devuelve True/False según si puede acceder a la atracción.
# ○ calcular_precio(atraccion) → devuelve el precio de la atracción.
# ○ registrar_visita() → pide datos del visitante, procesa las atracciones elegidas y retorna el
# resumen.
# ○ mostrar_resumen(resumen) → imprime en pantalla la información del visitante.
# 2. Modularización
# ● Guardar el código en dos archivos:
# ○ main.py (ejecución principal).
# ○ parque.py (donde van las funciones).
# 3. Paquete
# ● Crear un paquete llamado gestion_parque y dentro incluir parque.py.
# ● El main.py debe importar desde el paquete.
# 4. Colores con colorama
# ● Instalar un entorno virtual con venv.
# ● Instalar la librería colorama.
# ● Usar colores en la salida (ejemplo: mensajes de error en rojo, éxito en verde, menú en amarillo).
# 5. Nueva funcionalidad
# ● Agregar la opción de calcular un descuento del 10% si el visitante compra 3 o más atracciones.


def registrar_visitante():
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    return nombre, edad



def mostrar_atracciones():
    print("Bienvenido al Parque PythonLand 🎢")
    print("Atracciones disponibles:")
    print("1. Montaña Rusa - $1500")
    print("2. Casa del Terror - $1200")
    print("3. Carrusel - $800")
    cantidad = int(input("¿Cuántas atracciones desea usar? (máx. 3): "))
    atracciones_texto = ""
    monto_total = 0
    for i in range(cantidad):
        print(f"Atracción {i+1}:")
        opcion = int(input("Ingrese el número de atracción (1, 2 o 3): "))
        if opcion == 1:
            atracciones_texto += "Montaña Rusa "
            monto_total += 1500
        elif opcion == 2:
            atracciones_texto += "Casa del Terror "
            monto_total += 1200
        elif opcion == 3:
            atracciones_texto += "Carrusel "
            monto_total += 800
        else:
            print("Opción inválida, no se suma nada.")
    return atracciones_texto, monto_total

def puede_subir(edad, atraccion):
    if atraccion == "Montaña Rusa":
        return edad > 12
    elif atraccion == "Casa del Terror":
        return edad >= 6
    elif atraccion == "Carrusel":
        return True
    else:
        return False

def resumen (nombre,edad,lista_atracciones,costo_entradas):
    print("------------ Factura ------------")
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print("Atracciones elegidas:")
    print(lista_atracciones)
    print(f"Subtotal: ${costo_entradas}")
    print("Que disfrute de las atracciones!")
    print("---------------------------------")



# def mostrar_atracciones():
#     print("Bienvenido al Parque PythonLand 🎢")
#     print("Tipos de Atracciones: Montaña Rusa %1500\n Casa del Terror %1200\n y Carrusel $800")
#     pregunta = int(input("¿Cuántas atracciones desea usar? (máx. 3): "))
#     lista_atracciones = ""   
#     for i in range(pregunta):
#         atraccion = input("Ingrese el tipo de atracción (Montaña Rusa / Casa del Terror / Carrusel): ")
        # lista_atracciones += atraccion
#     return lista_atracciones





# def calcular_precio(atraccion):
#     monto = 0
#     if atraccion == "Montaña Rusa":
#         monto += 1500
#     elif atraccion == "Casa del Terror":
#         monto += 1200
#     else:
#         monto += 800

# def cunatas_preguntas_hace(numero):
    # costo_entradas = 0
        # if edad >= 12:
        #     if atraccion == "Montaña Rusa":
        #         costo_entradas += 1500
        #         lista_atracciones += "Montaña Rusa ✅\n"
        #     elif atraccion == "Casa del Terror":
        #         costo_entradas += 1200
        #         lista_atracciones += "Casa del Terror ✅\n"
        #     elif atraccion == "Carrusel":
        #         costo_entradas += 800
        #         lista_atracciones += "Carrusel ✅\n"
        # elif edad < 6:
        #     if atraccion != "Carrusel":
        #         print("⚠️ Solo podés subirte al Carrusel.")
        #         lista_atracciones += atraccion + " ❌\n"
        #     else:
        #         costo_entradas += 800
        #         lista_atracciones += "Carrusel ✅\n"
        # else:
        #     if atraccion == "Casa del Terror":
        #         costo_entradas += 1200
        #         lista_atracciones += "Casa del Terror ✅\n"
        #     elif atraccion == "Carrusel":
        #         costo_entradas += 800
        #         lista_atracciones += "Carrusel ✅\n"
        #     else:
        #         print("⚠️ No podés subirte a la Montaña Rusa.")
        #         lista_atracciones += "Montaña Rusa ❌\n"










