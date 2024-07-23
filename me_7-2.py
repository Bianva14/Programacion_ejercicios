# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 14:00:28 2022

@author: Bianca Ramirez Mejia 421117321
"""
#%%Ejercicio 144:Numerar las lineas en un archivo(ya)
"""
Cree un programa que agregue números de línea a un archivo. El usuario leerá el
nombre del archivo de entrada, al igual que el nombre del nuevo archivo que
creará su programa.
Cada línea del archivo de salida debe comenzar con el número de línea, seguido 
de dos puntos y un espacio, seguido de la línea del archivo de entrada.
"""

def numlinea(archivo, nuearchivo):
    """
    

    Parameters
    ----------
    archivo : La direccion del archivo a analizar
    nuearchivo : El nombre del archivo que se creara 

    Returns
    -------
    nuearchivo : El nuevo archivo con una linea mas 

    """
    #Abrimos el archivo que ingreso el usuario
    archivo_r = open(archivo, 'r') 
    #Abrimos un nuevo archivo
    nuevoarchivo = open(nuearchivo, 'w')
    #Creamos una variables con el valor 1 para que     
    inicio = 1
    #Creamos un ciclo para que lea las lineas del archivo que ingreso el usuario
    for lineas in archivo_r:
        numerolinea = nuevoarchivo.write(str(inicio) + ":" +lineas)
        #Cuando tengamos las lineas del archivo le sumamos otra linea de texto
        inicio +=1
    #Imprimamos el nombre del nuevo archivo y las lineas que tendra
    print("El numero de lineas del nuevo archivo",nuearchivo, "son", inicio  )

def mainnumlinea():
    archivo = input("Ingrese la direccion del archivo original") 
    nuearchivo = input("Ingrese el nombre del archivo que quiere crear")      
    print(numlinea(archivo, nuearchivo))
if __name__ == "__main__":
    mainnumlinea()
"""Complicaciones:
Tuve algunos problemas con la interpretacion del ejercicio pero despues de volver
a buscar su traduccion y pedir ayuda a algunos compañeros sobre su interpretacion.
Con esto ya pude realizar el ejercicio"""

#%%Ejercicio 145:Encuentra la palabra más larga en un archivo (ya)
"""En este ejercicio, creará un programa de Python que identifique la(s) palabra(s) más 
larga(s) en un archivo.
Su programa debe generar un mensaje apropiado que incluya la longitud de la palabra más 
larga, junto con todas las palabras de esa longitud que se produjeron en el archivo.
Trate cualquier grupo de caracteres que no sean espacios en blanco como una palabra, 
incluso si incluye números o signos de puntuación."""
#Me falta poner a todas las palabras con esa misma longitud de larga solo me aparece una
def palabra_mas_largas(archivo):
    """
    
    Parameters
    ----------
    archivo : La direccion del archivo a analizar 

    Returns
    -------
    la(s) palabra(s) mas largas y su longitud

    """
    #Hacemos una try, por si la direccion del archivo no se encuentra o es incorrecta
    try: 
        #Abrimos el archivo ingresado por el usuario
        with open(archivo, 'r') as f:
            #Leemos las lineas del archivo
            contenido = f.readlines()
            #Convertimos las lineas leidas en una cadena
            textocontenido = "".join(contenido)
            #Obtenemos una lista con las palabras del texto
            palabras = textocontenido.split()
            
            print('Cantidad de palabras:', len(palabras))
            #Nombramos una variable con valor 0
            indice = 0 
            #Obtenemos la palabra que se encuentra en el indice 0
            palabra = palabras[indice]
            #Obtenemos las longitud de la palabta con este indice
            longitud = len(palabra)
            #Creamos dos listas vacias donde se guardaran las palabra(s) mas larga(s)
            listaa = []
            listaaa = []
            #Creamos un ciclo donde se revisan las longitudes de las palabras y 
            #las agregamos a una lista
            for i in range(1, len(palabras)):
                if len(palabras[i]) > longitud:
                    indice = i
                    palabra = palabras[i]
                    longitud = len(palabra)
                    
                    listaa.append(longitud)
            #Definimos a longitud2 como la palabras mas grande
            longitud2 = listaa[-1]
            #Creamos otro ciclo donde buscaremos las palabras que tengan la lontitud2
            #a esas palabras las agregamos a "listaaa"
            for i in range(1, len(palabras)):
                if len(palabras[i]) == longitud2:
                    palabra = palabras[i]
                    listaaa.append(palabra)
            #Imprimimos las palabras mas largas y su longitud
            print("Las palabras mas largas son",listaaa, "con longitud", longitud2)
    #Hacemos que la excepcion ocurre cuando no hay un archivo especificado    
    except OSError as e:
        print('El archivo especificado no existe.')
def mainpalabra_mas_larga():
    archivo = input("Escriba la direccion del archivo")        
    resultado = palabra_mas_largas(archivo)
    print(resultado)
if __name__ == "__main__":
    mainpalabra_mas_larga()
"""Complicaciones:
Tuve un poco de problemas de obtener todas las palabras con la longitud mas grande,
pues solo obtenia una, pero aun habia mas con esa longitud, pero despues de observar
este video : https://www.youtube.com/watch?v=PV49-QSC9JA&t=336s, pude tener mejor panorama"""    
    
