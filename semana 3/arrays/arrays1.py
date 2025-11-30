#  Cargar y mostrar array:
# Declarar un array de 5 enteros. Cargarlo por teclado y mostrar su contenido por pantalla usando un
# ciclo for.

lista = [0] * 5

for i in range(len(lista)):
    numeros = int(input("Ingrese numeros: "))
    lista[i] += numeros
    print(lista)