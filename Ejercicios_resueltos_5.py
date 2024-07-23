# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 00:40:15 2021

@author: Bianca Ramirez Mejia 421117321 Octaedros Dorados
"""
#%%Ejercicio 104: Sorted Order (Orden de clasificación)
"""
@author: Vasquez Matias Cynthia Noemi, 318218364
Ben Stephenson. (2014). The Python Workbook. Switzerland: Springer., 
Ejercicio 104: Sorted Order (Orden de clasificación)

Descripción del problema:
Escribe un programa que lea enteros del usuario y los almacene en una lista.
Su programa debe continuar leyendo valores hasta que el usuario introduzca 0.
Entonces debe mostrar todos los valores introducidos por el usuario (excepto
el 0) en orden de menor a mayor, con un valor que aparezca en cada línea.
Utilice el método de ordenación o la función 'sorted' para ordenar la lista.

Descripción de la solución del problema:
Primero se creará una lista vacía y cada vez que el usuario introduzca un número
este se irá agregando a esa lista, siempre y cuando este entero sea distinto de
0, pues en ese caso se dejarán de agregar los valores y es cuando se mostrará
la lista de todos los enteros que se introdujeron exceptuando el 0. 
"""
##
# Muestra los enteros introducidos por el usuario en orden ascendente.
#

# Comienza con una lista vacía
datos = []

# Leer los valores, añadiéndolos a la lista, hasta que el usuario introduzca 0
num = int(input("Introduzca un número entero (de 0 a salir): "))
while num != 0:
    datos.append(num)
    num = int(input("Introduzca un número entero (0 para salir): "))

# Ordenar los valores
datos.sort()

"""
La invocación del método 'sort' en una lista reordena los elementos de la lista
en orden. El uso del método 'sort' es apropiado para este problema porque no hay
necesidad de mantener una copia de la lista original. La función 'sorted' puede
utilizarse para crear una nueva copia de la lista en la que los elementos estén
ordenados. La llamada a la función ordenada no modifica la lista original. Por
lo tanto, se puede utilizar en situaciones en las que la lista original y la
lista ordenada se necesitan simultáneamente.
"""

# Mostrar los valores en orden ascendente
print("Los valores, ordenados de forma ascendente, son:")
for num in datos:
    print(num)
"""
No hubo mayor problema al traducir el código pues todas las palabras se tradujeron
de manera correcta y con sentido de acuerdo a lo que se pedía.
En general el problema no presentó mayor dificultad, mas que saber la manera en
que estaba funcionando el while y el for en la parte final, pero al leerlo bien
fue fácil saber su funcionamiento.
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

#%%Ejercicio 107: Evitando duplicados
"""
Created on Thu Nov 18 15:16:25 2021

@author: Christian Feldhaus Hagemeister
"""
"@author: Christian Feldhaus Hagemeister"
"Ejercicio 107: Evitando duplicados"
"""
En este ejercicio, creará un programa que lee palabras del usuario hasta que
el usuario ingresa una línea en blanco. Después de que el usuario ingresa una 
línea en blanco, su programa debe mostrar cada palabra ingresada por el usuario 
exactamente una vez. Las palabras deben mostrarse en
el mismo orden en que fueron ingresados. Por ejemplo, si el usuario ingresa:
    primero
    segundo
    primero
    tercero
    segundo
el programa debera mostrar:
    primero
    segundo
    tercero
"""

#Empezamos leyendo palabras a una lista
words = []
word = input("Escriba una palabra (Linea en blanco para finalizar): ")
while word != "":
    # Agregaremos la palabra a la lista solo si aun no está en ella.
    if word not in words:
        words.append(word)
    # Repetimos la instruccion para leer la siguiente palabra.
    word = input("Escriba una palabra (Linea en blanco para finalizar): ")

# Mostramos las palabras sin repetir ninguna.
for word in words:
    print(word)

