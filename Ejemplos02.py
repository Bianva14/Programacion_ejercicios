# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 16:21:27 2021

@author: Programación 2021-2
"""
def total_tiros(n=500):
    from Funciones import esta_en_rectangulo3 as meer, aleatorio_entre as ae
    #n = 500
    tiros = 0
    for i in range(n):
        valido = 0
        general = 0    
        
        while not valido == 10:
            resultado = meer(ae(3, 10), ae(3, 10))
            general +=1
            if resultado == "dentro":
                valido +=1 
        tiros += general
    promedio = tiros/n
    return promedio

N = 50
lista_tiros = [ total_tiros()  for i in range(50)]    
print(sum(lista_tiros)/N)