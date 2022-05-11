# -*- coding: utf-8 -*-

"""
El ejercicio consiste en unir todos los documentos en uno solo
"""

import os

carpeta_nombre = "C:\\Users\\Admin\Documents\\Escuela\\6º Semestre\\Optativa\\Python\\Documentos\\"
carpeta_salida = "C:\\Users\\Admin\Documents\\Escuela\\6º Semestre\\Optativa\\Python\\Documentos\\"

archivo_salida = "Union.txt"

archivos_lista = os.listdir(carpeta_nombre)

union = ""
for archivo_nombre in archivos_lista:
    archivo = open(carpeta_nombre + archivo_nombre)
    texto = archivo.read()
    archivo.close
    union += texto

with open(carpeta_salida + archivo_salida, "w") as salida:
    salida.write(union)