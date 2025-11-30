def contar_valores(lista_dados):
    conteos = [0, 0, 0, 0, 0, 0, 0]
    for valor_dado in lista_dados:
        conteos[valor_dado] = conteos[valor_dado] + 1
    return conteos

def sumar_por_valor(lista_dados, valor_buscado):
    suma = 0
    for valor_dado in lista_dados:
        if valor_dado == valor_buscado:
            suma = suma + valor_buscado
    return suma

def ordenar_lista(lista_original):
    lista_ordenada = lista_original[:]
    indice_externo = 0
    while indice_externo < len(lista_ordenada) - 1:
        indice_interno = 0
        while indice_interno < len(lista_ordenada) - 1 - indice_externo:
            if lista_ordenada[indice_interno] > lista_ordenada[indice_interno + 1]:
                auxiliar = lista_ordenada[indice_interno]
                lista_ordenada[indice_interno] = lista_ordenada[indice_interno + 1]
                lista_ordenada[indice_interno + 1] = auxiliar
            indice_interno = indice_interno + 1
        indice_externo = indice_externo + 1
    return lista_ordenada

def es_escalera(lista_dados):
    dados_ordenados = ordenar_lista(lista_dados)
    if dados_ordenados == [1, 2, 3, 4, 5] or dados_ordenados == [2, 3, 4, 5, 6]:
        return True
    else:
        return False

def es_full(conteos):
    hay_tres_iguales = False
    hay_dos_iguales = False
    indice_valor = 1

    while indice_valor <= 6:
        cantidad = conteos[indice_valor]
        if cantidad == 3:
            hay_tres_iguales = True
        elif cantidad == 2:
            hay_dos_iguales = True
        indice_valor = indice_valor + 1
    if hay_tres_iguales == True and hay_dos_iguales == True:
        return True
    else:
        return False

def es_poker(conteos):
    indice_valor = 1
    while indice_valor <= 6:
        cantidad = conteos[indice_valor]
        if cantidad == 4:
            return True
        indice_valor = indice_valor + 1
    return False

def es_generala(conteos):
    indice_valor = 1
    while indice_valor <= 6:
        cantidad = conteos[indice_valor]
        if cantidad == 5:
            return True
        indice_valor = indice_valor + 1
    return False

def puntaje_categoria_numerica(nombre_categoria, lista_dados):
    valores_numericos = {
        "unos": 1,
        "doses": 2,
        "treses": 3,
        "cuatros": 4,
        "cincos": 5,
        "seises": 6
    }

    if nombre_categoria in valores_numericos:
        numero = valores_numericos[nombre_categoria]
        return sumar_por_valor(lista_dados, numero)
    else:
        return -1

def puntaje_categoria_especial(nombre_categoria, lista_dados, nivel, conteos, generala_servida):
    if nombre_categoria == "escalera":
        if es_escalera(lista_dados):
            return nivel["puntos_especiales"]["escalera"]
        else:
            return 0
    elif nombre_categoria == "full":
        if es_full(conteos):
            return nivel["puntos_especiales"]["full"]
        else:
            return 0
    elif nombre_categoria == "poker":
        if es_poker(conteos):
            return nivel["puntos_especiales"]["poker"]
        else:
            return 0
    elif nombre_categoria == "generala":
        if es_generala(conteos):
            if generala_servida == True:
                return nivel["puntos_especiales"]["generala_servida"]
            else:
                return nivel["puntos_especiales"]["generala"]
        else:
            return 0
    return 0

def calcular_puntaje_categoria(nombre_categoria, lista_dados, nivel, generala_servida):
    conteos = contar_valores(lista_dados)
    puntaje_numerico = puntaje_categoria_numerica(nombre_categoria, lista_dados)
    if puntaje_numerico != -1:
        return puntaje_numerico
    puntaje_especial = puntaje_categoria_especial(nombre_categoria,lista_dados,nivel,conteos,generala_servida)
    return puntaje_especial

def determinar_generala_servida(cantidad_tiros):
    if cantidad_tiros == 1:
        return True
    else:
        return False