"""
La transcripcion fue muy sencilla y el problema también lo era. No hubo problemas
lógicos ni de sintaxis.
Creo que lo más 'complicado' era agregar las palabras a la lista solo si no se 
habian ingresado antes.
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
en que fueron introducidos por el usuario. Por ejemplo, si el usuario introduce 
los valores 3, -4, 1, 0, -1, 0 y -2, su programa debe mostrar 
los valores -4, -1, -2, 0, 0, 3 y 1. Su programa debe mostrar cada valor en su 
propia línea

Traducción realizada con la versión gratuita del traductor www.DeepL.com/Translator

Descripción de la solución del problema:
    
Primero se crearán tres listas para almacenar los valores negativos, cero 
y positivos, después se leerán los valores ingresados por el usuario y se almacenarán
en sus respectivas listas, es decir, dependiendo de si son positivos negativos 
o el número cero, para esto usaremos ciclos for y while, se tendrá que introducir un 
espacio en blanco para salir, por último mostrará la lista en orden ascendente, 
primero se mostrarán todos los valores negativos, luego los ceros y al final los 
positivos.
    
"""

##
# Leer una colección de enteros del usuario. Muestra todos los números negativos,
# seguido de todos los ceros, seguido de todos los números positivos.
#

# Crear tres listas para almacenar los valores negativos, cero y positivos
negativos = []
ceros = []
positivos = []

# Leer todos los enteros del usuario, almacenando cada
# entero en la lista correcta
linea = input("Introduzca un número entero (en blanco para salir):  ")
while linea != "":
    num = int(linea)
    
    if num < 0:
      negativos.append(num)
    elif num > 0:
      positivos.append(num)
    else:
      ceros.append(num)

    #Leer la siguiente línea de entrada del usuario 
    linea = input("Introduzca un número entero (en blanco para salir):  ")
    
#Mostrar todos los valores negativos , luego todos los ceros, luego todos los valores positivos
print("Los números eran: ")

for n in negativos:
    print(n)
    
for n in ceros:
    print(n)
    
for n in positivos:
    print(n)
    
"""Esta solución utiliza una lista para llevar la cuenta de los ceros que se 
introducen. Sin embargo, como todos los ceros son iguales, no es necesario
guardarlos. En su lugar, se podría utilizar una variable entera para contar el 
número de ceros y luego mostrar esa cantidad de ceros más adelante en el programa.
En este ejercicio no se presentó ningún problema, tanto en la redacción como en 
la solución y su respectivo resultado, solo vi un video para recordar la forma 
en que funcionan los ciclos for.

Programación ATS. (2018, 30 diciembre). 38. Programación en Python | Bucles | Bucle For [Vídeo]. YouTube. https://www.youtube.com/watch?v=mRI8C2ZhDkg&t=385s
"""

#%%Ejercicio 109: Lista de divisores adecuados(INDIVIDUAL)
"""
Descripcion del problema:
Un divisor propio de un entero positivo, n, es un entero positivo menor que n que divide 
uniformemente en n.Escribe una función que calcule todos los divisores propios de un positivo
entero. El entero se pasará a la función como su único parámetro. La función
devolverá una lista que contiene todos los divisores adecuados como único resultado. Completo
este ejercicio escribiendo un programa principal que demuestra la función leyendo
un valor del usuario y muestra la lista de sus divisores adecuados. Asegúrese de que su
El programa principal solo se ejecuta cuando su solución no se ha importado a otro archivo."""
from me_5.py import mostrar_div_prop

if __name__ == "main":
    mostrar_div_prop()
