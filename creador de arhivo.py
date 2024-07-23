# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 15:34:42 2022

@author: pc1
"""

import os
file = open("/ruta/filename.txt", "w")
file.write("Primera línea" + os.linesep)
file.write("Segunda línea")
file.close()