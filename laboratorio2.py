#!/usr/bin/python3

#Laboratorio2.py
#Adonay Juarez Moraga B74047
'''Este es un programa que recibe y procesa una cantidad de nombres
   haciendo un arreglo de mayusculas para aquellas que las necesita. Luego se finalizar
   "SALIR" se registra todos los nombres recibidos'''




print("----------------------------------------------------")
print("Es un programa que recibe y procesa nombres haciendo un cambio gramatical(hace mayúscula) el inicio de cada palabra.")
print("Si desea SALIR, esta lista los nombres procesados al final del programa.")
print("----------------------------------------------------")
#Lista vacía que recibe los nombres del bucle.
nombres1 = []


#Con este bucle, realiza un ciclo de procesamiento de nombres
#cuando reciba un "SALIR" saldrá del programa. 
while(True):

    #Dentro del bucle se crea una variable interativa
    #Se convierte el nombre recibido en string
    nombre = input("Escriba el nombre a procesar, o SALIR para salir:")
    nom = str(nombre)
    cadena = nom.split(" ")
    cantidad =len(cadena)
    
    '''Dependiendo de las condiciones que presente el nombre recibido será procesada
       por las siguintes condiciones'''
    
    #Se sale del ciclo
    if (nombre == "SALIR"):
        for elem in nombres1:
            print("{}".format(elem))   
        break

    #Si la cantidad de componentes recibidos es menor que 3.
    elif (cantidad < 3):
        print("No se puede tener menor de 3 componenetes. Vuelva a intentarlo.")
    
    #Si la cantidad de componentes recibidos es mayor a 4.
    elif (cantidad > 4):
        print("No se puede tener mayor a 4 componenetes. Vuelva a intentarlo.")

    #Si la cantidad de componentes es igual a 3. Entonces inicia el procesamiento. 
    elif (cantidad == 3):

        #"nombres" adjunta los nombres en una lista (vacia) en un solo string. 
        nombres = []

        #Posiciones de las strings recibidos. 
        primer_nom = cadena[0]
        apellido1 = cadena[1]
        apellido2 = cadena[2]

        #Procesamientos de las mayúsculas en los primeros dígitos. 
        a = primer_nom.capitalize()
        b = apellido1.capitalize()
        c = apellido2.capitalize()

        #Hacer string a las posiciones para adjuntar en la lista vacia "nombres" 
        string1 = str(a)
        string2 = str(b)
        string3 = str(c)
        
        #Se adjunta los strings en la lista vacia "nombres"
        nombres.append(string1)
        nombres.append(string2) 
        nombres.append(string3)

        #Se convierte los strings de nomnbres y apellidos en una sola, para así adjuntarlo en la lista vacía "nombres1"
        cadena1 = " ".join(nombres)
        cadena_final = str(cadena1)
        nombres1.append(cadena_final)

    #Si la cantidad de componentes es igual a 4. Entonces inicia el procesamiento.   
    elif (cantidad == 4):

        #"nombres2" adjunta los nombres en una lista (vacia) en un solo string. 
        nombres2 = []

        #Posiciones de las strings recibidos. 
        primer_nom = cadena[0]
        segund_nom = cadena[1]
        apellido1 = cadena[2]
        apellido2 = cadena[3]

        #Procesamientos de las mayúsculas en los primeros dígitos.
        d = primer_nom.capitalize()
        e = segund_nom.capitalize()
        f = apellido1.capitalize()
        g = apellido2.capitalize()

         #Hacer string a las posiciones para adjuntar en la lista vacia "nombres2" 
        string4 = str(d)
        string5 = str(e)
        string6 = str(f)
        string7 = str(g)

        #Se adjunta los strings en la lista vacia "nombres2"
        nombres2.append(d)
        nombres2.append(e)
        nombres2.append(f)
        nombres2.append(g)

        #Se convierte los strings de nomnbres y apellidos en una sola, para así adjuntarlo en la lista vacía "nombres1"
        cadena2 = " ".join(nombres2)
        cadena_final1 = str(cadena2)
        nombres1.append(cadena_final1)

    else:
        print("Fin del programa")

print("                                   ")
print("                                   ")       
print("-----------------------------------")
print("-----------------------------------")
print("FIN DEL PROGRAMA")
print("-----------------------------------")
print("-----------------------------------")   
    
    
        


