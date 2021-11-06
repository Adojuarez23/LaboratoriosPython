#!/usr/bin/python3

# Laboratorio3.py 
# Curso: Programación bajo plataformas abiertas
# Adonay Juárez Moraga B74047
'''Es un programa que simula la operación de fibonacci,
   dependiendo del número recibido.
'''

import argparse
import time

'''Se importa de la biblioteca los "argparse" para agregar
argumentos opcionales y requeridos.'''


# Definir una función fibonacci:


def fibonacci(numero):

    # Formula de fibonacci
    if numero == 0 or numero == 1:
        return 1
    else:
        return (fibonacci(numero-1) + fibonacci(numero-2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Programa para calcular la formula de fibonacci")
    parser.add_argument("posición", type=int, help='Posicion en la secuencia de Fibonacci que debe ser calculado.')
    parser.add_argument('--completa', '-c', dest= 'completo', action="store_true", help='Imprime la secuencia completa.')

    args = parser.parse_args()

    resultado = fibonacci(args.posicion)
    resultado2 = fibonacci(args.completo)
    print("the" + str(args.posicion) + "texto de agregar" + str(resultado))
    print("the" + str(args.completo) + "texto de agregar" + str(resultado2))


# Red interativa: Recibe y procesa.
numero = int(input("Digite un numero: "))
print("El fibonacci del número digitado es: {}".format(fibonacci(numero)))