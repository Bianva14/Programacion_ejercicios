# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 00:00:11 2021

@author: pc1
"""

#%%Ejercicio 135: Anagramas:
    
"""Dos palabras son anagramas si contienen todas las mismas letras, pero en diferentes
pedido. Por ejemplo, "evil" y "life" son anagramas porque cada uno contiene una e, una
i, una l y una v. Cree un programa que lea dos cadenas del usuario, determina
sean o no anagramas, e informa el resultado.
"""
def characterCounts(s):
    #Creamos un diccionario vacio
    counts = {}
    #Actualiza el recuento de cada caracter de la cadena
    for ch in s:
        if ch in counts:
            counts[ch]=counts[ch]+1
        else:
            counts[ch]=1
        #Regresa el recuento
        return counts
#Determinar si dos cadenas ingresadas por el usuario son anagramas
def main():
    #Lee las cadenas ingresadas por los usuarios
    s1=input("Enter the first string:")
    s2=input("Enter the second string:")
    #Obtenga el recuento de caracteres para cada cadena
    counts1 = characterCounts(s1)
    counts2 = characterCounts(s2)
    #Mostrar el resultado
    if counts1==counts2:
        print("Those strings are anagrams.")
    else:
        print("Those strings are not anagrams")
#Mandar a llamar main
main()
#%%Ejercicio 136: Otra vez anagramas
"""La noción de anagramas se puede extender a varias palabras. Por ejemplo, 
"William Shakespeare" y "Soy un ortográfico débil" son anagramas cuando se 
ignoran las mayúsculas y los espacios.
Amplíe su programa del ejercicio 135 para que pueda comprobar si dos frases son anagramas.
Su programa debe ignorar las mayúsculas, los signos de puntuación y el espaciado al tomar 
la determinación."""
def characterCounts(h):
    #Creamos un diccionario vacio
    counts = {}
    #Actualiza el recuento de cada caracter de la cadena
    for ch in s:
        if ch in counts:
            counts[ch]=counts[ch]+1
        else:
            counts[ch]=1
        #Regresa el recuento
        return counts
#Determinar si dos cadenas ingresadas por el usuario son anagramas
def mainn():
    #Lee las cadenas ingresadas por los usuarios
    s1=input("Enter the first string:")
    s2=input("Enter the second string:")
    #Obtenga el recuento de caracteres para cada cadena
    import string 
    #Eliminamos los signos d epuntuacion
    s1 = ''.join([i for i in s1 if i not in string.punctuation]) 
    s2 = ''.join([i for i in s2 if i not in string.punctuation])    
    #Eliminamos los espacios y convertimos en letras minúsculas
    s1 = s1.replace(" ", "").lower()
    s1 = s2.replace(" ", "").lower()
    counts1 = characterCounts(s1)
    counts2 = characterCounts(s2)
    #Mostrar el resultado
    if counts1==counts2:
        print("Those strings are anagrams.")
    else:
        print("Those strings are not anagrams")
#Mandar a llamar main
mainn()
"No huo complicaciones"