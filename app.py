import numpy as np
import random

datos = {
    1: "a",
    2: "b",
    3: "c",
    4: "d",
    5: "e",
    6: "f",
    7: "g",
    8: "h",
    9: "i",
    10: "j",
    11: "k",
    12: "l",
    13: "m",
    14: "n",
    15: "o",
    16: "p",
    17: "q",
    18: "r",
    19: "s",
    20: "t",
    21: "u",
    22: "v",
    23: "w",
    24: "x",
    25: "y",
    26: "z"
}

n = 18
letras = list(datos.values())

while len(letras) < n * n:
    letras += letras

matriz = []

for i in range(n):
    fila = []
    for j in range(n):
        aux = random.randint(1, 26)
        letra = datos[aux]
        fila.append(letra)
    matriz.append(fila)

palabra = input("Ingrese una palabra: ")
numlettras = len(palabra)

#PARA PODER MOSTRAR SOLO LAS LETRAS DEL MENSAJE
M = []
for i in range(n):
    fila = []
    for j in range(n):
        fila.append(' ')
    M.append(fila)

#SUSTITUIR LA LETRAS DE NUESTRO MENSAJE TOMANDO COMO BASE LA MATRIZ QUE SE LLENO DE LOS VALORES DEL JSON
archivo = open("desencriptacion.txt", "w")
for a in range(numlettras):
    i = random.randint(0, n-1)
    j = random.randint(0, n-1)
    # GUADAR EN LA MATRIZ PRINCIPAL
    matriz[i][j] = palabra[a]
    # GUADAR EN LA MATRIZ PARA MOSTRAR LA POSICION
    M[i][j] = palabra[a]
    # print(f"Las coordenadas de {a} son: {i+1} | {j+1}")
    coordenadas = (f"Las coordenadas de {palabra[a]} son: {i+1} | {j+1} \n")
    archivo.write(coordenadas)


for fila in matriz:
    for elemento in fila:
        print(elemento, end=" | ")
    print()

M = np.array(M)
np.savetxt(archivo, M, delimiter=" |", fmt="%s")

archivo.close()
