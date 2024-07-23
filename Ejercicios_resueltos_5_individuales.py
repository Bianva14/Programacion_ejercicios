# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 17:09:37 2021

@author: pc1
"""

#%%Ejercicio 105: Reverse Order(INDIVIDUAL)((Me falta las descripcion y poner espacio entre numeros de reverse)
"""
@autor: Bianca Ramirez Mejia 421117321
Ejercicio individual

Descripcion del problema:
Escriba un programa que lea enteros del usuario y los almacene en una lista. Utilice 0 como
un valor centinela para marcar el final de la entrada. Una vez leídos todos los valores
su programa debe mostrarlos (excepto el 0) en orden inverso, con un valor
que aparecen en cada línea.
Descripcion de la solucion:
"""
enteros= input("Escribe los numeros enteros que quieres que se orden")
enteroslis= list(enteros) 
def ReverseOrder(enteroslis):
    if enteroslis == []:
        return enteroslis
    else:
        reversa = [enteroslis[-1]] + ReverseOrder(enteroslis[:-1])
    return reversa
   
print(ReverseOrder(enteroslis))

#%%Ejercicio 109: Lista de divisores adecuados(INDIVIDUAL)
"""
Descripcion del problema:
Un divisor propio de un entero positivo, n, es un entero positivo menor que n que divide 
uniformemente en n.Escribe una función que calcule todos los divisores propios de un positivo
entero. El entero se pasará a la función como su único parámetro. La función
devolverá una lista que contiene todos los divisores adecuados como único resultado. Completo
este ejercicio escribiendo un programa principal que demuestra la función leyendo
un valor del usuario y muestra la lista de sus divisores adecuados. Asegúrese de que su
El programa principal solo se ejecuta cuando su solución no se ha importado a otro archivo."