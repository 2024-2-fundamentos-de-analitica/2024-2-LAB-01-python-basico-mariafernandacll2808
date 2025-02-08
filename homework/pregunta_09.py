"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    valores_por_clave = {}

    with open("files/input/data.csv", "r") as file:
        for line in file:
            valores = line.strip().split("\t")
            diccionario = valores[4].split(",")

            for par in diccionario:
                clave, valor = par.split(":")
                valor = int(valor)

                if clave in valores_por_clave:
                    valores_por_clave[clave] += 1
                else:
                    valores_por_clave[clave] = 1

    resultado = dict(sorted(valores_por_clave.items()))

    return resultado
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