#%%Ejercicio 146:Frecuencias de letras(ya)
"""Una técnica que se puede utilizar para ayudar a descifrar algunas formas simples 
de encriptación es el análisis de frecuencia. Este análisis examina el texto cifrado 
para determinar qué caracteres son los más comunes. Luego, intenta asignar las letras
más comunes en inglés, como E y T, a los caracteres más comunes en el texto cifrado.
Escriba un programa que inicie este proceso determinando y mostrando las frecuencias 
de todas las letras en un archivo. Ignore los espacios, los signos de puntuación y 
los números mientras realiza este análisis. Su programa debe ser insensible a mayúsculas 
y minúsculas, tratando a y A como equivalentes. El usuario proporcionará el nombre del 
archivo como un parámetro de línea de comando.
Su programa debería mostrar un mensaje de error significativo si el usuario proporciona
un número incorrecto de parámetros de línea de comando, o si el programa no puede abrir 
el archivo indicado por el usuario"""
def Frecuencia(archivoo):
    """
    
    Parameters
    ----------
    archivo : La direccion del archivo a analizar 

    Returns
    -------
    la frecuencia de las letras del texto del archivo

    """
    #Hacemos un try por si la direccion del archivo ingresada es incorrecta
    try:
        #Abrimos el archivo ingresado
        with open(archivoo, 'r') as f_in:
            #Leemos las lineas del archivo 
            lines = list(line for line in (l.strip() for l in f_in) if line)
            #Las lineas leidas las convertimos en una cadena
            texto = "".join(lines)
            print("El texto del archivo es", texto)
            #Creamos un diccionario abierto
            conteo = {}
            #Eliminamos los espacios en blanco de la cadena
            texto_sin = texto.replace(" ","") 
            #Hacemos un ciclo for donde agregamos las veces en las que aparecen las letras
            #las agregamos a el diccionario conteo
            for letra in texto_sin.lower():
                if letra not in conteo:
                    conteo[letra]=1
                #Se le va sumando 1 si aparece otra vez
                else:
                    conteo[letra] +=1
            #Hacemos los resultados de la frecuencia de las letras en forma de lista
            listaconteo = conteo.items()
            listaconteo = list(listaconteo)
            #Imprimimos los resultados de la frecuencias de las letras por separado 
            for l in listaconteo:
                print("La frecuencia de las letras que aparecen en el texto son",l)
           
    #Hacemos la excepcion cuando no se encuentra el archivo
    except FileNotFoundError as e:
        print('El archivo especificado no existe.')

def main_Frecuencia():
    archivoo = input("Escribe la direccion del archivo")
    print(Frecuencia(archivoo)) 
if __name__ == "__main__":
    main_Frecuencia()
"""Complicaciones:
Tuve un poco de problemas al querer darle un mejor formato a lo mostrado, 
la forma mas "bonita" de presentarlo fue en una lista, en lo demas no tuve muchos
problemas."""

