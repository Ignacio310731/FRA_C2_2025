# A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el programa deberá determinar la posición del jugador en la cancha, considerando los siguientes parámetros:
# Menos de 160 cm: Base
# Entre 160 cm y 179 cm: Escolta
# Entre 180 cm y 199 cm: Alero
# 200 cm o más: Ala-Pívot o Pívot

altura = int(input("Ingrese su altura (en cm): "))
if altura > 0:
    if altura < 160:
        print(f"Tu altura es: {altura} y Sos Base")
    elif altura <= 179:
        print(f"Tu altura es: {altura} y Sos Escolta")
    elif altura <= 199:
        print(f"Tu altura es: {altura} y Sos Alero")
    else:
        print(f"Tu altura es: {altura} y Sos Ala-Pívot")
else:
    print("Numero invalido...")







# Calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un mensaje según el valor:
# 6, 7, 8, 9 y 10  ---> Promoción directa, la nota es ...
# 4 y 5                ---> Aprobado, la nota es ...
# 1, 2 y 3            ---> Desaprobado, la nota es ...

import random
primer_numero = random.randint(1,10)
if primer_numero >= 6:
    print(f"Promocion directa, tu nota es: {primer_numero}")
elif primer_numero >= 4:
    print(f"Aprobado, tu nota es: {primer_numero}")
else:
    print(f"Desaprobado, tu nota es: {primer_numero}")




