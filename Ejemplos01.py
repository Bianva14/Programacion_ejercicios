# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 08:30:37 2021

@author: Programación 2021-2

"""

from Funciones import mostrar_promedio as mp

mp()
#%%
from Funciones import regresar_promedio as rp
promedio = rp()

#%%
from Funciones import regresar_promedio_conParametros as rpp
promedio = rpp(10,10,10,10,10)
print("El promedio del segundo semestre es: ", promedio)
#%%
from Funciones import Promedio as p
promedio = p([10,10,10,10,10, 10 ,10])
print("El promedio del segundo semestre es: ", promedio)

#%%
"""

"""
from Funciones import en_intervalo
resultado = en_intervalo(5,15,3)
print(resultado)
"""

"""
#%%
from Funciones import main_100ValoresAleatorio

main_100ValoresAleatorio()
#%%
from Funciones import velocidad_distancia_tiempo_con_verificacion as vdtv, \
    regresa_velocidad_distancia_tiempo_con_verificacion as rvdtv
r1 = vdtv(0,0)
r2 = rvdtv(0,0)
#%%
from Funciones import mostrar_esta_en_rectangulo as meer
meer()
#%%
from Funciones import mostrar_esta_en_rectangulo1 as meer
meer()
#%%
from Funciones import mostrar_esta_en_rectangulo2 as meer
meer()
#%%
from Funciones import esta_en_rectangulo3 as meer, aleatorio_entre as ae

resultado = meer(ae(3, 10), ae(3, 10))
print(resultado)
#%%
"""
Desc
Cuantas flechas es necesario lanzar para que 10 caigan dentro de 
la diana

Sol
Mientras no tenga diez lanzamientos válidos:
Lanzar una flecha: 
    * si está dentro de la diana sumamos un lanzamiento válido 
                                 y un lanzamiento en general
    * si no está dentro de la diana sumamos un lanzamianto en general
Se necesitaron los lanzamintos en general para tener diez válidos

"""
valido = 0
general = 0
from Funciones import esta_en_rectangulo3 as meer, aleatorio_entre as ae

#while valido != 10:
while not valido == 10:
    resultado = meer(ae(3, 10), ae(3, 10))
    if resultado == "dentro":
        valido +=1
        general +=1
    else:
        general +=1
print("Se requirieron ", general,"lanzamientos para obtener ",valido,
      "válidos")
#%%
"""
Desc
Cuantas flechas es necesario lanzar para que 10 caigan dentro de 
la diana

Sol
Mientras no tenga diez lanzamientos válidos:
Lanzar una flecha: 
    * si está dentro de la diana sumamos un lanzamiento válido 
                                 y un lanzamiento en general
    * si no está dentro de la diana sumamos un lanzamianto en general
Se necesitaron los lanzamintos en general para tener diez válidos

"""
valido = 0
general = 0
from Funciones import esta_en_rectangulo3 as meer, aleatorio_entre as ae

#while valido != 10:
while not valido == 10:
    resultado = meer(ae(3, 10), ae(3, 10))
    general +=1
    if resultado == "dentro":
        valido +=1        
print("Se requirieron ", general,"lanzamientos para obtener ",valido,
      "válidos")
#%%
"""
Desc
Cuántos lanzamientos en promedio se requieren para tener 
10 válidos

Sol

Realiza el programa anerior n numero de veces, 
sumando en una varible contador el numero de dardos lanzados 
para al final dividirlo entre n 

Podria ser que todo el código anterior lo metamos dentro de 
otro while al que le pongamos un contador i que cuando 
llegue a 10 veces repetidas todo el ciclo while sume los 
valores obtenidos de general y lo divida entre 10

tambien se podria con un for i in range?  
"""

from Funciones import esta_en_rectangulo3 as meer, aleatorio_entre as ae
n = 500
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
print("Se necesitan en promedio %d tiros para tener 10 válidos"
      %(promedio))
#%%











#%%
import fc
r = fc.mfinancieras.interes.monto_final(1000,.2,3)
print(r)