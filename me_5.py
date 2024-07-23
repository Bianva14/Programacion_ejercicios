# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 17:13:36 2021

@author: pc1
"""
#%%Ejercicio 105: Reverse Order(INDIVIDUAL)
"""
@autor: Bianca Ramirez Mejia 421117321
Ejercicio individual

Descripcion del problema:
Escriba un programa que lea enteros del usuario y los almacene en una lista. Utilice 0 
como un valor centinela para marcar el final de la entrada. Una vez leídos todos los
valores su programa debe mostrarlos (excepto el 0) en orden inverso, con un valor
que aparecen en cada línea.
Descripcion de la solucion:
"""
#enteros= input("Escribe los numeros enteros que quieres que se orden")
#enteroslis= list(enteros) 
#definimos la funcion ReverseOrder que tiene como entraa la lista que quiere que se ponga en orden inverso
def ReverseOrder(enteroslis):
    """

    Parameters
    ----------
    enteroslis : TYPE
        DESCRIPTION.

    Returns
    -------
    lista
        Nos regresa la lista con el orden inverso

    """
    #Si la lista es vacia nos debe regresar la misma
    if enteroslis == []:
        return enteroslis
    #En lo contrario, ocupamos la recursividad para que nuestra lista se ponga en orden inverso
    #Al ultimo elemento de la lista se convierte en lista y se le agrega el ultimo elemento que quedo asi
    #sucesivamente hasta llegar a un elemento al primer elemento
    else:
        reversa = [enteroslis[-1]] + ReverseOrder(enteroslis[:-1])
        return reversa 
#Definimos main que le pregunta al usuarion la lista para que despues se envie a ReverOrder()
def main():
    enteroslis = list(input("Escribe los numeros enteros que quieres que se ordenen"))
    print(ReverseOrder(enteroslis))   
main()
if __name__ =="__main__":
    main()
"""Complicaciones:
No hubo ninguna complicacion solo me tarde un poco"""    
    


    

#%%"Ejercicio 109: Lista de divisores propios"
"""
Descripcion de la solucion:
Un divisor propio de un entero positivo, n, es un entero positivo menor que n que divide 
uniformemente en n.Escribe una función que calcule todos los divisores propios de un 
positivo entero. El entero se pasará a la función como su único parámetro. La función
devolverá una lista que contiene todos los divisores adecuados como único resultado.
Completo este ejercicio escribiendo un programa principal que demuestra la función leyendo
un valor del usuario y muestra la lista de sus divisores adecuados. Asegúrese de que su
El programa principal solo se ejecuta cuando su solución no se ha importado a otro 
archivo."""
"Solución del problema"
#Definimos la funcion divi_prop que se le metera como dato el entero del cual se 
#quieren sus divisores propios
def divi_prop(n):
    """
    

    Parameters
    ----------
    n : entero del cual obtenemos los divisores propios

    Returns
    -------
    Lista : lista de los divisores propios de n.

    """
    Lista = []
    #Dividimos el número ingresado entre los numeros entre el 2 y n+1     
    for i in range(2, n+1):
        division = n / i
        #Si el resultado de la division es entera lo agreamos a lista
        if division == int(division): 
            Lista.append(division)
     
    return Lista
def main():
    """
    

    Returns
    -------
    None.

    """
    n = int(input("Ingresa un numero: ")) # pedimos al usuario ingresar un número
    div_propp = divi_prop(n) 
    print(div_propp) # imprimimos la lista despues de obtener los divisores
    
if __name__ == "__main__":
    main()   
    
""" No lograba entender a que se referia con divisores propios hasta que investigue"""
#%%Ejercicio 111: Solo palabras(INDIVIDUAL)
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
su archivo no ha sido importado a otro programa.

Descripcion de la solucion:"""

