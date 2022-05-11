"""
Dante Villanueva López
- El programa consiste en leer dos documentos de texto.txt,
- cada documento de texto.txt debe tener tres parrafos como minimo,
- de los cuales muestre cuantas lineas(longitud) con texto y 
- cuantas lineas vacias tiene cada documento,
- que elimine los simbolos de puntuacion y
- que muestre todas las palabras que contiene cada documento de mananera ordenada,
- que muestre cuantas palabras(longitud) contiene cada documento,
- que una los dos documentos en otro nombre de documento.txt y que elimine los simbolos de puntuacion y 
- que muestre todas las palabras que contiene el documento nuevo, de manera ordenada y 
- que muestre cuantas palabras(longitud) contiene el documento,
- que escribas una palabra y la busque o indique si la encontro o no.
"""

import os

# Leer dos documentos
archivo = open('C:\\Users\\Admin\\Documents\\Escuela\\6º Semestre\\Optativa\\Python\\documentos\\doc1.txt')
print("Documento 1: ",archivo.read())
archivo.close()

print("----------------------------------------------------------------------------------------------")

archivo = open('C:\\Users\\Admin\\Documents\\Escuela\\6º Semestre\\Optativa\\Python\\documentos\\doc2.txt')
print("Documento 2: ",archivo.read())
archivo.close()

print("----------------------------------------------------------------------------------------------")

# Mostrar cuantas lineas(longitud) con texto y cuantas lineas vacias tiene cada documento
print("Documento 1: ")

carpeta_nombre="C:\\Users\\Admin\\Documents\\Escuela\\6º Semestre\\Optativa\\Python\\Documentos\\"
archivo_nombre="doc1.txt"

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    lineas_lista=archivo.readlines()

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

print("Lineas totales:",num_linea)
print("Lineas con texto:",num_texto)
print("Lineas vacias:",num_vacio)

print("----------------------------------------------------------------------------------------------")

print("Documento2: ")

carpeta_nombre="C:\\Users\\Admin\\Documents\\Escuela\\6º Semestre\\Optativa\\Python\\Documentos\\"
archivo_nombre="doc2.txt"

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    lineas_lista=archivo.readlines()

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

print("Lineas totales:",num_linea)
print("Lineas con texto:",num_texto)
print("Lineas vacias:",num_vacio)

print("----------------------------------------------------------------------------------------------")

# Eliminar simbolos de puntuacion
carpeta_nombre = "C:\\Users\\Admin\Documents\\Escuela\\6º Semestre\\Optativa\\Python\\Documentos\\"
archivo_nombre = "doc1.txt"

archivo=open(carpeta_nombre+archivo_nombre)
texto=archivo.read()
archivo.close()

simbolos=["(",")",",",".",";",":","\""]
for simbolo in simbolos:
    texto=texto.replace(simbolo,"")
print(texto)

print("----------------------------------------------------------------------------------------------")

carpeta_nombre = "C:\\Users\\Admin\Documents\\Escuela\\6º Semestre\\Optativa\\Python\\Documentos\\"
archivo_nombre = "doc2.txt"

archivo=open(carpeta_nombre+archivo_nombre)
texto=archivo.read()
archivo.close()

simbolos=["(",")",",",".",";",":","\""]
for simbolo in simbolos:
    texto=texto.replace(simbolo,"")
print(texto)

print("----------------------------------------------------------------------------------------------")

# Palabras de forma ordenada
carpeta_nombre="C:\\Users\\Admin\\Documents\\Escuela\\6º Semestre\\Optativa\\Python\\Documentos\\"
archivo_nombre="doc1.txt"

archivo=open(carpeta_nombre+archivo_nombre)
texto=archivo.read()
archivo.close()

print("Documento 1: ")
palabras_lista=texto.split()
palabras_lista.sort()
for palabra in palabras_lista:
    print(palabra)

print("----------------------------------------------------------------------------------------------")

carpeta_nombre="C:\\Users\\Admin\\Documents\\Escuela\\6º Semestre\\Optativa\\Python\\Documentos\\"
archivo_nombre="doc2.txt"

archivo=open(carpeta_nombre+archivo_nombre)
texto=archivo.read()
archivo.close()

print("Documento 2: ")
palabras_lista=texto.split()
palabras_lista.sort()
for palabra in palabras_lista:
    print(palabra)

print("----------------------------------------------------------------------------------------------")

# Palabras(longitud) de cada documento
carpeta_nombre="C:\\Users\\Admin\\Documents\\Escuela\\6º Semestre\\Optativa\\Python\\Documentos\\"
archivos_lista=os.listdir(carpeta_nombre)

for archivo_nombre in archivos_lista:
    print(archivo_nombre)
    archivo=open(carpeta_nombre+archivo_nombre)
    lineas_lista = archivo.readlines()
    archivo.close()
    longitud = len(lineas_lista)
    print("El archivo", archivo_nombre,"tiene",longitud,"lineas")

print("----------------------------------------------------------------------------------------------")

# Unir los documentos y eliminar los simbolos de puntuacion
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

carpeta_nombre = "C:\\Users\\Admin\Documents\\Escuela\\6º Semestre\\Optativa\\Python\\Documentos\\"
archivo_nombre = "Union.txt"

archivo=open(carpeta_nombre+archivo_nombre)
texto=archivo.read()
archivo.close()

simbolos=["(",")",",",".",";",":","\""]
for simbolo in simbolos:
    texto=texto.replace(simbolo,"")
print(texto)

print("----------------------------------------------------------------------------------------------")

# Mostrar todas las palabras que contiene el documento nuevo, de manera ordenada y que muestre cuantas palabras(longitud) contiene el documento,

carpeta_nombre="C:\\Users\\Admin\\Documents\\Escuela\\6º Semestre\\Optativa\\Python\\Documentos\\"
archivo_nombre="Union.txt"

archivo=open(carpeta_nombre+archivo_nombre)
texto=archivo.read()
archivo.close()

print("Union: ")
palabras_lista=texto.split()
palabras_lista.sort()
for palabra in palabras_lista:
    print(palabra)

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    lineas_lista=archivo.readlines()

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

print("Lineas totales:",num_linea)

print("----------------------------------------------------------------------------------------------")

# Escribir una palabra y la busque o indique si la encontro o no.
carpeta_nombre="C:\\Users\\Admin\\Documents\\Escuela\\6º Semestre\\Optativa\\Python\\Documentos\\"
archivo_nombre="Union.txt"
palabra = input("Escribe la palabra a buscar en el documento ")

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    texto=archivo.read()

if palabra in texto:
    print("La palabra:", palabra, "fue encontrada en el texto")
else:
    print("La palabra:", palabra, "no fue encontrada en el texto")