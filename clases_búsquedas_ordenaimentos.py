# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 17:43:39 2022

@author: pc1
"""

#%%Burbuja

from geometria import tales

lista= [tales([3,6,7]).razon(),tales([6,8,9,]).razon(), tales([7,9,10]).razon(), tales([2,3,4]).razon(),
       tales([5,4,6]).razon()]
#lista= [tales([3,6,7]),tales([6,8,9,]), tales([7,9,10]), tales([2,3,4]),
       #tales([5,4,6])]
def burbuja(lista:list):
    l = lista.copy()
    if l==[]:
        return []
    else:
        for i in range(len(l)-1):
            if l[i]>l[i+1]:
                tmp = l[i]
                l[i] = l[i+1]
                l[i+1] = tmp
        return burbuja(l[:-1]) + [l[-1]]
  

def burbuja_invertida(lista:list):
    l = lista.copy()
    if l == []:
        return []
    else:
        for i in range(len(l)-1,0,-1):
            if l[i-1] > l[i]:
                l[i-1], l[i] = l[i], l[i-1]
        return [l[0]] + burbuja_invertida(l[1:])
def coctel(lista):
    l = lista.copy()
    #if l != []:
    if len(l) > 1:
        for i in range(len(l)-1):
            if l[i]>l[i+1]:
                tmp = l[i]
                l[i] = l[i+1]
                l[i+1] = tmp
        for i in range(len(l)-2,0,-1):
            if l[i-1] > l[i]:
                tmp = l[i]
                l[i] = l[i-1]
                l[i-1] = tmp
        return [l[0]] + coctel(l[1:-1]) + [l[-1]]
    else:
        #return []
        return l
def insercion(lista):
    for i in range(len(lista)):
        for j in range(i,0,-1):
            if(lista[j-1] > lista[j]):
                aux=lista[j];
                lista[j]=lista[j-1];
                lista[j-1]=aux;
    return lista;
def merge_sort(arreglo):
    longitud = len(arreglo)
    mitad = longitud//2  # El doble / es para dividir y redondear hacia abajo
    # Condición de salida de recursividad es que el arreglo mida 1 o 0
    if longitud <= 1:
        return arreglo
    mitad_izquierda = arreglo[:mitad]
    mitad_derecha = arreglo[mitad:]
    mitad_izquierda = merge_sort(mitad_izquierda)
    mitad_derecha = merge_sort(mitad_derecha)
    return merge(mitad_izquierda, mitad_derecha)


def merge(izquierda, derecha):
    #print(f"Recibo {izquierda} y {derecha}")
    lista_ordenado = []
    indice_de_izquierda = 0
    indice_de_derecha = 0
    indice_lista_ordenado = 0
    # Recorremos ambos arreglos y vamos colocando los elementos ordenados. Colocamos siempre el que sea menor
    while indice_de_izquierda < len(izquierda) and indice_de_derecha < len(derecha):
        valor_izquierda = izquierda[indice_de_izquierda]
        valor_derecha = derecha[indice_de_derecha]
        if valor_izquierda <= valor_derecha:
            # El de la izquierda es menor, entonces lo ponemos primero
            lista_ordenado.append(valor_izquierda)
            # Y aumentamos en 1 el valor de la izquierda
            indice_de_izquierda += 1
        else:
            lista_ordenado.append(valor_derecha)
            indice_de_derecha += 1

        # Sin importar lo que hayamos movido, aumentamos el índice del actual
        indice_lista_ordenado += 1
    # Hasta aquí puede que el índice izquierdo o derecho hayan llegado a su fin, pero no ambos. Entonces
    # nos aseguramos de recorrerlos a ambos hasta el final
    while indice_de_izquierda < len(izquierda):
        lista_ordenado.append(izquierda[indice_de_izquierda])
        indice_de_izquierda += 1

    while indice_de_derecha < len(derecha):
        lista_ordenado.append(derecha[indice_de_derecha])
        indice_de_derecha += 1
    #print(f"Los ordeno y combino. Resultado: {lista_ordenado}.")
    return lista_ordenado

def seleccion(lista):
    for i in range(len(lista)):
        minimo=i;
        for j in range(i,len(lista)):
            if(lista[j] < lista[minimo]):
                minimo=j;
        if(minimo != i):
            aux=lista[i];
            lista[i]=lista[minimo];
            lista[minimo]=aux;
    return lista
     
      
                
            
def quicksort(lista, izquierda, derecha):
    if izquierda < derecha:
        indiceParticion = particion(lista, izquierda, derecha)
        quicksort(lista, izquierda, indiceParticion)
        quicksort(lista, indiceParticion + 1, derecha)


def particion(lista, izquierda, derecha):
    pivote = lista[izquierda]
    while True:
        # Mientras cada elemento desde la izquierda esté en orden (sea menor que el
        # pivote) continúa avanzando el índice
        while lista[izquierda] < pivote:
            izquierda += 1

        # Mientras cada elemento desde la derecha esté en orden (sea mayor que el
        # pivote) continúa disminuyendo el índice
        while lista[derecha] > pivote:
            derecha -= 1

        """
            Si la izquierda es mayor o igual que la derecha significa que no
            necesitamos hacer ningún intercambio
            de variables, pues los elementos ya están en orden (al menos en esta
            iteración)
        """
        if izquierda >= derecha:
            # Indicar "en dónde nos quedamos" para poder dividir el arreglo de nuevo
            # y ordenar los demás elementos
            return derecha
        else:
            # Nota: yo sé que el else no hace falta por el return de arriba, pero así el algoritmo es más claro
            """
                Si las variables quedaron "lejos" (es decir, la izquierda no superó ni
                alcanzó a la derecha)
                significa que se detuvieron porque encontraron un valor que no estaba
                en orden, así que lo intercambiamos
            """
            lista[izquierda], lista[derecha] = lista[derecha], lista[izquierda]
            """
                Ya intercambiamos, pero seguimos avanzando los índices
            """
            izquierda += 1
            derecha -= 1
    
def busquedar_secuencial(lista, v):
    esta = False
    if lista == []:
        esta = False
    elif lista != []:
        if v == lista[0]:
            esta = True
        elif v!=lista[0]:
            return busquedar_secuencial(lista[1:],v)
    return esta
def busqueda_binaria(lista, v):
    if lista == []:
        return False
    else:
        mitad = len(lista)//2
        if lista[mitad] == v:
            return True
        elif lista[mitad] < v:
            return busqueda_binaria(lista[mitad+1:], v)
        else:
            return busqueda_binaria(lista[:mitad], v)

lista_ordenanda_burbuja_invertida = burbuja_invertida(lista)        
lista_ordenanda_coctel = coctel(lista)
lista_ordenada_insercion = insercion(lista)
lista_ordenada_mezcla = merge_sort(lista)
#lista_ordenada_selccion = seleccion(lista)
#lista_ordenada_rapido= quicksort(lista, 0, len(lista)-1)
lista_ordenada_busquedar_secuencial = busquedar_secuencial(lista, 2.0)
lista_ordenanda_busqueda_binaria = busqueda_binaria(lista,2.0 )
print("Lista ordenada con burbuja_invertida")
print(lista_ordenanda_burbuja_invertida)
print("Lista ordenada con coctel")
print(lista_ordenanda_coctel)
print("Lista ordenada con inserccion")
print(lista_ordenada_insercion)
print("lista ordenada con mezcla")
print(lista_ordenada_mezcla)
seleccion(lista)
print("Despues de ordenarlo con seleccion")
print(lista)
quicksort(lista, 0, len(lista) - 1)
print("Después de ordenarlo con quicksort: ")
print(lista)
print("Busqueda secuencial, buscamos a 2.0")
print(lista_ordenada_busquedar_secuencial)
print("Busqueda binaria, buscamos a 2.0")
print(lista_ordenanda_busqueda_binaria)

