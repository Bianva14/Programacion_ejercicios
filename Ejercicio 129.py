# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 00:32:11 2021

@author: pc1
"""
#%% EJERCICIO 129, @author: Daniela Flores Cruz 318099567
"""
En este ejercicio vas a simular 1.000 tiradas de dos dados. Comience escribiendo
una función que simule el lanzamiento de un par de dados de seis caras.
Tu función no tomará ningún parámetro. Devolverá como único resultado el total 
que se ha tirado en los dos dados.
"""
# Simular el lanzamiento de dos dados muchas veces y comparar los resultados simulados
# con los resultados esperados por la teoría de la probabilidad.
#
from random import randrange

num_runs = 1000
d_max = 6

## Simular el lanzamiento de dos dados de seis caras
# @devuelve el total de tirar dos dados simulados

def dosDados():
    """
    Esta función solo te regresa el total de veces que se tienen al tirar 
    dos dados

    Returns
    -------
    TYPE
        Nos regresa un entero que son las veces al tirar dos dados

    """
    #Simular dos dados
    d1 =randrange(1,d_max+1)
    d2 =randrange(1,d_max+1)
    
    #Devuelve el total
    return d1+d2

#Simular muchas tiradas y mostrar el resultado 
def main_dosDados():
    """
    Esta funcion sumula nuestras tiradas de dos dados y nos muestra el
    resultado del porcentaje esperado y el porcentaje simulado.

    Returns
    -------
    None.

    """
    #Crea un diccionario de proporciones esperadas
    expected={2: 1/36, 3:2/36, 4: 3/36, 5:4/36,\
              6:5/36, 7:6/36, 8:5/36, 9:4/36,\
                  10:3/36, 11:2/36, 12:1/36}
    
    #Crear un diccionario que mapee desde el total de
    #dos dados al número de ocurrencias
    counts={2:0,3:0,4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0,12:0}
    
    #Simular las tiradas de num_runs, y contar cada tirada
    for i in range(num_runs):
        t = dosDados()
        counts[t]=counts[t]+1
        
    #Mostrar las proporciones simuladas y las proporciones esperadas
    print("Total  porcentaje   porcentaje")
    print("       simulado      esperado")
    for i in sorted(counts.keys()):
        print("%5d %11.2f %8.2f" \
              % ( i, counts[i]/num_runs*100, expected[i]*100))
"""
En este ejercicio como lo dije anteriormente, tuve un problema que en la transcripción
no me dí cuenta que cuando estaba definiendo mi diccionario en vez de = puse:
pero en general todo vien con la traducción y el código fue solo ese detalle que
no había notado
"""