"""Complicaciones
Tardarme en escribir el codigo"""
#%%Ejercicio 110: Perfect Numbers (Numeros perfectos)
"""
@author: Rojas Trejo Agustin Santiago, 318056045
Ben Stephenson. (2014). The python workbook : a brief introduction with 
exercises and solutions.
Ejercicio 110: Perfect Numbers (Numeros perfectos)

Descripción del problema:
Se dice que un número entero, n, es perfecto cuando la suma de todos 
los divisores propios de n es n. Por ejemplo, 28 es un número perfecto 
porque sus divisores propios son 1,2,4,7 y 14, y 1 + 2 + 4 + 7 + 14 = 28.
Escribe una función que determine si un entero positivo es o no perfecto. 
Su función tomará un parámetro. Si ese parámetro es un número perfecto 
entonces su función devolverá true. En caso contrario, devolverá falso. 
Además, escribe un programa principal que utilice su función para identificar 
y mostrar todos los números perfectos entre 1 y 10,000. Importe su solución 
al Ejercicio 109 cuando complete esta tarea.

Descripción de la solucion del problema:
Primero se crea la funcion isPerfect la cual determina si un número es perfecto
o no, primero obteniendo los divisores propios del número y despues verificando 
que la suma de los divisores propios sea el numero. Finalmente la funcion main 
aplica la función isPerfect para los numeros desde el 1 hasta el 10,000 y 
muestra los números que son perfectos.
"""

from tpw.mer_5 import main_isPerfect

# Llama a la función main.
main_isPerfect()

"""
No hubo mayor problema ni en la traduccion del ejercicio y solucion ni al 
resolver este ejercicio, lo unico que quedaba duda era en entender el 
significado de número perfecto y pensar en la correcta implementación de una 
funcion que regresara los divisores propios de un entero en formato de lista 
para que la demas solución del ejercicio pudiera llevarse a cabo como en el 
libro se indica.
"""

#%%Ejercicio 114: Números Aleatorios de la Lotería
"""
@author: Erika Giebele Martinez Mares
Ben Stephenson. (2014). The Python Workbook. Switzerland: Springer., 
Exercise 114: Random Lottery Numbers (Números Aleatorios de la Lotería)

Descripción del problema:
Para ganar el premio mayor de una lotería en particular, uno debe hacer 
coincidir los 6 números de su billete con los 6 números entre el 1 y el 49 que 
son sorteados por el organizador de la lotería. Escribe un programa que genere 
una selección aleatoria de 6 números para un billete de lotería. Asegúrese de 
que los 6 números seleccionados no contengan ningún duplicado. Muestre los 
números en orden ascendente.

Traducción realizada con la versión gratuita del traductor www.DeepL.com/Translator

Descripción de la solución del problema:
Este programa calcula números aleatorios distintos para un billete de lotería.
Primero importamos la función randrange del módulo random de python, después 
definiremos los valores máximos y mínimos que estarán en el boleto, de entre 1 y 49 
y la cantidad de numero en total que serán seis, después guardaremos en una 
lista de los números del ticket y haremos uso de la función randrange para generar 
los números del ticket con un ciclo while para de esta forma ir agregando números
que no estén en el ticket, al final ordenaremos los números en orden ascendente
y serán mostrados al usuario.
 
"""

##
# Calcula números aleatorios pero distintos para un billete de lotería.
#
from random import randrange

NUM_MIN = 1
NUM_MAX = 49
NUM_NUMS = 6

# Guarda una lista de los números del ticket
ticket_nums = []

# Generar NUM_NUMS números aleatorios pero distintos
for i in range(NUM_NUMS):
    # Generar un número que no esté ya en el ticket
    rand = randrange(NUM_MIN, NUM_MAX +1)
    while rand in ticket_nums:
        rand = randrange(NUM_MIN, NUM_MAX +1)
        
    #Agregar el número distinto al ticket  
    ticket_nums.append(rand)
    
#Ordenar los números en orden ascendente y mostrarlo
ticket_nums.sort()
print("Tus números son: ", end="")
for n in ticket_nums:
    print(n, end=" ")
print()
        
