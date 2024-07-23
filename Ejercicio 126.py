# -*- coding: utf-8 -*-
"""
@author: Bianca Ramirez Mejia
"""

"""DESCRIPCION DEL EJERCICIO 126
Generar todas las sublistas de una lista
Usando la definición de una sublista de ejercicio 125, escriba una función que 
devuelva una lista que contiene todas las posibles sublistas de una lista. Por 
ejemplo, las sublistas de [1, 2, 3] son [], [1], [2], [3], [1, 2], [2, 3] y 
[1, 2, 3]. Tenga en cuenta que su función siempre devolverá una lista que 
contenga al menos la lista vacía porque la lista vacía es una sublista de todas
las listas. Incluya un programa principal que demuestre su función mostrando 
todas las sublistas de varias listas diferentes."""

##Creamos una funcion TodasSublistas donde se ocupa la lista donde se sacaran las sublistas
def TodasSublistas(lista):
    #comenzamos con una lista vacía como la única sublista de lista
    sublists = [[]]
    
    #Genera todas las sublistas de lista de la longitud de la lista.
    for length in range (1, len(lista) + 1):
        #Genera la sublista que comienza en cada índice
        for i in range(0, len(lista) - length + 1):
            #Agrega la sublista actual a la lista de sublistas
            sublists.append(lista[i : i + length])
    #Regresa el resultado
    return sublists
#Demuestre que la funcion TodasSublistas
def main():
    print("Las sublistas de [] son:")
    print(TodasSublistas([]))
    
    print("Las sublistas de [1] son:")
    print(TodasSublistas([1]))
    
    print("Las sublistas de [1, 2] son:")
    print(TodasSublistas([1,2,3]))
    
    print("Las sublistas de [1,2,3,4] son:")
    print(TodasSublistas([1, 2, 3, 4]))
#Llama la funcion main
main()
