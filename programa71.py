import nltk
#nltk.download('punkt')

carpeta_nombre="C:\\Users\\Admin\Documents\\Escuela\\6º Semestre\\Optativa\\Python\\Documentos\\"
archivo_nombre="doc3.txt"

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    texto=archivo.read()
tokens=nltk.word_tokenize(texto,"spanish")
for token in tokens:
    print(token)

palabras_total=len(tokens)
print("palabras", palabras_total)

tokens_conjunto=set(tokens)
palabras_diferentes=len(tokens_conjunto)
print("Palabras diferentes:", palabras_diferentes)

riqueza_lexica=palabras_diferentes/palabras_total
print("Riqueza lexica:", riqueza_lexica)
riqueza_lexica=100*palabras_diferentes/palabras_total
print("Riqueza lexica:", riqueza_lexica, "%")

texto_nltk=nltk.Text(tokens)
palabra=input("Escribe la palabra a buscar en el documento: ")
texto_nltk.concordance(palabra)
texto_nltk.similar(palabra)
conteo_individual=tokens.count(palabra)
print("Numero de veces que se encuentra la palabra en el texto:", conteo_individual)
