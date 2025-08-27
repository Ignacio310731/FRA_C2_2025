# 6. Crear una función convertir_minutos(minutos) que reciba una cantidad de minutos y devuelva
# cuántas horas y minutos sobran.

def convertir_minutos(total_minutos):
    horas = 0
    minutos = total_minutos
    print(f"Inicio: {horas} hora(s), {minutos} minuto(s)")
    while minutos >= 60:
        minutos -= 60
        horas += 1
    print(f" {total_minutos} minutos son {horas} hora(s) y {minutos} minuto(s)")

entrada = int(input("Ingrese los minutos: "))
convertir_minutos(entrada)