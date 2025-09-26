# #Ejercicio 1: Registro de Temperaturas
# Una estación meteorológica registra las temperaturas diarias de una semana (7 días) en 3 horarios.
# Cargar en una matriz 7x3 las temperaturas (números enteros) y mostrar:
#     El promedio de temperatura de cada día.
#     El promedio general de toda la semana.


matriz = [[10, 12, 15],  # Día 1
    [14, 16, 13],  # Día 2
    [11, 18, 17],  # Día 3
    [20, 19, 22],  # Día 4
    [13, 15, 14],  # Día 5
    [17, 16, 18],  # Día 6
    [19, 21, 20]]   # Día 7

# DIAS = 7
# HORARIOS = 3
# dias = ["Lunes,", "Martes", "Miercoles", "Jueves", "Viernes"]
# for i in range(HORARIOS):
#     print(f"Horario: {i + 1}")
#     for j in range(DIAS):
#         valor_valido = False
#         while valor_valido == False:
#             carga = float(input("Ingrese las temperaturas: "))
#             if carga >= 0:
#                 matriz[i][j] = carga
#                 valor_valido = True
#             else:
#                 print("No se permiten negativos")

suma_total = 0
contador = 0

# Promedio por día
for i in range(7):   # 7 días
    suma = 0
    for j in range(3):   # 3 horarios
        suma += matriz[i][j]      # acumulo para el día
        suma_total += matriz[i][j]  # acumulo para el total
        contador += 1                 # cuento el número
    promedio_dia = suma / 3
    print(f"El promedio del día {i+1} es: {promedio_dia}")

# Promedio general
promedio_general = suma_total / contador
print(f"El promedio general de la semana es: {promedio_general}")

# print(f"{dias[j]}: {matriz[i][j]}")

# #Ejercicio 2: Puntajes de un Torneo
# En un torneo de programación hay 4 equipos que compiten en 5 rondas.
# Cargar en una matriz 4x5 los puntajes obtenidos (enteros). Luego mostrar:
#     El puntaje total de cada equipo.
#     Qué equipo obtuvo el mayor puntaje en total.

# #Ejercicio 3: Control de Producción
# Una fábrica produce 3 productos y mide la producción durante 4 días.
# Cargar en una matriz 3x4 las cantidades producidas. Mostrar:
#     La producción total de cada producto.
#     La producción total de cada día.
#     Cuál fue el día con mayor producción total.