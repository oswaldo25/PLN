import re

carpeta_nombre="C:\\Users\\Admin\Documents\\Escuela\\6º Semestre\\Optativa\\Python\\Documentos\\"
archivo_nombre="doc1.txt"

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    texto=archivo.read()
expresion_regular=re.compile(r"Arquitectura")
"""
resultado_busqueda=expresion_regular.search(texto)
print(resultado_busqueda.group(0))
"""

resultados_busqueda=expresion_regular.finditer(texto)
for resultado in resultados_busqueda:
    print(resultado.group(0))

expresion_regular=re.compile(r"en")
resultados_busqueda=expresion_regular.finditer(texto)
for resultado4 in resultados_busqueda:
    print(resultado4.group(0))
