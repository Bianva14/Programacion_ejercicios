# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 14:46:47 2021

@author: pc1
"""
#%%Ejercicio 118
from random import randrange

def createDeck():
    suits = ['s', 'h', 'd', 'c']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    deck = []
    for s in suits:
        for v in values:
            deck.append(v+s)
            #import pdb; pdb.set_trace()
       
        return deck

def swapPositions(lista, pos1, pos2):
    elemento1 = lista[pos1]
    elemento2 = lista[pos2]
    
    indexelemento1 = deck.index(elemento1)
    firstElement = lista.pop(pos1)
    
    indexelemento2 = deck.index(elemento2)
    secondElement = lista.pop(pos2)
    
    lista.insert(indexelemento2, secondElement)
    lista.insert(indexelemento1, firstElement)
    return lista
    

def shuffle(lista):
    for element in lista:
        pos1 = deck.index(element)
        pos2 = randrange(len(lista))
        while(pos1==pos2):
            pos2 = randrange(len(lista))
        #print ("posicion1" + str(pos1))
        #print ("posicion2" + str(pos2))
        lista = swapPositions(deck, pos1, pos2)
        #import pdb; pdb.set_trace()
   
    return lista
deck = createDeck()
print(deck)
shuffle(deck)

#import pdb; pdb.set_trace()
    