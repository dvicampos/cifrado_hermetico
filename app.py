from flask import Flask, render_template, request, jsonify
import numpy as np
import random

app = Flask(__name__)

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

@app.route('/', methods=['GET', 'POST'])
def ocultar_palabra():
    imagen = 'loading.png'
    if request.method == 'POST':
        palabra = request.form['palabra']
        n = 15
        matriz, coordenadas, M = generar_cuadrado(palabra, n)
        return render_template('index.html', matriz=matriz, M=M, adivinar=True, palabra=palabra, coordenadas=coordenadas, imagen=imagen)
    else:
        return render_template('index.html')
def generar_cuadrado(palabra, n):
    posiciones = random.sample(range(n * n), len(palabra))
    posiciones.sort()
    matriz = [[''] * n for _ in range(n)]

    global M
    M = []

    for i in range(n):
        fila = []
        for j in range(n):
            fila.append('-')
        M.append(fila)

    global valores
    valores = ""
    coordenadas = ""
    for i, letra in enumerate(palabra):
        fila = posiciones[i] // n
        columna = posiciones[i] % n
        matriz[fila][columna] = letra
        M[fila][columna] = letra
        coordenadas += f"<p class='coordenadas'>Las coordenadas son: {columna+1} , {fila+1}</p>"
        valores+=f"{columna+1},{fila+1} "
    letras_disponibles = [datos[i] for i in range(1, 27)]
    for i in range(n):
        for j in range(n):
            if matriz[i][j] == '':
                matriz[i][j] = random.choice(letras_disponibles)

    return matriz, coordenadas, M


@app.route('/adivinar', methods=['POST'])
def adivinar_palabra():
    respuesta = request.json['respuesta']
    palabra = request.json['palabra']

    global valores

    mensaje = f'Las coordenadas son: {valores}'
    
    if respuesta in valores:
        mensaje += ' ¡FELICIDADES! ¡Las coordenadas son correctas! :)'
    else:
        mensaje += ' Incorrecto, vuelve a intentarlo.'

    return jsonify({'mensaje': mensaje})


# @app.route('/adivinar', methods=['POST'])
# def adivinar_palabra():
#     respuesta = request.json['respuesta']
#     palabra = request.json['palabra']
    
#     global M
#     global valores

#     # Imprimir los valores de la variable global valores en el mensaje
#     mensaje = f'Las coordenadas son: {valores}'
    
#     if respuesta == valores:
#         mensaje += ' ¡FELICIDADES! ¡Es la palabra correcta! :)'
#     else:
#         mensaje += ' Incorrecto, vuelve a intentarlo.'

#     return jsonify({'mensaje': mensaje})


if __name__ == '__main__':
    app.run(debug=True)