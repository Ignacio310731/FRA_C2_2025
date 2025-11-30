# 7. Invertir orden:
# Cargar un array de 6 enteros y mostrarlo invertido, es decir, desde el último al primero.

lista = [1,2,3,4,5,6]

for i in range(len(lista)-1,-1,-1):
    print(lista[i], end= " ")