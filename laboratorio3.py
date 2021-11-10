#!/usr/bin/python3

# Laboratorio3.py 
# Curso: Programación bajo plataformas abiertas
# Adonay Juárez Moraga B74047


'''Es un programa que simula la operación de fibonacci,
   dependiendo del número recibido.
'''

import argparse
import time


'''Se importa de la biblioteca "argparse" y "time" para agregar
argumentos requeridos y posicionales.'''


# Se agrega los argumentos, tanto requeridos como opcionales. 
parser = argparse.ArgumentParser(
    description="Menú de ejecucion de fibonacci"
)

parser.add_argument(
    "posición",
    type=int, 
    help='Posicion en la secuencia de Fibonacci que debe ser calculado.'
)
parser.add_argument(
    "--tiempo",
    "-t", 
    action="store_true", 
    help="Tiempo que dura en ejecutar la tarea"
)
parser.add_argument(
    '--completa', 
    '-c', 
    action="store_true", 
    help='Imprime la secuencia completa.'
)

# Obtengo los argumemtos y los guardo en args
args = parser.parse_args()

# Accedo fácilmente los argumentos mediante atributos del objeto args
# Si el argumento no fue dado por el usuario se convierte en None
resultado = args.posicion
resultado2 = args.tiempo
resultado3 = args.completa


# Definir la funcion Fibonacci.
# Es llamada por el argumento posición.
def fibonacci(resultado):


    # Definir las restricciones del dígito ingresado
    if resultado == 0 or resultado == 1:
        return 1
    else:
        return (fibonacci(resultado-1) + fibonacci(resultado-2))


print(
    "El fibonacci de índice: ", 
    str(resultado), "es: ", 
    fibonacci(resultado
    )
)


# Definir funcion para el tiempo.
# Llamada por el argumento opcional -t.
def duracion(resultado2):

    
    # Definir los parametros de tiempo.
    inicio = time.time()
    fibonacci(resultado)
    fin = time.time()
    x = fin - inicio

    if resultado2 == True or resultado2 == False:
        return print("El tiempo que dura la ejecucion es:", x, "segundos")
    else:
        print("")


print(
    duracion(resultado2)
)


# Definir funcion de completa.
def completa(resultado3):


    # Definir fibonaci, agrega la secuencia completa.
    # Toma el nombre de fibona
    def fibona(resultado):

        print("fibonacci: "+ str(resultado))
        if resultado == 0:
            return 1
        elif resultado == 1:
            return (fibona(resultado-1) + fibona(resultado-2))
    if resultado3 == True:
        return fibona(resultado)
    else:
        return print("")


print(
    completa(resultado3)
)
