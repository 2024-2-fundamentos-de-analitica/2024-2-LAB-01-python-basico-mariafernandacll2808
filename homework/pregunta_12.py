"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    suma_por_letra = {}

    with open("files/input/data.csv", "r") as file:
        for line in file:
            valores = line.strip().split("\t")
            letra = valores[0]
            diccionario = valores[4].split(",")

            suma_valores = sum(int(par.split(":")[1]) for par in diccionario)

            if letra in suma_por_letra:
                suma_por_letra[letra] += suma_valores
            else:
                suma_por_letra[letra] = suma_valores

    return dict(sorted(suma_por_letra.items()))  # Ordena alfabéticamente las claves
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