#%%Ejercicio 147:Palabras que ocurren más(ya)
"""Escriba un programa que muestre la palabra (o palabras) que ocurren con mayor 
frecuencia en un archivo. Su programa debe comenzar leyendo el nombre del archivo 
del usuario. Luego, debe encontrar la(s) palabra(s) dividiendo cada línea en el 
archivo en cada espacio.
Finalmente, cualquier signo de puntuación inicial o final debe eliminarse de cada
palabra. Además, su programa debe ignorar las mayúsculas. Como resultado Apple y ApPle 
deben tratarse como la misma palabra. 
Probablemente encontrará útil su solución al Ejercicio 111 cuando complete este problema."""
import re
def Ocurrir(archivooo):
    """
    
    Parameters
    ----------
    archivo : La direccion del archivo a analizar 

    Returns
    -------
    la(s)

    """
    #Hacemos un try por si la direccion del archivo ingresada es incorrecta
    try:
        #Abrimos el archivo ingresado por el usuario
        with open(archivooo, 'r') as f:
            #Leemos las lineas del archivo 
            contenido = f.readlines()
            #Convertimos las lineas en una cadena
            textocontenidoo = "".join(contenido)
            #Eliminamos los signos de puntuacion de la cadena
            out = re.sub(r'[^\w\s]','',textocontenidoo)
            #Al texto todo lo convertimos en minusculas
            out = out.lower()
            #Obtenemos las palabras del texto        
            palabras = out.split()
            #Creamos un diccionario vacio donde se agregara una palabra si todavia
            #no esta en este y si ya esta se le aumentara un valor
            lista = {} 
            for palabra in palabras:
                if palabra in lista:
                    lista[palabra] += 1
                else:
                    lista[palabra] = 1
            #Obtenemos el valor maximo de los valores del diccionario
            valor_maximo= max(lista.keys(), key=lambda k:lista[k])
            valor_m = lista[valor_maximo]
            #Creamos una lista vacia donde guardaremos las palabras repetidas
            palabras_repetidas=[]
            #Creamos un ciclo para ver si mas valores son iguales al valor maximo 
            for palabra in lista:
                if lista[palabra] == valor_m:
                    palabras_repetidas.append(palabra)
            #Imprimimos las palabras repetidas y las veces que se repiten
            print("La(s) palabras:",palabras_repetidas, "se repiten", valor_m)

    #Hacemos la excepcion cuando no se encuentra un archivo   
    except FileNotFoundError:
        print("El archivo especificado no existe.") 
def main_Ocurrir():
    archivooo = input("Escribe la direccion del archivo")
    Ocurrir(archivooo)
if __name__ == "__main__":
    main_Ocurrir()    
"""Complicaciones:
No hubo  complicaciones"""
#%%Ejercicio 159:Palabras repetidas(falta)
"""Ejercicio 159: Palabras Repetidas
(61 líneas)
Los errores de ortografía son solo uno de los muchos tipos diferentes de errores que 
pueden aparecer en un trabajo escrito.
Otro error que es común para algunos escritores es una palabra repetida. Por ejemplo, 
un autor podría duplicar una palabra sin darse cuenta, como se muestra en la siguiente 
oración:

    "At least one value must be entered 
    entered in order to compute the average."

Algunos procesadores de texto detectarán este error y lo identificarán cuando se 
realice una revisión ortográfica o gramatical.
En este ejercicio, escribirá un programa que detecte palabras repetidas en un archivo
de texto.
Cuando se encuentra una palabra repetida, su programa debe mostrar un mensaje que 
contiene el número de línea y la palabra repetida. Asegúrese de que su programa 
maneje correctamente el caso en que aparece la misma palabra al final de una línea 
y al comienzo de la línea siguiente, como se muestra en el ejemplo anterior.
El nombre del archivo a examinar se proporcionará como el único parámetro de línea de 
comando del programa.
Muestre un mensaje de error adecuado si el usuario no proporciona un parámetro de línea
de comandos o si se produce un error al procesar el archivo."""


archivio = input("Escribe la direccion del archivo")
try:
    with open(archivio, 'r') as f:
        contenido = f.readlines()
        text = "".join(contenido)
        print(text)
        texto = text.lower()
        #print(text)
        # Las palabras están separadas por un espacio así que convertimos la cadena a arreglo
        palabras = texto.split()
        # Ahora vamos a contar las palabras creando un diccionario. En este caso la clave del diccionario
        # será la palabra, y el valor será el conteo
        diccionario_frecuencias = {}
        for palabra in palabras:
            if palabra in diccionario_frecuencias:
                diccionario_frecuencias[palabra] += 1
            else:
                diccionario_frecuencias[palabra] = 1
        print(diccionario_frecuencias)
        for palabra in diccionario_frecuencias:
            frecuencia = diccionario_frecuencias[palabra]
            if frecuencia >= 2:
                
        
                print("La", {palabra}, " se repite en la linea" )
            #print(f"La palabra '{palabra}' tiene una frecuencia de {frecuencia}")
except:
    print("no")
    







    