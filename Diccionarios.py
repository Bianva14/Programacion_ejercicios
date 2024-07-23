# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 14:43:00 2021

@author: pc1
"""

#Pedro 1
#Juan  3
#Karla 5
#Luis  4
#Hugo  2

listAsignaciones = [('Pedro',1), ('Juan',3), ('Karla',5), ('Luis',4), ('Hugo',2)]

for (nombre, num) in listAsignaciones:
    if nombre == 'Hugo':
        print (num)
        

dictAsginaciones = {'Pedro':1,'Juan':3,'Karla':5, 'Luis':4, 'Hugo':2}
dictAsginaciones['Juanchin'] = 99

dictAsginaciones2 = {}
dictAsginaciones2['Pedro'] = 1
dictAsginaciones2['Juan'] = 3
dictAsginaciones2['Karla'] = 5
dictAsginaciones2['Luis'] = 4
dictAsginaciones2['Hugo'] = 2

print (dictAsginaciones)
print (dictAsginaciones2)

print (dictAsginaciones['Hugo'])

for key in dictAsginaciones:
    print (key+" "+str(dictAsginaciones[key]))
    
    #import pdb; pdb.set_trace()