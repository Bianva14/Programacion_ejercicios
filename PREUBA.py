# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 10:26:30 2022

@author: pc1
"""
import sys
sys.path.append(r'C:/Users/pc1/Documents/programacion-2021-2/fc/matematicas')
from package import module
from matematicas.algebra import Tales
t = Tales(['AB',12])
print(t)
t2 = Tales(['BC',6])
t.mul()
