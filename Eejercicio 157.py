# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 15:49:34 2021

@author: pc1
"""

 
carpeta = "C:/Users/HRodriguez/Desktop/BabyNames/"

nombres_ninas = []
for n in range(1900, 2013):
    a = open(carpeta + str(n) + "_GirlsNames.txt","r")
    nombres_ninas.append(a.readlines())
    a.close()
    
    
    solo_nombre_nina = []
    for m in nombres_ninas: 
        for o in m:
            solo_nombre_nina.append(o.split()[0])
    nombres_de_ninas = []
    for t in solo_nombre_nina:
        if not t in nombres_de_ninas:
            nombres_de_ninas.append(t)
            
            
print("Los nombres de niñas usados del año 1990 - 2012 fueron: ")            
print(nombres_de_ninas)