carpeta_nombre="C:\\Users\\Admin\\Documents\\Escuela\\6º Semestre\\Optativa\\Python\\Documentos\\"
archivo_nombre="doc1.txt"
palabra = input("Escribe la palabra a buscar en el documento ")

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    texto=archivo.read()

if palabra in texto:
    print("La palabra:", palabra, "fue encontrada en el texto")
else:
    print("La palabra:", palabra, "no fue encontrada en el texto")