# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 16:05:05 2022

@author: Bianca Ramirez Mejia no.cuenta:421117321
"""
#%%Ejercicio 164:Total de los valores
"""
@autor: Bianca Ramirez Mejia  no.cuenta:421117321
Ejercicio 164:Total de los valores
Descripcion del ejercicio:
Escriba un programa que lea los valores del usuario hasta que se ingrese una línea en blanco.
Muestra el total de todos los valores ingresados por el usuario (o 0.0 si el primer valor 
ingresado es una línea en blanco). Complete esta tarea usando la recursividad. Es posible
que su programa no utilice bucles.

Sugerencia: el cuerpo de su función recursiva necesitará leer un valor del usuario y luego 
determinar si debe o no realizar una llamada recursiva. Su función no necesita tomar ningún 
parámetro, pero deberá devolver un resultado numérico.
"""
#Calcular el total de una colección de números ingresados por el usuario ingresará una 
#línea en blanco para indicar que no se ingresarán más números

#Calcular el total de todos los números ingresados por el usuario ingresa una línea en 
#blanco devuelve el total de los valores ingresados

def leeryTotal():
    
    #Lee un valor que ingresa el usuario
    linea = input("Ingresa un numero (en blanco para salir): ")
    
    #Caso base: El usuario ingresa un linea en blanco entonces el total es 0
    if linea == "":
        return 0
    else:
    #Caso recursivo: Convierta la línea actual en un número y use la recursividad para leer
    #la siguiente línea
        return float(linea)+leeryTotal()

#Lee una colección de números del usuario y muestra el total
def main1():
    #Lee los valores del usuario y calcula el total
    total = leeryTotal()
    #Muestra el resultado
    print("El total de todos los valores es ", total)
#Llama a la funcion main
main1()
if __name__ =="__main__":
    main1()
"""No hubo complicacion alguna,estuvo muy bien explicado"""
#%% Ejercicio 167:Palíndromo recursivo
"""
@autor: Bianca Ramirez Mejia no.cuenta:421117321
Ejercicio 167: Palíndromo recursivo
Descripcion del ejercicio:
La noción de palíndromo se introdujo previamente en el ejercicio 72. En este ejercicio 
escribirás una función recursiva que determina si una cuerda es un palíndromo o no. 
La cadena vacía es un palíndromo, al igual que cualquier cadena que contenga solo un 
carácter. Cualquier cadena más larga es un palíndromo si su primer y último carácter 
coinciden, y si la cadena formada al eliminar el primer y último carácter también es 
un palíndromo.
Escriba un programa principal que lea una cadena del usuario. Utilice su función
recursiva para determinar si la cadena es un palíndromo o no. Luego muestre un mensaje 
apropiado para el usuario.
Escriba una función recursiva que calcule la distancia de edición entre dos cadenas.
Utilice el siguiente algoritmo:
    Sean s y t las cadenas
    Si la longitud de s es 0
      Return la longitud de t
    Else if si la longitud de t es 0 entonces
      Return la longitud de s
    Else
      Establecer el costo en 0
      If el ultimo caracter en s no es igual al ultimo caracter en t entonces 
         Establecer el costo en 1
      Establecer d1 igual a la distancia de edicion entre todos los caracteres excepto 
      la ultima en s, y todos los caracteres en t, mas 1
      Establecer d2 igual a la distancia de edicion entre todos los caracteres en s y 
      todos los caracteres excepto el ultimo en t, mas 1
      Establecer d3 igual a la distancia de edicion entre todos los caracteres excepto
      el ultimo en s, y todos los caracteres excepto el ultimo en t, mas costo
    Return el minimo de d1,d2 y d3