"""El uso de constantes facilita la reconfiguración de nuestro programa para 
otras loterías.
En este ejercicios solo se cambio la palabra bucle por la palabra ciclos pues 
esta última resulta más familiar, esto en cuanto a la traducción y en cuanto 
a la solución del problema solo bastó con ver un video para entender bien el uso 
del ciclo while en este caso.

Programación ATS. (2018a, diciembre 15). 37. Programación en Python | Bucles | Bucle While [Vídeo]. YouTube. https://www.youtube.com/watch?v=YEWxlbffgxE&t=156s"""
#%%Ejercicio 121: Count the Elements (Contar los elementos)
"""
@author: Vasquez Matias Cynthia Noemi, 318218364
Ben Stephenson. (2014). The Python Workbook. Switzerland: Springer., 
Ejercicio 121: Count the Elements (Contar los elementos)

Descripción del problema:
La biblioteca estándar de Python incluye un método llamado count que determina
cuántas veces aparece un valor específico en una lista. En este ejercicio,
crearás una nueva función llamada countRange que determina y devuelve el número
de elementos dentro de una lista que son mayores o iguales a algún valor mínimo
y menores a algún valor máximo. Tu función tomará tres parámetros: la lista, el
valor mínimo y el valor máximo. Devolverá un resultado entero mayor o igual a 0.
Incluya un programa principal que demuestre su función para varias listas
diferentes, valores mínimos y valores máximos. Asegúrese de que su programa
funciona correctamente tanto para listas de enteros como para listas de números
de punto flotante.

Descripción de la solución del problema:
Importaremos la función 'main' para que se nos muestre lo que queremos del
problema.
"""
from tpw.mer_5 import main
# Llama al programa principal
main()
"""
El único problema que tuve fue que al inicio no recordaba cómo se debía importar
una función y también había importado las dos funciones del problema, pero
sólo una de ellas era la que me regresaba lo que quería, además de que en esa
función ya estaba incluída la primera función entonces no había necesidad de
importar ambas funciones.
"""

#%%Ejercicio 122: Tokenizar una cadena
"@author: Christian Feldhaus Hagemeister"
"Ejercicio 122: Tokenizar una cadena"

"""
La tokenización es el proceso de convertir una cadena en una lista de subcadenas, 
conocida como tokens. En muchas circunstancias, es mucho más fácil trabajar con 
una lista de tokens que la cadena original porque la cadena original puede tener 
un espaciado irregular. En algunos casos también se requiere un trabajo sustancial 
para determinar dónde termina una ficha y la siguiente comienza.
En una expresión matemática, los tokens son elementos como operadores, números y
paréntesis. Algunos tokens, como *, /, ˆ, (y) son fáciles de identificar porque el
token es un solo carácter, y el caracter nunca es parte de otro token. El + y
- son un poco más difíciles de manejar porque pueden representar
el operador de suma o resta, o pueden ser parte de un token numérico.
Hint: Un + o - es un operador si el carácter que no es un espacio en 
blanco inmediatamente antes de que sea parte de un número, o si el carácter que 
no es un espacio en blanco inmediatamente antes es un paréntesis cerrado. 
De lo contrario, es parte de un número.
Escriba una función que tome una cadena que contenga una expresión matemática como su
único parámetro y lo divida en una lista de tokens. Cada token debe estar entre paréntesis,
un operador, o un número con un + o - opcional al principio (para simplificar, vamos a
trabajar solo con números enteros en este problema). Devuelve la lista de tokens como el 
resultado de la funcion.
Puede suponer que la cadena pasada a su función siempre contiene un código válido,
una expresión matemática formada por paréntesis, operadores y números enteros. 
Sin embargo, su función debe manejar cantidades variables de espacios en blanco 
entre estos elementos. Incluya un programa principal que demuestre su función de 
tokenización que lea una expresión del usuario e imprima la lista de tokens. 
Asegúrese de que el programa principal no se ejecutará cuando el archivo que contiene 
su solución se importe a otro programa.
"""

#Convertir una expresion matemática a una lista de tokens

