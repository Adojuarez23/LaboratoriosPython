#TAREA DE PLATAFORMAS 

#Importar paquetería 
import string

print("---------------------------------------------------")
print("---------------------------------------------------")
print("Creación de pirámide")
print("Según el últimmo valor del carnet se construye una piramide. Esta determina la altura.")
print("Ademas se añade un caracter para su elaboración")
print("---------------------------------------------------")
print("---------------------------------------------------")

#Hacer una lista el valor del carnet
milista = []
def string_int(datos):
    for i in datos:
        milista.append(str(i))
digito = input("Digite su carnet:")   
string_int(digito)

#Se crea una variable interativa 
cararter = str(input("Digite el caracter que desea diseñar la pirámide:"))

#Determinar la paridad del ultimo digito
#Creacíon de la pirámide impar
ultimo = milista[5]
entero = int(ultimo)

if entero % 2 == 0:
    print("El último valor de su carnet es: {}".format(milista[5]),"y es par")
    print("La pirámide es invertida")
    for i in range(entero+1):
        escalon = entero-i 
        print(escalon*cararter)
else:
    print("El último valor de su carnet es: {}".format(milista[5]),"y es impar")
    print("La pirámide no es invertida")
    for i in range(entero+1):
        print(cararter*i)

print("---------------------------------------")
print("---------------------------------------")
print("Fin del programa.")
print("¡Gracias!")
print("---------------------------------------")
print("---------------------------------------")













