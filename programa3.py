# -*- coding: utf-8 -*-
"""
El ejercicio consiste en:
- Contar las lineas que tiene un archivo y mostrar el numero junto a cada linea
- Mostrar el contenido de cada linea, y en caso de que este vacia, indicar
- Mostrar en pantalla un conteo final indicando cuantas lineas son en total
"""

carpeta_nombre="C:\\Users\\Admin\\Documents\\Escuela\\6º Semestre\\Optativa\\Python\\Documentos\\"
archivo_nombre="doc1.txt"

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    lineas_lista=archivo.readlines()

palabra = input("Escribe la palabra a buscar en el documento: ")
num_palabras = 0
num_linea = 1
num_texto = 0
num_vacio = 0
for linea in lineas_lista:
    if linea.strip() == "":
        num_linea = num_linea+1
        print("LINEA",num_linea,":","Esta linea esta vacia")
        num_vacio=num_vacio+1
    else:
        num_linea=num_linea+1
        print("LINEA",num_linea,":",linea)
        num_texto=num_texto+1
        if palabra in linea:
            num_palabras = num_palabras+1
print("Lineas totales:",num_linea)
print("Lineas con texto:",num_texto)
print("Lineas vacias:",num_vacio)
print("La palabra:",palabra,"se encuentra:",num_palabras,"veces en el documento")