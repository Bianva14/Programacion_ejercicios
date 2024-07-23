# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 00:16:26 2021

@author: pc1
"""

"""La criba de Eratóstenes es una técnica que se desarrolló hace más de 2.000 años
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
el problema es que cuando hice tal cual la transcripción 
el programa no corría, entonces lo que hice fue utilizar el debuger y el problema es
que cuando entra al ciclo while p< limite ese ciclo no tiene un fin, pues p nunca será 
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
los primos y eso me dí cuenta porqué cuando consideré el  número 50, luego le 
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