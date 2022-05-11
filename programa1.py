print("Procesamiento de Lenguaje natural")
print("Ingenieria en computacion")

suma = 5 + 6
resultado = suma * 4

print("Resultado =", resultado)
print("__________________________")

archivo = open('C:/Users/Admin/Documents/Escuela/6º Semestre/Optativa/Python/Prueba.txt')
print(archivo.read())
archivo.close()

archivo2 = open("C:\\Users\\Admin\\Documents\\Escuela\\6º Semestre\\Optativa\\Python\\Prueba2.txt","w")
cadena1 = "Clase de programación de python, en procesamiento"
archivo2.write(cadena1)
archivo2 = open("C:\\Users\\Admin\\Documents\\Escuela\\6º Semestre\\Optativa\\Python\\Prueba2.txt")
print(archivo2.read())
archivo2.close()
