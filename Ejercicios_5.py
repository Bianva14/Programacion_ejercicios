# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 05:37:52 2021

@author: pc1
"""

#%%Ejercicio 105: Reverse Order
"""
@autor: Bianca Ramirez Mejia 421117321
Ejercicio individual

Descripcion del problema:
Escriba un programa que lea enteros del usuario y los almacene en una lista. Utilice 0 como
un valor centinela para marcar el final de la entrada. Una vez leídos todos los valores
su programa debe mostrarlos (excepto el 0) en orden inverso, con un valor
que aparecen en cada línea."""

from me_5 import main
if __name__ =="__main__":
    main()
"""Complicaciones:
No hubo ninguna complicacion solo me tarde un poco""" 
#%%"Ejercicio 109: Lista de divisores propios"
"""
Descripcion de la solucion:
Un divisor propio de un entero positivo, n, es un entero positivo menor que n que divide 
uniformemente en n.Escribe una función que calcule todos los divisores propios de un positivo
entero. El entero se pasará a la función como su único parámetro. La función
devolverá una lista que contiene todos los divisores adecuados como único resultado. Completo
este ejercicio escribiendo un programa principal que demuestra la función leyendo
un valor del usuario y muestra la lista de sus divisores adecuados. Asegúrese de que su
El programa principal solo se ejecuta cuando su solución no se ha importado a otro archivo."""
"Solución del problema"
from me_5.py import mostrar_divi_prop
if __name__ == "__main__":
    mostrar_divi_prop()   
    
""" No lograba entender a que se referia con divisores propios hasta que investigue"""
#%%Ejercicio 111:Solo palabras
"""
Descripcion del ejercicio:
En este ejercicio, creará un programa que identifica todas las palabras en una cadena
ingresado por el usuario. Empiece por escribir una función que tome una cadena de texto 
como único parámetro. Su función debería devolver una lista de las palabras en la 
cadena con los signos de puntuación en los bordes de las palabras eliminadas. Los 
signos de puntuación que debes eliminar incluyen comas, puntos, signos de interrogación,
guiones, apóstrofos, signos de exclamación, dos puntos y punto y coma. No elimine los 
signos de puntuación que aparecen en la mitad de una palabra, como los apóstrofos 
utilizados para formar una contracción. Por ejemplo, si su función se 
proporciona con la cadena"Examples of contractions include: don’t, isn’t, and wouldn’t."
entonces su función debería devolver la lista ["Examples", "of", "contractions", "include","don’t", "isn’t",
"and", "wouldn’t"].
Escribe un programa principal que demuestre tu función. Debería leer una cadena
del usuario y mostrar todas las palabras de la cadena con los signos de puntuación
remoto. Deberá importar su solución a este ejercicio al completar
Ejercicio 158. Como resultado, debe asegurarse de que su programa principal solo se ejecute cuando
su archivo no ha sido importado a otro programa."""
from me_5 import main
if __name__=="__main__":
    main()
#%%Ejercicio 112: Por debajo y encima del promedio(INDIVIDUAL)
"""
Descripcion del problema:
Escriba un programa que lea números del usuario hasta que se ingrese una línea en blanco.
Su programa debe mostrar el promedio de todos los valores ingresados por el usuario.
Luego, el programa debe mostrar todos los valores promedio inferiores, seguidos de todos 
los valores promedio (si los hay), seguidos de todos los valores promedio anteriores. Debe 
mostrarse una etiqueta apropiada antes de cada lista de valores.
Descripcion de la solucion:
"""
from me_5 import main
main()
#%%Ejercicio 115: Pig Latin(HUGO)
"""Pig Latin es un idioma construido mediante la transformación de palabras en inglés. 
Si bien se desconocen los orígenes del idioma, se menciona en al menos dos documentos 
del siglo XIX, lo que sugiere que existe desde hace más de 100 años. Las siguientes 
reglas se utilizan para traducir del inglés al latín de cerdo:
• Si la palabra comienza con una consonante (incluida y), todas las letras al principio 
de la palabra, hasta la primera vocal (excluyendo y), se eliminan y luego se agregan al
final de la palabra, seguidas de ay. Por ejemplo:
computer se convierte en omputercay and think se convierte en inkthay.
• Si la palabra comienza con una vocal (sin incluir y), entonces se agrega way al final
de la palabra. Por ejemplo, algorithm se convierte en algorithmway y office se convierte
en officeway.
Escriba un programa que lea una línea de texto del usuario. Entonces su programa debe
traduzca la línea al latín de cerdo y muestre el resultado. Puede suponer que la cadena
ingresado por el usuario solo contiene letras minúsculas y espacios."""

#Lee pedimos al usuario una cadena para obtener su pig latin
cadena = input("Ingresa una cadena: ")
listaPalabras = cadena.split(" ")#Devuelve una lista de palabras usando " " como cadena de separación. 
#Creamos las listas que contienen los elementos de vocales
vocales_incluyendo_y = ["a", "e", "i", "o", "u", "y"]
print(cadena)
nuevaCadena = "" #Cadena vacía
for palabra in listaPalabras:
    #print(palabra)
    bufferLetras = ""
    nuevaPalabra = ""
    #Revisamos las letras de la palabra y cuando lleguemos a una vocal, la agregaremos 
    #a una cadena llamada bufferLetras
    for letra in palabra:
        #print(letra)
        if letra in vocales_incluyendo_y:
            break
        bufferLetras += letra
    #Cuando tengamos el buffer de letras se creara nuestra nueva palabra(pig latin)
    #esta sera  obtendra cuando todas las letras al principio de la palabra, hasta 
    #la primera vocal (excluyendo y), se eliminan y luego se agregan al
    #final de la palabra, seguidas de ay.
    if bufferLetras:
        nuevaPalabra = palabra+bufferLetras+"ay"
        nuevaPalabra = nuevaPalabra[len(bufferLetras):]
    #Si la palabra comienza con una vocal (sin incluir y), entonces se agrega way
    #al final de la palabra
    else: 
        nuevaPalabra = palabra+"way"
    #a la cadena NuevaCadena se le agrega la nueva palabra    
    nuevaCadena += nuevaPalabra+" "
    
print(nuevaCadena)
"""Complicaciones:
No hubo complicaciones"""
#import pdb; pdb.set_trace()  #Es para hacer un debug
#%%Ejercicio 116:Latin de cerdo mejorado
"""Ejercicio 116: latín de cerdo mejorado
Descripcion del problema
Amplíe su solución al ejercicio 115 para que maneje correctamente las letras mayúsculas y
signos de puntuación como comas, puntos, signos de interrogación y signos de exclamación.
Si una palabra en inglés comienza con una letra mayúscula, entonces su representación 
en latín de cerdo.
también debe comenzar con una letra mayúscula y la letra mayúscula se debe mover al final
de la palabra debe cambiarse a minúscula. Por ejemplo, Computer debería convertirse
Omputercay. Si una palabra termina en un signo de puntuación, el signo de puntuación
debe permanecer al final de la palabra después de que se haya realizado la transformación.
Por ejemplo ciencia! debería convertirse en Iencescay !."""
#Lee pedimos al usuario una cadena para obtener su pig latin
cadena = input("Ingresa una cadena: ")
listaPalabras = cadena.split(" ")#Devuelve una lista de palabras usando " " como cadena de separación. 
#Creamos las listas que contienen los elementos de vocales y signos de ortografia
vocales_incluyendo_y = ["a", "e", "i", "o", "u", "y"]
signos_de_ortografia = [",",";",":","!","¡","¿","?","-"]
print(cadena)
nuevaCadena = "" #Cadena vacía
for palabra in listaPalabras:
    bufferLetras = ""
    signo = ""
    nuevaPalabra = ""  
    #Si la palabra que esta en lista de palabras empieza con mayuscula, 
    if palabra == palabra.capitalize(): 
        #Revisamos las letras de la palabra y cuando lleguemos a una vocal, la agregaremos 
        #a una cadena llamada bufferLetras
        for letra in palabra:
            #print(letra)
            if letra in vocales_incluyendo_y:
                break           
            bufferLetras += letra
         #Cuando tengamos el buffer de letras se creara nuestra nueva palabra(pig latin)
         #esta sera  obtendra cuando todas las letras al principio de la palabra, hasta 
         #la primera vocal (excluyendo y), se eliminan y luego se agregan al
         #final de la palabra, seguidas de ay.
        if bufferLetras:
            nuevaPalabra = palabra+bufferLetras+"ay"
            nuevaPalabra = nuevaPalabra[len(bufferLetras):]
        #Si la palabra comienza con una vocal (sin incluir y), entonces se agrega way
        #al final de la palabra
        else: 
            nuevaPalabra = palabra+"way"
        #Con la nueva cadena generada debemos hacer que si la palabras tiene un signo de  ortografia
        #se debe enviar al ultimo lugar de la cadena
        for x in nuevaPalabra:
            if x in signos_de_ortografia:
                signo += x
            for y in range(len(signo)):
                nuevaPalabra2 = nuevaPalabra.replace(signo[y],"")
                nuevaPalabra = nuevaPalabra2 + signo[y]

        nuevaCadena += nuevaPalabra+ " " 
    #Si la palabra es minuscula se repite el mismo procedimiento que con la mayuscula
    else:
        for letra in palabra:
            #print(letra)
            if letra in vocales_incluyendo_y:
                break           
            bufferLetras += letra
        
        if bufferLetras:
            nuevaPalabra = palabra+bufferLetras+"ay"
            nuevaPalabra = nuevaPalabra[len(bufferLetras):]
        else: 
            nuevaPalabra = palabra+"way"
        for x in nuevaPalabra:
            if x in signos_de_ortografia:
                signo += x
            for y in range(len(signo)):
                nuevaPalabra2 = nuevaPalabra.replace(signo[y],"")
                nuevaPalabra = nuevaPalabra2 + signo[y]
            
        nuevaCadena += nuevaPalabra+" "
#Imprimimos la nueva palabra  
print(nuevaCadena)
"""Complicaciones:
No hubo complicaciones"""
#%%Ejercicio 117:Linea de mejor ajuste(Me falatn comenatiso)
"""Una linea del mejor ajuste es una linea recta que se
aproxima mejor a una colección de n puntos de datos. En este ejercicio 
nosotros aasumiremos que cada uno de los puntos en la colección tienen 
una cordenanda x y una cordenada y. El simbolo x´ y y´son usados para 
representar el valor medio de x en la colección y el valor promedio de 
y en la colección respectivamente. La linea del mejor areglo es representada
por la ecuación y = mx + b, donde m y b son calculados usando las 
siguientes formulas:
    
    m = ( (sum(xy))-((sum(x) * sum(y)) / n)) / (sum(x^2)-(((sum(x))^2 ) / n)) 
    b = y_ - (m * x_)
