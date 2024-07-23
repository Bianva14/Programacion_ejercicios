# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 14:17:11 2021

@author: pc1
"""

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
#print(verificaTarjetaBingo(tarjetaBingo))  