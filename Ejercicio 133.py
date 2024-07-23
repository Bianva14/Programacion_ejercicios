# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 14:22:25 2021

@author: pc1
"""

#940
#TODO 
#TIENEN CONVERTIR EL CODIGO EN UNA FUNCION/METODDO
#TIENE QUE PEDIR EL NUMERO DE ENTRADA AL USUARIO Y VERIFICAR QUE SEA UN NUMERO ENTRE 0 Y 999
#TIENE QUE IMPRIMER LA CADENA EN UNA SOLA LINEA
cientos = {100:"One Hundred", 
           200:"Two Hundred",
           300:"Three Hundred",
           400:"Four Hundred",
           500:"Five Hundred",
           600:"Six Hundred",
           700:"Seven Hundred",
           800:"Eight Hundred",
           900:"Nine Hundred",
          }

decenas = {20:"Twenty",
           30:"Thirty",
           40:"Fourty",
           50:"Fifty",
           60:"Sixty",
           70:"Seventy",
           80:"Eighty",
           90:"Ninety",
          }

unidades = {1:"One",
            2:"Two",
            3:"Three",
            4:"Four",
            5:"Five",
            6:"Six",
            7:"Seven",
            8:"Eight",
            9:"Nine",
            10:"Ten",
            11:"Eleven",
            12:"Twelve",
            13:"Thirteen",
            14:"Fourteen",
            15:"Fifteen",
            16:"Sixteen",
            17:"Seventeen",
            18:"Eighteen",
            19:"NineTeen"}

numero = 999
parteADosDigitosDelNumero = (numero % 100)
cientosEnElNumeros = (numero - parteADosDigitosDelNumero)
if cientosEnElNumeros in cientos:
    print(cientos[cientosEnElNumeros])

parteAUnDigitoDelNumero = parteADosDigitosDelNumero % 10
decenasEnElNumero = parteADosDigitosDelNumero - parteAUnDigitoDelNumero
if decenasEnElNumero in decenas:
    print (decenas[decenasEnElNumero])
    if parteAUnDigitoDelNumero in unidades:
        print (unidades[parteAUnDigitoDelNumero])
    
else:
    if parteADosDigitosDelNumero in unidades:
        print (unidades[parteADosDigitosDelNumero])

if numero == 0:
    print ("Zero")