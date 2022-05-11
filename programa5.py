# -*- coding: utf-8 -*-

"""
El ejercicio consiste en obtener el vocabulario de TODOS los documentos, es dec
"""

carpeta_nombre = "C:\\Users\\Admin\Documents\\Escuela\\6º Semestre\\Optativa\\Python\\Documentos\\"
archivo_nombre = "doc1.txt"

with open(carpeta_nombre + archivo_nombre, "r") as archivo:
    texto = archivo.read()

simbolos = ["(",")",",",".",";",":","\""]

for simbolo in simbolos:
    texto = texto.replace(simbolo," " + simbolo + " ")

palabras_lista = texto.split()

palabras_unicas = []

for palabra in palabras_lista:
    if palabra in palabras_unicas:
        continue
    palabras_unicas.append(palabra)
print(palabras_unicas)
num = len(palabras_unicas)
print("Numero de palabras unicas en el documento:", num)
num2 = len(palabras_lista)
print("Numero de palabras de todo el documento:", num2)
# En este punto la solucion esta en palabras_unicas