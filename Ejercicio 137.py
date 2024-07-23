# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 00:35:26 2021
@author: Daniela Flores Cruz 318099567
Ejercicio 137: Puntuación de Scrabble™
(Resuelto-18 líneas)

En el juego de Scrabble™, cada letra tiene puntos asociados. La puntuación 
total de una palabra es la suma de las puntuaciones de sus letras. 
Las letras más comunes valen menos puntos mientras que las menos comunes 
valen más puntos. A continuación se muestran los puntos asociados a cada letra:

Un punto
A, E, I, L, N, O, R, S, T y U

Dos puntos
D y G

Tres puntos
B, C, M y P

Cuatro puntos
F, H, V, W e Y

Cinco puntos
K

Ocho puntos
J y X

Diez puntos
Q y Z

Escribe un programa que calcule y muestre la puntuación de Scrabble™ de una palabra.
Crea un diccionario que relacione las letras con los valores de los puntos. 
A continuación, utiliza el diccionario para calcular la puntuación.

Un tablero de Scrabble™ incluye algunas casillas que multiplican el valor de
una letra o el valor de una palabra entera. En este ejercicio ignoraremos 
estas casillas.
Solución:
    Primero creamos un diccionario que tenga los valores que le corresponde
    a cada una de las letras en el abecedario, luego le pedimos al 
    usuaro la palabra que quiere que se calcule y la volvemos mayuscalas
    todas sus letras para no tener problema al momento de asignarle un valor, 
    igual creamos una variable que nos va a ir sumando los valores que tiene 
    cada una de las letras en la palabra, con un ciclo vamos recorriendo cada 
    una de las letrs de nuestra palabra y con un contador vamos agregando
    los valores, por ultimo mostramos su palabra y su valor.
"""
##
# Utiliza un diccionario para calcular la puntuación Scrable TM de una palabra.
#

#Inicializar el diccionario para que mapee las letras de la forma a los pines
puntos ={"A":1, "B":3, "C":3, "D":2, "E":1, "F":4,\
         "G":2,"H":4,"I":1,"J":2,"K":5,"L":1, \
        "M":3,"N":1,"O":1,"P":3,"Q":10,"R":1,\
            "S":1,"T":1,"U":1,"V":4,"W":4,"X":8,"Y":4,"Z":10}

#Leer una palabra del usuario
palabra = input("Introduzca una palabra: ")

#Calcular la puntuación de la palabra
mayusculas = palabra.upper()
puntuacion=0
for ch in mayusculas:
    puntuacion = puntuacion + puntos[ch]
    
#Mostrar el resultado
print(palabra, "vale", puntuacion, "puntos")
"""
En este ejercicio no tuve problemas, ni de traducción, ni de comprender el 
código, de hecho este programa me gusto se me hizo interesante pues
ya he jugado este juego de mesa.
"""
#%%Ejercicio 106: Eliminar los valores extremos
""" 
@author: Erika Giebele Martinez Mares
Ben Stephenson. (2014). The Python Workbook. Switzerland: Springer., 
Exercise 106: Remove Outliers(Eliminar los valores extremos)

Descripción del problema:
Cuando se analizan los datos recogidos como parte de un experimento científico, 
puede ser conveniente eliminar los valores más extremos antes de realizar otros 
cálculos. Escribe una función que tome como parámetros una lista de valores y 
un número entero no negativo, n. La función debe crear una nueva copia de la 
lista con los n elementos más grandes y los n elementos más pequeños eliminados. 
A continuación, debe devolver la nueva copia de la lista como único resultado 
de la función. El orden de los elementos en la lista devuelta no tiene que 
coincidir con el orden de los elementos en la lista original. Escribe un programa 
principal que demuestre tu función. Su función debe leer una lista de números 
del usuario y eliminar de ella los dos valores más grandes y los dos más pequeños. 
Muestre la lista con los valores atípicos eliminados, seguida de la lista original. 
Su programa debe generar un mensaje de error apropiado si el usuario introduce 
menos de 4 valores. 
Traducción realizada con la versión gratuita del traductor www.DeepL.com/Translator

Descripción de la solución del problema:
    Se creará la función eliminarLosValoresAtípicos la cual estará encargada de
ordenar los datos y elimina los valores atípicos, es decir, los valores máximos
y mínimos de la lista de datos y devolverá una lista sin estos, después se definira
la función main la cual leerá los valores del usuario hasta que se introduzca 
una línea negra(un enter en blanco) y los almacenará en la lista valores, para 
después tras eliminar los valores atípicos mostrar ambas entradas, es decir, tanto 
la lista con los datos atípicos, como la lista sin ellos.
"""
##
# Eliminar los valores atípicos de un conjunto de datos.
# 

## Eliminar los valores atípicos de una lista de datos 
# @param data la lista de valores de datos a procesar
# @param num_valoresatípicos el número de valores más pequeños y más grandes a eliminar
# @devuelve una nueva copia de los datos en la que los valores están ordenados de forma ascendente
# orden ascendente y los valores más pequeños y más grandes han sido eliminados

from mer_5 import eliminarLosValoresAtípicos, main
eliminarLosValoresAtípicos()
main()
"""Los valores atípicos más pequeños y más grandes podrían eliminarse utilizando 
el mismo ciclo. En esta solución se utilizan dos ciclos para aclarar los pasos.
En este ejercicio solo hubo un problema no quedaba claro a qué se refería con 
línea negra para salir, intente con todos los caracteres parecidos (|,/,\,-,_) 
pero ninguno funciono, busque en internet pero literalmente salen líneas negras. 
Al final el ejercicio se refiere a un enter sin ningún dato.
En lo demás todo resultó bastante claro, en cuanto a los restante de la traducción 
no hubo ningún problema al igual que al entender las funciones definidas en este. 
"""


#%%Ejercicio 108: Negativos, Ceros y Positivos 
"""
@author: Erika Giebele Martinez Mares
Ben Stephenson. (2014). The Python Workbook. Switzerland: Springer., 
Exercise 108: Negatives, Zeros and Positives (Negativos, Ceros y Positivos)

Descripción del problema:
Cree un programa que lea los números enteros del usuario hasta que se introduzca 
una línea en blanco. Una vez leídos todos los números enteros, el programa debe mostrar 
todos los números negativos, seguidos de todos los ceros y de todos los números 
positivos. Dentro de cada grupo, los números deben mostrarse en el mismo orden 