Escribe un programa que lea una colección de puntos dados por el usuario. 
El usuario ingresará la parte x de la primer cordenada en su propia linea,
seguido de la parte y de la primer cordenada en su propia linea. 
Permite que el usuario continue ingresando cordenadas, con las partes 
x y y cada entrada en su propia linea, hasta que tu programa lea una 
linea en blanco para la cordenada x.
Muestra la formula para la line del mejor arreglo en la forma y = mx + b
reemplazando m y b con los valores calculados usando las formulas precedentes.
Por ejemplo, si el usuario ingresa las coordenadas (1,1),(2,2.1) y (3,2.9)
entonces tu programa debería mostrar y = 0.95x + 0.1        
Solución del problema"""
x=[]
y=[]
x_cuadrado=[]
xy=[]
# se crean varias variables independientes de tipo lsita
cordenadax=float(input("Ingrese la coordenada X "))
cordenaday=float(input("Ingrese la coordenada Y "))
# se piden un  par de coordenadas iniciales
x.append(cordenadax)
x_cuadrado.append(cordenadax**2)
y.append(cordenaday)
xy.append(cordenadax*cordenaday)
# para cada una de las listas iniciales, se vn añadiendo segun cumplan o se les de distinto aparametro a la funcion
actual=float(input("Ingrese la parte X: "))
# se crea un ciclo que se mantendra activo simepre y cuando no ingrese un espaio el usuario
while actual != '':
    actx=float(actual)
    acty=float(input("Ingrese la parte Y "))
    x.append(actx)
    x_cuadrado.append(actx**2)
    y.append(acty)
    xy.append(actx*acty)
    actual=input("Ingrese la parte X: ")
sumx=sum(x)
sumy=sum(y)
mediax=sum(x)/len(x)
mediay=sum(y)/len(y)
# la linea 266 es la aplicacionde la formula exactamtene como see encuentra en la pagina del libro
m=(sum(xy)-(sumx*sumy/len(x)))/(sum(x_cuadrado)-(sumx**2/len(x)))
b=mediay-m*mediax
print("y =",m,"x+",b)

#%%Ejercicio 118:HUGO(Me faltan comenatiso)

"""Descripcion del problema:
Una baraja estándar de naipes contiene 52 cartas. Cada carta tiene uno de cuatro palos
junto con un valor. Los palos son normalmente espadas, corazones, diamantes y tréboles, 
mientras que los valores son del 2 al 10, jota, reina, rey y as.
Cada naipe se puede representar con dos personajes. El primer carácter es el valor de 
la carta, con los valores del 2 al 9 representados directamente. Los caracteres "T", "J",
"Q", "K" y "A" se utilizan para representar los valores 10, Jota, Reina, Rey y As 
respectivamente. El segundo carácter se utiliza para representar el traje.
de la tarjeta. Normalmente es una letra minúscula: "s" para espadas, "h" para corazones, 
"d" para diamantes y "c" para tréboles. La siguiente tabla proporciona varios ejemplos 
de cartas y sus representaciones de dos caracteres.
Comience escribiendo una función llamada createDeck. Utilizará bucles para crear una 
baraja completa de cartas almacenando las abreviaturas de dos caracteres de las 52 
cartas en una lista. Devuelve la lista de tarjetas como único resultado de la función. 
Su función no tomará ningún parámetro.
Escribe una segunda función llamada barajar que aleatorice el orden de las cartas en una lista. Una técnica que se puede utilizar para barajar las cartas es visitar cada elemento de la lista y cambiarlo por otro elemento aleatorio de la lista. Debes escribir tu propio bucle para barajar las cartas. No puedes utilizar la función aleatoria integrada de Python
función.
Utilice las dos funciones descritas en los párrafos anteriores para crear un programa 
principal que muestre una baraja de cartas antes y después de barajarla. Asegúrese de
que su programa principal solo se ejecute cuando sus funciones no se hayan importado a 
otro archivo."""
#Importamos randrange para generar un numero aleatorio
from random import randrange


def createDeck():
    """
    

    Parameters
    ----------
    exp_postfija : expresión en forma postfija

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    #Creamos dos lista una con los valores que toman las cartas y otra con los palos
    suits = ['s', 'h', 'd', 'c']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    #Hacemos una lista vacia, donde se mostrara una baraja de cartas
    deck = []
    #Hacemos un ciclo donde se le agregara a la lista deck la suma de los elementos 
    #de un elemento de suits y uno de deck
    for s in suits:
        for v in values:
            deck.append(v+s)
            #import pdb; pdb.set_trace()
       
        return deck

def swapPositions(lista, pos1, pos2):
    """
    

    Parameters
    ----------
    lista, posicion 1 y posicion 2

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    elemento1 = lista[pos1]
    elemento2 = lista[pos2]
    
    indexelemento1 = deck.index(elemento1)
    firstElement = lista.pop(pos1)
    
    indexelemento2 = deck.index(elemento2)
    secondElement = lista.pop(pos2)
    
    lista.insert(indexelemento2, secondElement)
    lista.insert(indexelemento1, firstElement)
    return lista
    

def shuffle(lista):
    for element in lista:
        pos1 = deck.index(element)
        pos2 = randrange(len(lista))
        while(pos1==pos2):
            pos2 = randrange(len(lista))
        #print ("posicion1" + str(pos1))
        #print ("posicion2" + str(pos2))
        lista = swapPositions(deck, pos1, pos2)
        #import pdb; pdb.set_trace()

    return lista
def main():
    deck = createDeck()
    print(deck)
    shuffle(deck)
if __name__="__main__":
    main()
    


#import pdb; pdb.set_trace()
#%%Ejercicio 120: Ya esta ordenada una lista(Me falta main)
#%%Ejercicio 125: La lista contiene una sublista(me falta main)