"""
#Determine si una cadena ingresada por el usuario es un palíndromo usando recursividad
##Determine si una cadena es un palindromo s es la cadena a checar, nos regresara True si
#la cadena es un palindromo. Falso en el caso contrario
def Palindromo(s):
    """

    Parameters
    ----------
    s : cadena

    Returns
    -------
    True si la cadena es un palindromo
    Falso en el caso contrario

    """
    #Caso base: Una cadena vacia es un palindrimo. Entonces esta cadena contiene solo un caracter
    if len(s) <= 1:
        return True
    #Caso recursivo:La cadena es un palindromo solo si el primer y ultimo caracter coinciden,
    #y el resto de la cadena es un palindromo
    return s[0] == s[len(s)-1] and Palindromo(s[1 : len(s) - 1])
#Revisa si la cadena ingresada por el usuario es un palindromo
def main():
    #Lee lo que introduce el usuario
    line = input("Introduzca una cadena: ")
    
    #Checa el estatus y muestra el resultado
    if Palindromo(line):
        print("Este es un palindromo!")
    else:
        print("Esta no es un palindromo.")
#Llma a la funcion main
main()
if __name__ =="__main__":
    main()

"""Solo tuve algunas complicaciones en entender a que se referia con palindromo, y en la
traduccion pero me sirvio mucho buscar algunas palabras en solitario para entender el sentido
de la traduccion"""
#%%Ejercicio 169:Distancia de edición de cadena
"""
@autor: Bianca Ramirez Mejia no.cuenta:421117321
Ejercicio 169: Distancia de edicion de cadena
Descripcion del ejercicio:
La distancia de edición entre dos cadenas es una medida de su similitud: cuanto menor es 
la distancia de edición, más similares son las cadenas con respecto al número mínimo de 
operaciones de inserción, eliminación y sustitución necesarias para transformar una cadena
en la otra.
Piense en las cadenas kitten and sitting. La primera cadena se puede transformar en 
la segunda cadena con las siguientes operaciones: Sustituya la k por una s, sustituya la 
e por una i e inserte una g al final de la cadena. Este es el menor número de operaciones
que se pueden realizar para transformar a un gatito en un asiento.
Como resultado, la distancia de edición es 3.
"""
#Calcula y muestra la distancia de edicion de dos cadenas

##Calcular la distancia de edición entre dos cadenas como un recuento del número mínimo
#de operaciones de inserción, eliminación y sustitución necesarias para transformar una
#cadena en el pedido
def DistanciaEdicion(s, t):
    """

    Parameters
    ----------
    s: una cadena
    t: otra cadena
    TYPE:
        Cadenas.

    Returns
    -------
    numero
        Nos regresa la distancia de edición entre dos cadenas

    """
    #Si una cadena es vacia, entonces la distancia de edicion es una operacion de insertar
    #para cada letra en una cadena
    if len(s) == 0:
        return len(t)
    elif len(t) == 0:
        return len(s)
    else:
        cost = 0
        #Si el ultimo caracter no es igual establecer el costo en 1
        if s[len(s) -1] != t[len(t) - 1]:
            cost = 1
    #Calcula tres distancias
    d1 = DistanciaEdicion(s[0 : len(s)-1], t) + 1
    d2 = DistanciaEdicion(s, t[0 : len(t)-1]) + 1
    d3 = DistanciaEdicion(s[0 : len(s)-1], t[0 : len(t)-1]) +cost
    #Regresa la minima distancia
    return min(d1, d2, d3)
#Calcula la distancia de edicion entre las dos cadenas ingresadas
def main2():
    #Lee lo ingresado por el usuario
    s1=input("Escribe una cadena")
    s2=input("Escribe otra cadena")
    
    #Calcula y muestra el resultado
    print("La edicion de distancia entre %s y %s es %d." % \
          (s1, s2, DistanciaEdicion(s1, s2)))
#Llama a la funcion main2
main2()
if __name__ =="__main__":
    main2()
"""La unica complicacion que tuve en este problema fue comprender a lo que se referia 
a distancia de edicion, y un poco en la traduccion pero igualmente busque las palabras
para poder entender el sentido de la traduccion"""

#%%Ejercicio172
"""
Flores Cruz Daniela 318099567
Ejercicio 172: Secuencias de elementos

