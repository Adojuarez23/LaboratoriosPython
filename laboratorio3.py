#!/usr/bin/python3

# Laboratorio3.py
# Curso: Programacion bajo plataformas abiertas
# Adonay Juarez Moraga B74047

''' Es un programa que simula la operacion de fibonacci,
    de pendiendo del numero recibido.
'''


import argparse
import time


''' Se importa de la biblioteca argsparser y time,
    para agregar argumentos requeridos y posicionales.
'''

# Se agrega argumentos: posicio, tiempo, completa.
parser = argparse.ArgumentParser(
        "Menus para ejecucion de fibonacci"
        )
# Se agrega argumento requeridos como opcionales
parser.add_argument(
        "posicion",type=int,
        help="formula de fibonacci dado a la posicion"
        )
parser.add_argument(
        "--tiempo", "-t", action= "store_true",
        help="Tiempo que dura en ejecutar la tarea"
        )
parser.add_argument(
        "--completa", "-c", action="store_true",
        help="Imprime la sencuencia completa"
        )

# Obtengo los argumentos y los guardo en args
args = parser.parse_args()

# Accedo facilmente los argumentos mediante atributos del objeto 
# args. Si el argumento no fue dado por el usuario se convierte
# en un None
resultado = args.posicion
resultado2 = args.tiempo
resultado3 = args.completa


# Definir funcion fibonacci.
# Es llamada por argumento posicional
def fibonacci(resultado):    
    if resultado == 0:
        return 1
    elif resultado == 1:
        return 1
    else:
        return (fibonacci(resultado-1) +
                fibonacci(resultado-2))

print(
        "El fibonacci de indice", 
        str(resultado), "es: ",fibonacci(resultado)
        )
''' Para las variables de resultado2 y resultado3
    se tiene que hacer funciones para activarlas, ya que
    solo se comporta como True y False. Por lo tando, al ser    llamadas    se ejeutan dichas operaciones.
'''


# Definir funcion para tiempo: duracion.
# Es llamada por argumento tiempo
def duracion(resultado2):
    inicio = time.time()
    fibonacci(resultado)
    fin = time.time()
    x = fin - inicio

    if resultado2 == True:
        return print(
                "El tiempo que dura la ejecucion es: ", x, "segundos"
                )
    
    else:
        print("")

# Se imprime la funcion del tiempo
print(duracion(resultado2))


# Definir funcion para la funcion completa.
# Es llamada por el argumento completa.
def completa(resultado3):
    def fibona(resultado):
        print("Fibonacci:"+ str(resultado))
        if resultado ==  0:
            return 1
        elif resultado == 1:
            return 1
        else:
            return (fibona(resultado-1) + 
                    (fibona(resultado-2)))


    if resultado3 == True:
        return fibona(resultado)
    else:
        return print("")


# Se imprime la secuencia completa
print(completa(resultado3))