def tokenList(s):
    #vamos a remover los espacios en blanco de s
    s = s.replace(" ", "")
    # hacemos un ciclo para todos los caracteres de la cadena
    # identificamos los tokens y los añadimos a la lista
    tokens = []
    i = 0
    while i < len(s):
        # resolvemos los tokens que son siempre un solo caracter (,/,*,(and))
        if s[i] == "*" or s[i] == "/" or s[i] == "^" or s[i] == "(" or s[i] == ")":
            tokens.append(s[i])
            i = i + 1
        # resolvemos para + y -
        elif s[i] == "+" or s[i] == "-":
        # si hay un caracter previo y es un numero o un corchete de cierre
        # entonces el + o el - es un token en si mismo
            if i > 0 and (s[i-1] >= "0" and s[i-1] <= "9" or s[i-1] == ")"):
                tokens.append(s[i])
                i = i + 1
            else:
                # el + o el - es parte de un numero
                num = s[i]
                i = i + 1
                
                # seguimos añadiendo caracteres al token mientras sean digitos
                while i < len(s) and s[i] >= "0" and s[i] <= "9":
                    num = num + s[i]
                    i = i + 1
                tokens.append(num)
        elif s[i] >= "0" and s[i] <= "9":
            num = ""
            # seguimos añadiendo caracteres al token mientras sean digitos
            while i < len(s) and s[i] >= "0" and s[i] <= "9":
                num = num + s[i]
                i = i + 1
            tokens.append(num)
        
        # cualquier otro caracter significa que la expresión no es válida.
        # regresar una lista vacia para indicar que ocurrio un error
        else:
            return []
    return tokens

# Leer una expresion del usuario y tokenizarla, mostrando el resultado.

def main():
    exp = input("Ingrese una expresion matemática: ")
    tokens = tokenList(exp)
    print ("Los tokens son: ",tokens)

# Llamar la funcion main solo si el archivo no ha sido importado
if _name_ == "_main_":
    main()                         
                
"""
La transcrpicion de enste problema fue muy complicada debido a que hay muchos niveles
en el codigo, se requirieron multiples revisiones para corrobarar que cada condicional
y cada ciclo estuviera en el nivel indicado.
Creo que el codigo es complejo y usa muchisimas cosas que hemos visto.
tantos i´s y 1´s tambien fueron complicados de transcribir.
"""
#%%Ejercicio 126: Genera todas las sublistas de una lista
from me_5 import main
main()
#%%Ejercicio 127: La criba de Erastostenes
"""
@author: Daniela Flores Cruz 318099567
Ejercicio 127
(Resuelto-33 Líneas)

La criba de Eratóstenes es una técnica que se desarrolló hace más de 2.000 años
para encontrar fácilmente todos los números primos entre 2 y algún límite,
digamos 100. A continuación se describe el algoritmo:
Escriba todos los números desde el 0 hasta el límite
Tacha el 0 y el 1 porque no son primos
Establece p igual a 2
Mientras p sea menor que el límite, haz tachar todos los múltiplos de p (pero no el propio p)
Poner p igual al siguiente número de la lista que no esté tachado
Informar de que todos los números que no han sido tachados son primos 
La clave de este algoritmo es que es relativamente fácil tachar cada n números
en un papel. Esto también es una tarea fácil para un ordenador: un bucle for
puede simular este comportamiento cuando se proporciona un tercer parámetro
a la función range. Cuando un número es tachado, sabemos que ya no es primo,
pero sigue ocupando espacio en el papel y debe seguir siendo considerado cuando
se calculen los números primos posteriores. Por lo tanto, no se debe simular que
se tacha un número eliminándolo de la lista. En su lugar, debes simular que
tachas un número sustituyéndolo por el 0. Entonces, una vez que el algoritmo
se completa, todos los valores distintos de cero en la lista son primos.

Crea un programa en Python que utilice este algoritmo para mostrar todos
los números primos entre 2 y un límite introducido por el usuario.
Si implementas el algoritmo correctamente deberías ser capaz de mostrar todos
los números primos menores de 1.000.000 en unos pocos segundos.

Este algoritmo para encontrar números primos no es el único mérito de Eratóstenes.
Entre sus otros logros cabe destacar el cálculo de la circunferencia de la
Tierra y la inclinación del eje terrestre. También fue bibliotecario jefe de
la Biblioteca de Alejandría.

Descripción de la solución:
    Primero pedimos el limite hasta donde se darán los numeros primos, se crea
    una lista vacia en la cual iremos agregando toso los numero e ir anulando 
    con un cero, entonces con un cliclo for que tenga un rango desde cero hasta
    el limite que nos dan y los vamos agregar esos numeros a nuestra lista,
    luego hacemos cero el 1, y comenzamos hacer cero aquelos que son multiplos
    de dos y de ,35,7, una vez que tenemos los numeros que eran multiplos de
    2,3,5,7 tachados (son ceros) ahora si, consideramos a todos los que no son 
    cero y se los mostramos al usuario.
    
"""

