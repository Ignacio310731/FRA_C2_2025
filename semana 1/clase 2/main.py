from gestion_parque import parque 


# def mostrar_todo():
#     parque.registrar_visitante()
#     print(parque.mostrar_atracciones())
#     parque.puede_subir(parque.registrar_visitante(), parque.mostra_atracciones())
#     parque.calcular_precio(parque.mostrar_atracciones)
#     print(parque.resumen(parque.registrar_visitante),(parque.mostrar_atracciones),parque.mostrar_atracciones)

# print(mostrar_todo())


def main():
    resumen = parque.registrar_visita()
    parque.mostrar_resumen(resumen)

main()
