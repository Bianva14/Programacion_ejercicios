# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 15:52:41 2021

@author: pc1
"""
import random

archivoPalabras = open("palabras151.txt", "r")
palabras = archivoPalabras.readlines()
archivoPalabras.close()
numPalabras = len(palabras)
password = ""

while(True):
   numRandom1 = random.randint(0, numPalabras-1)
   numRandom2 = random.randint(0, numPalabras-1)

   palabra1 = palabras[numRandom1]
   palabra2 = palabras[numRandom2]

   palabra1 = palabra1.strip().title()
   palabra2 = palabra2.strip().title()
   if len(palabra1) < 3:
       continue
   if len(palabra2) < 3:
       continue

   password = palabra1+palabra2  
   #print  (password)
   if len(password) >= 8 and len(password) <= 10:
       break
   else:
       continue

print (password)