Solución:
    Lo que vamos hacer es crar tres funciones la primera es la que nos 
    va ir viendo que elementos inician con la ultima letra del elemento dado
    por el ususario
    esta función debe de tener dos parametros, el primero es la palabra que es el
    nombre del elemento y el segundo parametro es una lista que contiene todos
    los elementos que vamos a ir comparando con la ultim letra,
    ahora nuestro caso base es cuando el elemento o palabra inicial es una cadena
    vacía, en ese caso nos va a devolver una lista vacia pues no hay letras a comparara
    luego si no es una cadena vacía primero se crea una lista donde vamos a ir guardando 
    los elementos que le siguen a nuestro elemnto dado por el usuario, entonces para
    cada lera inicial de las palabras que estan el la lista de todos nuestros elementos
    lo vamos a ir comparando con la ultima letra del elemento dado así hasta que sea igual
    y cuando pase esto vamos hacer el llamdo de nuestra funcion para ir agregando el restante de la palabra
    e ir agregando a la lista que se va a mostrar
    
    La segunda función lo que hace es abrir nuestro archivo y en una lista que es la que se usa
    enla primera función va a ir agregando los elementos que tiene la lista
    
    Por ultimo vamos hacer la función principal para que pida al usuario el
    elemento y utilice las funciones ya hechas para mostrar el resultado
"""
#
#Determinar la secuencia más larga de elementos que pueden seguir a un elemento
# introducido por el usuario donde comienza cada elemento de la secuencia con
# la misma letra que la última letra si su predecesor
#
#from sys import *

elementos = "C:/Users/dan_f/Documents/programacion-2021-2/Ayudantias/elements.txt"

#Encuentra la secuencia más larga de palabras que empiezan por inicio, donde cada palabra
# comienza con la última letra de su predecesora.
#@param inicio la primera palabra de la secuencia
#@param la lista de palabras que pueden aparecer en la secuencia
#@devuelve la lista más larga de palabras que empiezan por inicio y que cumple con la
#Las restricciones de letras descritas anteriormente

def secuencia_mas_larga(start, words):
   """
    Esta es una función recuriva que va comparando la ultima letra de un elemento
    dado por ele usuario y va agregando el elemento que empieze con la ultima letra

    Parameters
    ----------
    start : STR
        DESCRIPTION. es el nombre del elemento dado por el usuario
    words : lista
        DESCRIPTION. Es la lista que contiene todos los elementos 

    Returns
    -------
    None.

    """
   #Caso base: Si inicio está vacío, la lista de palabras está vacía
   if start == "":
       return[]

   #Encuentra la mejor lista de palabras (la más larga) comprobando cada palabra posible
   #que podría aparecer a continuación en la secuencia
   best=[]
   last_letter =start[len(start)- 1].lower()
   for i in range(0,len(words)):
       first_letter = words[i][0].lower()
       #si la primera letra de la siguiente palabra coincide con la última letra de la palabra anterior
       if first_letter == last_letter:
           #Utiliza la recursión para encontrar una secuencia de palabras candidatas
           candidate = secuencia_mas_larga(words[i],\
                           words[0 : i ]+ words [i + 1:len(words)])
           #Guardar el candidato si es mejor que la mejor secuencia que hemos visto anteriormente
           if len(candidate)>len(best):
               best = candidate

   #Devuelve la mejor secuencia candidata, procurada por la palabra inicial
   return[start] + best 

#Carga los nombres de todos los elementos del fichero de elementos
#@devolver una lista de todos los nombres de los elementos
def cargarNombres():
    """
    Esa funcion solo obitne los elementos que tiene nustro archivo

    Returns
    -------
    names : TYPE lista
        DESCRIPTION. es la lista con todos los nombres de nuestros elementos 
        a comparar

    """
    names = []

    #Abrir el conjunto de datos de los elementos
    inf=open(elementos, "r")

    #Carga cada línea, almacenando el nombre del elemento en una lista
    for line in inf:
        line = line.rstrip()
        parts = line.split(",")
        names.append(parts[2])

    #cerrar el archivo y devolver la lista
    inf.close()
    return names

#Mostrar una secuencia más larga de elementos empezando por un elemento introducido por el usuario
def principal():
    """
    Esta es la función principal que pide al usuario dar un leemento y te regresara
    todos los elementos que empiezan con la ultima letra del elemento anterior

    Returns
    -------
    None.

    """
    #Carga todos los nombres de los elementos
    names = cargarNombres()

    #Leer el elemento inicial y ponerlo en mayúsculas
    start = input("Introduce el nombre de un elemento (en inglés): ")
    start = start.capitalize()

    #Eliminar el elemento inicial de la lista de elementos
    names.remove(start)

    #Buscar una secuencia más larga que empiece por estrella
    sequence = secuencia_mas_larga(start, names)

    #Mostrar la secuencia de elementos
    print("La secuencia más larga que empieza por", start, "es: ")
    for element in sequence:
        print(" ", element)

#Llamar a la función principal
principal()

"""
Para este ejercicio si tuve problemas, cuando li intente ejecutar vi que no
funcionaba, y cuando intentaba depurarlo no podía asi estuve bastante rato, 
despues creí que era por el archivo que solo debía de contener los elementos y no
como el archi original y cree uno pero tampoco era eso, luego lo volví a comparar
con el libro pero yo no notaba el error, entonces egí intentando, y volví hacer 
la depuracion y ví que estaba haciendo mal la depuración pues estaba apretando 
otro boton cuando quería entrar a la función, luego ya que pude ir depurando llegué
a la segunda función y ví que no seguía depurando entonces había un error, y el error
era que el indice no cincidía pues como lo dije anteriormente yo cree otro archivo que solo tenía 
los nombres de los elementos entonces ese indice no funcionaba, luego ya que pude resolver eso, 
cuando hacia la función principal hace uso de la primera entonces cuando entre a la primera
y ya llegaba a que la primera letra coincidia con la ultima del primer elemento algo había mal
y me indicaba que era porque faltaba uno de los parametros pero yo no enetendía el porque
hasta que lo volví arevisar y era porque el ultimo parentesis lo haía colocado mal
elo había puesto antes de mi segundo parametros, una vez que vi eso ya corrí el programa y funcionaba bien
igual volví a corregir la derección de mi archivo y listo
"""

#%%Ejercicio 174
"""
@autor: Flores Cruz Daniela 318099567

