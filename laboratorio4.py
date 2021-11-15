#!/usr/bin/python3

# Laboratorio4.py
# Curso: Programación bajo plataformas abiertas
# Adonay Juárez Moraga B74047

''' Este programa se encarga restar y sumar matrices, siempre y cuando sea
    de la misma magnitud
'''
class Matriz:
    def __init__(self, fila1, columna1, fila2, columna2):
        # Se añaden lo atributos de la clase matriz.
        self.n = fila1
        self.m = columna1
        self.n2 = fila2
        self.m2 = columna2

    # Se crea parametros para Matriz 1
    def matriz_1(self):

        # Crear matriz 1
        matriz = []
        for i in range(fila1):
            matriz.append([0]*columna1)
        for f in range(fila1):
            for c in range(columna1):
                matriz[f][c] = int(input("Elemento de la matriz 1 >> %d, %d : " % (f,c)))
        print(matriz)


    # Se crea paramnetos para Matriz 2
    def matriz_2(self):

        # Crear parametros para Matriz 2
        matriz1 = []
        for i in range(fila2):
            matriz1.append([0]*columna2)
        for fi in range(fila2):
            for co in range(columna2):
                matriz1[fi][co] = int(input("Elemento de la matriz 2 >> %d, %d : " % (fi,co)))
        print(matriz1)
     



# Validez para ejecutar el código de la clase
if __name__== "__main__":
    fila1 = int(input("Digite la magnitud de la fila matriz 1: "))
    columna1 = int(input("Digite la magnitud de la columna 1: "))
    fila2 = int(input("Digite la magnitud de la fila 2: "))
    columna2 = int(input("Digite la magnitud de la columna 2: "))
    x = Matriz(fila1, columna1, None, None)
    y = Matriz(fila2, columna2, None, None)
    uno = x.matriz_1()
    dos = y.matriz_2()
    print(uno, dos)
    