def palabras(texto):
    """
    

    Parameters
    ----------
    texto : una cadena ingresada por el usuario

    Returns
    -------
    Lista : Con las palabras ingresadas por el usuario

    """
    #Definimos una lista con los signos de ortografia
    signos = [",",".","¿","?","-","´","¡","!",":",";"] 
    #separamos las palabras de la cadena y las convertimos en una lista                 
    listapalabras=texto.split(" ") 
    #Creamos dos cadenas vacias
    palabrass = ""
    signo = ""
    #Revisamos si el ultimo simbolo en listapalabras esta en signos,para eliminarlo y 
    #ademas si hay un signo en medio de la palabra dejarlo
    for palabra in listapalabras:
        for x in palabra:
            if x in signos:
                signo += x
            palabra = palabra.replace("´"," ")
            for y in range(len(signo)):
                palabra = palabra.replace(signo[y]," ") 
        #Cuando hayamos eliminado o dejado los simbolos correctos en la palabra, 
        #entonces con esto separamos la palabras del texto y  la convertimos en listas
        palabrass=palabra.split()
        #Imprimos las listas
        print(palabrass)
        #print(textoo)

def main():
    """
    

    Returns
    -------
    None.

    """
    #Pedimos al usuario que ingrese una cadena
    texto=input("escribe la una cadena de texto")
    #llamamos a la funcion palabra y le metemos como parametro el texto ingresado
    palabras(texto)
if __name__=="__main__":
    main()
        
"Me atore muchisimo en definir que no se eliminaran los apostrofes en medio de una palabra"


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

def PromNum(Numeros):
    """
    

    Parameters
    ----------
    Numeros : Es la lista de numeros a el que le sacaremos los promedios

    Returns
    -------
    int
         Nos va a regresar los promedios con algunos print

    """
    #Creamos listas vacias y definimos la suma como cero para ir agregando elementos 
    #a la lista y a la suma(sumando los numeros)        
    suma = 0
    debajo_del_prom= []
    promedio = []
    arriba_del_prom = []
    #Creamos un ciclo for para sumar los valores de los numeros de la lista y 
    #despues dividirlo entre su longitud
    for numeros in Numeros:
        suma +=numeros        
    n = suma/len(Numeros)
    print(n)
    #Creamos otro ciclo for para que nos regrese los numeros que estan debajo del promedio
    #los que son iguales a el promedio y por ultimo los que estan arriba del promedio
    for numeros in Numeros:
        if numeros<n:
            debajo_del_prom.append(numeros)
        elif numeros == n:
            promedio.append(numeros)
        else:
            arriba_del_prom.append(numeros)    
    #Imprimimos los 3 posibles resultados de los promedios     
    print("Los números debajo del promedio son", debajo_del_prom )

    print("Si hay números iguales al promedio son" , promedio)

    print("Los números encima del promedio son", arriba_del_prom )

def main():  
    """
    Programa principal, muestra la función PronNum con parametro los Numeros 
    indicados por el usuario

    Returns
    -------
    None.

    """
    NNumeros = input("Ingrese los numeros para sacar sus promedios, al final de los numeros colocar un espacio: ") 
    Numeros=[int(x) for x in NNumeros]
    print(PromNum(Numeros))
main()
if __name__=="__main__":
    main()
"""Complicaciones:
Hacer que el programa no tomara al espacio en blanco para obtener los promedios"""
#%%Ejercicio 119:Repartir manos de cartas
"""Ejercicio 119: Repartir manos de cartas
(44 líneas)
En muchos juegos de cartas, a cada jugador se le reparte un número específico de cartas 
después de barajar la baraja. Escribe una función, repartir, que toma el número de manos,
el número de cartas por mano y una baraja de cartas como sus tres parámetros. Tu función
debería devolver una lista que contenga todas las manos que se repartieron. Cada mano se 
representará como una lista de cartas.
Al repartir las manos, su función debe modificar la baraja de cartas que se le pasa como 
parámetro, eliminando cada carta de la baraja a medida que se agrega a la mano de un 
jugador.
Cuando se reparten cartas, se acostumbra dar a cada jugador una carta antes de que 
cualquier jugador reciba una carta adicional. Su función debe seguir esta costumbre al 
construir las manos para los jugadores.
Use su solución al Ejercicio 118 como ayuda para construir un programa principal que crea
y baraja una baraja de cartas y luego reparte cuatro manos de cinco cartas cada una.
Muestre todas las manos de cartas, junto con las cartas que quedan en la baraja después 
de que se hayan repartido las manos."""
import random
 