##
# Determina todos los números primos para 2 hasta algún límite introducido
# por el usuario utilizando la Criba de Eratóstenes.
#
#Leer el límite del usuario
limite = int(input("Generar todos los primos hasta qué límite?"))

#Generar todos los números desde el 0 hasta el límite
nums=[]
for i in range(0, limite +1):
    nums.append(i)
    
#"Tacha" el 1 sustituyéndolo por un 0
nums[1]=0

#Tachar todos los múltiplos de cada número primo que descubramos
p = 2
while p < limite:
    #Tacha todos los múltiplos de p (pero no el propio p)
    for i in range(p*2, limite + 1, p):
        nums[i]= 0
    
    #Busca el siguiente número que no esté tachado
    p = p + 1
    while p <limite and nums[p]== 0:
        p = p+1
        
#Mostrar el resultado
print("Los primos hasta", limite, "son:")
for i in nums:
    if nums[i]!=0:
        print(i)
        
"""
En este ejercicio si estuve bastante tiempo porque no me salia, 
el problema es que cuando hice tal cual la transcripción 
el programa no corría, entonces lo que hice fue utilizar el debuger y el problema es
que cuando entra al ciclo while p< limite ese ciclo no tiene un fin, pues p nunca será 
menor que el limite, eso si lo pude resolver haciendo que cada que se hace el ciclo vaya 
aumentando así:
lo que pasa es que cuando empzamos a hacer 
p = 2
while p < limite:
  #Tacha todos los múltiplos de p (pero no el propio p)
  for i in range(p*2, limite + 1, p):
  nums[i]=0
aquí p nunca a llegar a ser mayor que nuestro limite, entonces lo que yo hice fue
hacer crcer mi p para que justamente llegara a un punto que cuando me recorra
mi rango p sea mayor que el limite, y lo que pense fue hacer un contador
y a p volver a sumarle p asu hasta que acabe mi rango
pero una vez que solucione eso, si ya corría el ejercicio pero no me regresaba
los primos y eso me dí cuenta porqué cuando consideré el  número 50, luego le 
pedía ayuda al profesor Lus pero el me dijo que si estaba bien, entonces volvía 
checar todo el ejercicio y el problema fue que no lo estaba viendo bien, lo que 
pasa es que yo estapa copiando el segundo ciclo que es considerar a p< limite 
y que nums[p]==0  fuera del primer ciclo es decir, consideré dos ciclos distintos entonces
cada que corria mi ejercicio no pasaba por ese ciclo pues estaba afuera y ademas no
se cumplían las condiciones, luego ya que vi ese preoblema lo corregí, pero aun 
asi segia habiendo un problema y es que no borre por completo todo el código que yo había
creado, si no que deje una variable que me incrementaba el valor de p segun yo
para que se terminara el ciclo, pero este aumento hacia que mi segundo ciclo while
dentro del primer ciclo while no funcionará y de nuevo no lo ví, entonces volví
a revisar el código de nuevo linea por linea, y observe que justo era eso, estaba 
poniendo una variable de más que había considerado "para resolver que estaba mal
el código".
Una vez que borré esa variable, entonces lo volví a correr y efectivamente 
si corría bien el código.
"""
"""Descripcion del problema:
Lo que necesitamos es crear una lista vacia que tendra a todas nuestras sublistas
y para obtener las sublistas lo que necesitamos hacer es conocer la longitud de la lista
para que con ello ocupar el indice para crear una sublista."""

from tpw.mer_5 import main
#Llama a la funcion main
main()

"""Complicaciones:
Fue un poco dificil traducir el ejercicio y poder entender el objetivo del ejercicio,
al igual que se me complico un poco comprender el significado de range(1, len(lista)+1
pero despues de repasar la funcion range me quedo muchisimo mas claro"""
