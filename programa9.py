import nltk
import matplotlib.pyplot as plt
carpeta_nombre="C:\\Users\\Admin\Documents\\Escuela\\6º Semestre\\Optativa\\Python\\Documentos\\"
archivo_nombre="doc2.txt"
with open(carpeta_nombre+archivo_nombre, "r") as archivo:
    texto=archivo.read()
print("-------------------------------------------------------")
tokens=nltk.word_tokenize(texto, "spanish")

tokens_conjunto=set(tokens)
palabras_totales=len(tokens)
palabras_diferentes=len(tokens_conjunto)
print(palabras_totales)
print(palabras_diferentes)
texto_nltk=nltk.Text(tokens)
distribucion=nltk.FreqDist(texto_nltk)
print("-------------------------------------------------------")
hapaxes=distribucion.hapaxes()
for hapax in hapaxes:
    print(hapax)
from matplotlib import rcParams
rcParams.update({"figure.autolayout": True})
distribucion.plot(cumulative=True)
distribucion.plot(40,cumulative=True)

print("-------------------------------------------------------")
#La funcion count regresa la cuenta total de las palabras en el texto 
contar=texto_nltk.count('La')
print(contar)

#La funcion vocab devuelve el vocabulario total del texto de las palabras unicas
vocab=len(texto_nltk.vocab())
print(vocab)

"""Una colocación es una secuencia de palabras que aparecen juntas con una 
frecuencia inusual."""
#nltk.download('stopwords')
colocacion=texto_nltk.collocation_list()
print(colocacion)