suits = ['s', 'h', 'd', 'c']
values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
deck = []
for v in values:
    for s in suits:
        carta = "{} de {}".format(v,s)
        deck.append(carta)
random.shuffle(deck)

for i in range(0,40,4):
    for j in range(4):
        print("{:14}".format(deck[i+j]), end=" ")
    print()
print()
#Repartir cartas
jugadores = [[],[],[],[]]
for i in range(5):
    for j in range(4):
        jugadores[j].append(deck.pop(0))
#Mostrando las cartas restantes
for i in range(0,20,4):
    for j in range(4):
        print("{:14}".format(deck[i+j]), end=" ")
    print()
#%%Ejercicio 120: Ya esta ordenada una lista?(Me faltan comentarios)
"""Escriba una función que determine si una lista de valores está ordenada o no
(ya sea ascendente o descendente). La función debe devolver True si la lista es
ya ordenado. De lo contrario, debería devolver False. Escribe un programa principal
que lea una lista de números del usuario y luego usa su función para informar si
la lista está ordenada."""

def Ordena(s):
    """
    

    Parameters
    ----------
    s : valores que tiene la lista

    Returns
    -------
    string : Nos dice si esta o no ordenada

    """
    h=list(s)
    listaa=[int(i) for i in h]
    if listaa==sorted(listaa):
        print("La lista esta ordenada de forma ascendente")
        #return True
    else:
        print("la lista no esta ordenada de forma ascendente")
def mostrar_Ordena():
    s=input("Escribe una lista de numeros para ver si esta ordenada")
    Ordena(s)
mostrar_Ordena()
if __name__=="__main__":
    mostrar_Ordena()
    


#%%Ejercicio 125:¿Una lista contiene una sublista?(Me falatn comentarios)
"""Descripcion del problema:
Una sublista es una lista que forma parte de una lista más grande. Una sublista puede
ser una lista que contenga un solo elemento, varios elementos o incluso ningún elemento.
Por ejemplo, [1], [2], [3] y [4] son todas sublistas de [1, 2, 3, 4]. La lista [2, 3] 
también es una sublista de [1, 2, 3, 4], pero [2, 4] no es una sublista [1, 2, 3, 4] 
porque los elementos 2 y 4 no son adyacentes. en la lista más larga. La lista vacía es 
una sublista de cualquier lista. Como resultado, [] es una sublista de [1, 2, 3, 4]. Una
lista es una sublista de sí misma, lo que significa que [1, 2, 3, 4] también es una 
sublista de [1, 2, 3, 4]. En este ejercicio, creará una función, isSublist, que determina 
si una lista es una sublista de otra. Su función debe tomar dos listas, más grande y más
pequeña, como sus únicos parámetros. Debería devolver True si y solo si más pequeño es
una sublista de más grande. Escribe un programa principal que demuestre tu función."""
def isSublist(smaller1, larger1):
    smaller=[int(i) for i in smaller1]
    larger=[int(j) for j in larger1]  
    if len(smaller)==0:
        print("TRUE")
        return True
    if larger==smaller:
        print("TRUE")
        return True
    if len(smaller)>len(larger):
        print("FALSE")
        return False
    for v in smaller:
        if v not in larger:
            print("FALSE")
            return False
    return True
def mostrar_isSublist():
    smaller1=list(input("Escribe la sublista que queremos verificar"))
    larger1= list(input("Escribe la lista"))
    isSublist(smaller1, larger1)
mostrar_isSublist()
if __name__=="__main__":
    mostrar_isSublist()    
        
    