# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 00:54:33 2021

@author: Bianca Ramirez Mejia 421117321 Octaedros Dorados
"""
#%%Ejercicio 128: Reverse Lookup
"""
Created on Tue Nov 23 15:13:03 2021

@author: Bianca Ramirez Mejia
"""

"""Escriba una función llamada reverseLookup que encuentre todas las claves en un 
diccionario ese mapa a un valor específico. La función tomará el diccionario y 
el valor para buscar como sus únicos parámetros. Devolverá una lista (posible
mente vacía) de claves de el diccionario que se correlaciona con el valor 
proporcionado.
Incluya un programa principal que demuestre la función reverseLookup como parte
de su solución a este ejercicio. Su programa debe crear un diccionario y luego
mostrar que la función reverseLookup funciona correctamente cuando devuelve 
múltiples llaves, una sola llave y sin llaves. Asegúrese de que su programa 
principal solo se ejecute cuando el archivo que contiene su solución a este 
ejercicio no se ha importado a otro programa."""
"""Descripcion del ejercicio
Primero se creara la funcion reverselook con una lista vacia keys se iran agregando la 
llaves si cumplen que la lista diccionario[key] es igual a valor, despues la funcion
main nos demostrara si la funciion reverselookup es correcta, para ello le colocaremos
una lista y luego la evaluaremos 3 veces para obtenes los 3 posibilidades de listas de
llaves"""

##Definimos la funcion reverseLookup que tome el. diccionario y el valor del que se quiere la llave
def reverseLookup(diccionario, valor):
    #Creamos una lista abierta keys para agregar las llaves y que sean en lista
    keys = []
    #Checamos cada llave con el ciclo y el if para ir agregando las llaves si cumplen
    #que esa llave nos da el valor correcto
    for key in diccionario:
        if diccionario[key] == valor:
            keys.append(key)
    #Regresamos la lista keys        
    return keys
#Definimos la funcion principal que nos ayudara a saber si es correcto el programa
def main():
    #Definimos el diccionario frEn con palabras francesas y su traduccion en ingles
    frEn = {"le":"the", "la":"the","livre":"book", "pomme":"apple"}
    #Luego imprimimos los 3 casos que nos piden, el primero es que nos regrese multiples
    #llaves, el segundo que nos regrese una llave y por ultimo uno que no nos regrese llave
    print("Las palabra francesas para 'the' son:", reverseLookup(frEn, "the"))
    print("Expected: ['pomme'] ")
    print()
    print("The french word for 'asdf' is:", reverseLookup(frEn, "asdf"))
    print("Expected: []")
#Este if solo llama a la funcion main si el archivo no ha sido importado
if _name=="main_":
    main()
    
"""Lo que se me complico fue que no lograba comprender a que se referia el ejercicio
cuando comenta que se debia crear un diccionario, pues yo pensaba que se le debia 
pedir al usuario un par de listas y con estas crear un diccionario pero despues de inten
tarlo varias veces no logre completarlo, pero posteriormente me di cuenta de la solucion
del libro y me di cuenta que estaba mal, pues mas bien debiamos definir nuestra lista ejemplo"""
#%% Ejercicio 129: Simulación de dos dados
## EJERCICIO 129, @author: Daniela Flores Cruz 318099567
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
#%%Ejercicio 134: Caracteres unicos
"""
Created on Wed Nov 24 23:56:31 2021

@author: Bianca Ramirez Mejia
"""

""" DESCRIPCION DEL EJERCICIO 134
Cree un programa que determine y muestre el número de caracteres únicos en un
cadena ingresada por el usuario. Por ejemplo, ¡Hola, mundo! tiene 10 caracteres 
únicos, whilezzz tiene un solo carácter único. Utilice un diccionario o un set 
para resolver este problema."""
"""Descripcion del ejercicio 134:
Lo que haremos preguntarle al usuario la cadena para despues tomar los simbolos
y con estos si cumplen que no estan en la lista vacia unico_caracter(donde van a guardarse
los caracteres unicos) entonces se agregaran en la lista y si ya se encuentran no se gregaran
con esto ya obtenemos una lista con los caracteres unicos, por ultimo para saber cuantos
caracteres se tienen con la funcion len se mide la longitud de la lista y este resultado
es el numero de caracteres en la cadena ingresada"""
    

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
"""Complicaciones:
Lo unico complicado fue comprender a que se referia con caracteres unicos pero, 
me di cuenta facilmente con el ejemplo de ¡Hola, mundo!"""
#%% Ejercicio 138:Tarjeta Bingo
import random
#tarjetaBingo = {'B':[0-15], 'I':[16-30], 'N':[31-45], 
#                'G':[46-60], 'O':[61-75]}

tarjetaBingoRangos = {'B':range(1,16), 
                'I':range(16,31), 
                'N':range(31,46),
                'G':range(46,61),
                'O':range(61,76)}

def genera5NumEnRango(num_ini, num_fin):
    listaNum = []
    random.randint(num_ini, num_fin)
    while (len(listaNum) < 5):
        numAleatorio = random.randint(num_ini, num_fin)
        if not numAleatorio in listaNum:
            listaNum.append(numAleatorio)
   
    
    return listaNum

def generaTarjetaBingo():
    tarjetaBingo = {}
    tarjetaBingo['B'] = genera5NumEnRango(1,15)
    tarjetaBingo['I'] = genera5NumEnRango(16,30)
    tarjetaBingo['N'] = genera5NumEnRango(31,45)
    tarjetaBingo['G'] = genera5NumEnRango(46,60)
    tarjetaBingo['O'] = genera5NumEnRango(61,75)

    return tarjetaBingo

def impTarjetaBingo(tarjetaBingo):
    print ("B\tI\tN\tG\tO")
    for index in range(0,5):
        cadenAImprime = str(tarjetaBingo['B'][index])+"\t"
        cadenAImprime += str(tarjetaBingo['I'][index])+"\t"
        cadenAImprime += str(tarjetaBingo['N'][index])+"\t"
        cadenAImprime += str(tarjetaBingo['G'][index])+"\t"
        cadenAImprime += str(tarjetaBingo['O'][index])+"\t"
        print(cadenAImprime)
        
def verificaTarjetaBingo(tarjetaBingo):
    for key in tarjetaBingo:
        if len(tarjetaBingo[key]) != 5:
            return False
        for ele in tarjetaBingo[key]:
            if not ele in tarjetaBingoRangos[key]:
                return False
        listaVerificadora = []
        for ele in tarjetaBingo[key]:
            if ele in listaVerificadora:
                return False
            else:
                listaVerificadora.append(ele)
        
    return True

#def verificaTarjetaGanadora(tarjetaBingo):
    

tarjetaBingo = {'B':[1,10,6,4,2], 
                'I':[16,23,19,20,22], 
                'N':[31,40,39,42,35],
                'G':[46,50,51,52,49], 
                'O':[61,75,70,69,67]}

impTarjetaBingo(generaTarjetaBingo())
#print(verificaTarjetaBingo(generaTarjetaBingo()))      

#impTarjetaBingo(tarjetaBingo)
#print(verificaTarjetaBingo(tarjetaBingo)