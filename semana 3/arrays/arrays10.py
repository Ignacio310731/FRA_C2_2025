# 10. Función para buscar la primera aparición de un valor:
# Escribir una función que reciba un array de enteros y un número a buscar. La función debe retornar
# la posición de la primera aparición de ese número o -1 si no se encuentra.

def array(vector, numero):
    for i in range(len(vector)):
        if vector[i] == numero:
            return i
    return -1
lista = [1,2,3,4,5]
print(array(lista,1))
print(array(lista,4))

