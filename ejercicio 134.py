# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 23:56:31 2021

@author: Bianca Ramirez Mejia
"""

""" DESCRIPCION DEL EJERCICIO 134
Cree un programa que determine y muestre el número de caracteres únicos en un
cadena ingresada por el usuario. Por ejemplo, ¡Hola, mundo! tiene 10 caracteres 
únicos, whilezzz tiene un solo carácter único. Utilice un diccionario o un set 
para resolver este problema."""


"""Primero crearemos una funcion llamada numcaracteresunicos para mostrar el numero
de caracateres unicos de la cadena que se ingrese"""
def numcaracteresunicos(s): 
    #Definimos a la cadena ingresada como "s"
    s=input("escribe una cadena sin espacios")
    #Creamos una lista vacia para ir agregando cuales son los caracteres unicos
    unico_caracter = []
    #Creamos un ciclo for para repetir el proceso del if hasta que termine con todos los simbolos
    for simbolo in s:
        #Con el if not vemos que simbolos no estan en unico_caracter, si estan ya no se agregan
        if not simbolo in unico_caracter:
            unico_caracter.append(simbolo)
    #Este print nos muestra los caracteres unicos que tiene "s"         
    print(unico_caracter)        
    #La variable numcaracter obtiene la longitud de la lista unico_caracter       
    numcaracter=len(unico_caracter)
    print(numcaracter)


