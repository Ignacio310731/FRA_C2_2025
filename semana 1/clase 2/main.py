from gestion_parque import parque 



def main():
    nombre, edad = parque.registrar_visitante()
    atracciones, total = parque.mostrar_atracciones()
    parque.resumen(nombre, edad, atracciones, total)

main()