Ejercicio 174: Codificación de longitud de ejecución

Solución:
    Primero definicmos una funcion que es la que hará la codificación entonces
    primero le pedimos como parametro los datos o mas bien los caracteres de los cuales
    se va hacer la codificación, una ves teniendo los datos, si no tiene nada
    entonces no se regresa nada es decir vacio, ahora si no pasa esto vamos 
    a definir nuestro indice igual a uno y vamos a ir comparando  hasta que la 
    longitud de nuestros datos es menor que nuestro indice iguala  uno ya ademas
    el indice 1 de nuestros datos sea igual a el indice menos uno y cada que se repita este 
    ciclo a nuetsro indice se le va a ir sumando uno mas nuestro indice anterior
    Por ultimo regresamos nuestra lista con la codificació, creamos una función
    principla que use la funcion anterior, pida la cadena y muestra la codificación.
"""
##Realiza la codificación de longitud de ejecución en una cadena o lista de valores
# @param data la cadena o lista a codificar
# @devuelve una lista donde los elementos en posiciones pares son valores de datos y los
# elementos en posiciones impares son recuentos del número de veces que
# el valor de los datos antes de ser replicado
def encode(data):
    """
    Esta es una función recursiva que dado caracteres por el usuario nos 
    regresa la codificación de la longitud de dichos caracteres

    Parameters
    ----------
    data : TYPE str
        DESCRIPTION. son os caracteres de los cuales se va hacer la codificación

    Returns
    -------
    TYPE lista
        DESCRIPTION. nos regresa la codificación es decir los caracteres con sus
        apariciones

    """
    #Si los datos están vacíos, no es necesario codificarlos
    if len(data)==0:
         return[]
    #Encuentra el índice del primer elemento que no es el mismo que el elemento en la posición 0 de data
    index = 1
    while index<len(data) and data[index]== data[index - 1]:
         index = index + 1

    #Codificar el grupo de caracteres actual
    current = [data[0], index]
 
    #Usa la recursión para procesar los caracteres desde el índice hasta el final de la cadena
    return current + encode(data[index : len(data)])

#Demuestra la función de codificación
def main4():
    """
    Esta es la función principal que nos muestra la codificación de una cadena dada 
    por nuestro usuario

    Returns
    -------
    None.

    """
    #Leer una cadena del usuario
    s = input("Introduzca algunos caracteres ")

    #Mostrar el resultado
    print("Cuando se codifican esos caracteres, el resultado es: ")
    print(encode(s))

#Llamar a la función principal
main4()

"""
En general no tuve problemas con este ejercicio, ni con la traducción no al momento
de ejecutarlo, todo bien.
"""