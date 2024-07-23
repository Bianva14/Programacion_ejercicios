# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 13:59:28 2022

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
from me_7-2.py import mainnumlinea()
if __name__ == "__main__":
    mainnumlinea()
"""Complicaciones:
Tuve algunos problemas con la interpretacion del ejercicio pero despues de volver
a buscar su traduccion y pedir ayuda a algunos compañeros sobre su interpretacion.
Con esto ya pude realizar el ejercicio"""

#%%Ejercicio 145:Encuentra la palabra más larga en un archivo(ya)
"""En este ejercicio, creará un programa de Python que identifique la(s) palabra(s) más 
larga(s) en un archivo.
Su programa debe generar un mensaje apropiado que incluya la longitud de la palabra más 
larga, junto con todas las palabras de esa longitud que se produjeron en el archivo.
Trate cualquier grupo de caracteres que no sean espacios en blanco como una palabra, 
incluso si incluye números o signos de puntuación."""
from me_7-2.py import mainpalabra_mas_larga()
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
from me_7-2.py import main_Ocurrir()
if __name__ == "__main__":
    main_Ocurrir()    
"""Complicaciones:
No hubo  complicaciones"""

#%%Ejercicio 149:Calificaciones de letras y puntos de calificación(ya)
"""Escriba un programa que convierta de calificaciones con letras a puntos de 
calificación y viceversa.
Su programa convertirá múltiples valores ingresados por el usuario, con un valor
ingresado en cada línea. Comience por intentar convertir cada valor ingresado por el 
usuario de una cantidad de puntos de calificación a una calificación con letras.
Si ocurre una excepción durante el intento, su programa debe intentar convertir el 
valor de una calificación de letra a una cantidad de puntos de calificación. Si ambas 
conversiones fallan, su programa debería proporcionar un mensaje que indique que la 
entrada proporcionada no es válida. Diseñe su programa para que continúe realizando 
conversiones hasta que el usuario ingrese una línea en blanco. Sus soluciones a los 
Ejercicios 51 y 52 pueden ser útiles al completar este ejercicio.
Letras   Puntos de calificacion
A+       4.0
A        4.0
A−       3.7
B+       3.3
B        3.0
B−       2.7
C+       2.3
C        2.0
C−       1.7
D+       1.3
D        1.0
F         0

"""


try:
    #Hacemos dos diccionarios uno donde las letras son las llaves y otra donde los 
    #puntos son las llaves
    tabla = {"A+": "4.0", "A":"4.0", "A-":"3.7", "B+":"3.3", "B":"3.0", "B-":"2.7", 
             "C+":"2.3", "C":"2.0", "C-":"1.7", "D+":"1.3", "D":"1.0", "F":"0"}
    tabla1 = {"4.0": "A+", "4.0":"A", "3.7":"A-", "3.3":"B+", "3.0":"B", "2.7":"B-", "2.3":"C+",
              "2.0":"C", "1.7":"C-", "1.3":"D+", "1.0":"D", "0":"F"}
    #Creamos una lista vacia donde se agregaran los valores que ingrese el usuario
    puntos = []
    #Pedimos los datos al usuario para asi convertirlo a letra o numero
    puntoscalificacion = input("Escribe una cadena : ")
    #Hacemos un ciclo donde se le seguira pidiendo datos al usuario hasta que se encuentre 
    #una linea en blanco
    while puntoscalificacion != "":
        puntos.append(puntoscalificacion)
        puntoscalificacion = input("Escriba una cadena : ")
    #Hacemos un ciclo donde si el dato ingresado es una letra se volvera un numero
    #si pasa lo contrario se obtendra la letra
    for numeros in puntos:
        if numeros in tabla.keys():
            print(tabla[numeros])
        elif numeros in tabla1.keys():
            print(tabla1[numeros])
#Si el dato ingresado por el usuario no es correcto se imprimira un error
except:
    print("Hay un error")
"""Complicaciones:
No hubo muchas complicaciones"""
#%%Ejercicio 152:¿Qué es ese elemento otra vez?(ya)
"""Escriba un programa que lea un archivo que contenga información sobre elementos 
químicos y lo almacene en una o más estructuras de datos apropiadas.
Entonces su programa debería leer y procesar la entrada del usuario. Si el usuario 
ingresa un número entero, su programa debe mostrar el símbolo y el nombre del elemento
con el número de protones ingresados.
Si el usuario ingresa una cadena, su programa debería mostrar la cantidad de protones
para el elemento con ese nombre o símbolo. Su programa debería mostrar un mensaje de 
error apropiado si no existe ningún elemento para el nombre, símbolo o número de 
protones ingresados.
Continúe leyendo la entrada del usuario hasta que se ingrese una línea en blanco."""

#Le pedimos al usuario la direccion del archivo
archivo1 = input("Escriba la direccion del archivo")
#Hacemos una excepcion por si la direccion del archivo no existe
try:
    #Abrimos el archivo
    with open(archivo1, 'r') as f:
        #Creamos una variable con la lista de las lineas del archivo
        contenido152 = f.readlines()
        #Creamos una lista vacia vacio donde se agregaran las lineas del archivo sin mayus
        #culas y separadas por una coma
        contenido = []
        for c in contenido152:
            contenido.append(c.lower().strip().split(","))
        #Le pedimos al usuario un dato para regresarle los que falten de ese elemento
        #le dejamos de pedir al usuario los datos hasta que ingrese una linea en blanco
        while True:   
            datos = input("Escriba la cadena para obtener los datos(Espacio en blanco para acabar): ")
            if datos == "":  
                break
            #Revisamos el dato ingresado y regresamos los que faltan como el numero
            for h in contenido:
                if h[0]==datos:
                    print("Su abreviacion es:"h[1],"y se llama:" h[2])
                if h[1]==datos:
                    print("El numero de protones es:"h[0],"y se llama"h[2])
                if h[2]==datos:
                    print("El numero de protones es:"h[0],"y su abreviacion es",h[1])
                    
except FileNotFoundError as e:
    print('El archivo especificado no existe.')
"""Complicaiones:
Solo tuve un problema al no saber como almacenar el contenido sin mayusculas pero me
parecio mas factiible hacerlo en una lista para de ahi obtener los datos que pedia el usuario"""

#%%Ejercicio 155:(ya)Nombres neutrales de género
"""Algunos nombres, como Ben y Jonathan, normalmente solo se usan para niños, mientras
que nombres como Rebbecca y Flora normalmente solo se usan para niñas.
Se pueden usar otros nombres, como Chris y Alex, tanto para niños como para niñas.
Escriba un programa que determine y muestre todos los nombres de bebés que se usaron 
tanto para niños como para niñas en un año especificado por el usuario.
Su programa debe generar un mensaje apropiado si no hubo nombres de género neutral en 
el año seleccionado.
Muestre un mensaje de error apropiado si no tiene datos para el año solicitado por el
usuario.
En el Ejercicio 154 se incluyen detalles adicionales sobre el conjunto de datos de 
nombres de bebés."""
import sys

#Hacemos un ciclo while donde le pide los datos al usuario y cuando este ingrese una linea
#en blacon se dentendra y mostrara resultados
while True:   
    
    año = input("Ingresa el año entre 1900 - 2012 (Espacio en blanco para acabar): ")
    if año == "":
        break
    #Almacenan el nombre con el que se buscara el archivo para niños correspondiente
    #a cada año
    carpeta = "C:/Users/pc1/Documents/programacion-2021-2/Scripts/Datos para los ejercicios del capitulo 7/BabyNames/" 
    archivo_M = carpeta + str(año) + "_BoysNames.txt"
    archivo_F = carpeta + str(año) + "_GirlsNames.txt"
    #Abrimos y leemos los archivos previamenten definidos y los definimos en una 
    #variable
    abrir_archivo = True
    
    if abrir_archivo == True:
        try:
            archivo_M_r = open(archivo_M, "r")
            archivo_F_r = open(archivo_F, "r")
            abrir_archivo = False
            
        except FileNotFoundError:
            print("Verifica si el año que ingresaste esta entre 1900 y 2012")
            sys.exit(0)
    #Creamos una lista vacia para almacenar los nombres de los niños
    nombre_niño = []
    #Vamos agregando los nombres sin que se repitan en la lista nombre_niño
    for niño in archivo_M_r.readlines():
        if niño.split(" ")[0] not in nombre_niño:
            nombre_niño.append(niño.split(" ")[0])
    
    #Creamos una lista vacia para almacenar los nombres que estan tanto en el archivo
    #niñas y niños
    nombre_neutro = []
    #Hacemos un ciclo para revisar si el nombre de la niña esta en nombre_nino y si
    #esta se agrega a la lista nombre_neutro sin que se repitan los nombres
    for niña in archivo_F_r.readlines():
        if niña.split(" ")[0] in nombre_niño and niña.split(" ")[0] not in nombre_neutro:
            nombre_neutro.append(niña.split(" ")[0])
    #Cerramos los archivos
    archivo_M_r.close()
    archivo_F_r.close()
    #Si no se guardo ningun nombre en la lista nombre_neutro en el año correspondiente,
    #significa que no hay nombres neutros en esos años
    if len(nombre_neutro) == 0:
        print("")
        print("No se utilizo ningun nombre neutro en el año ({}).".format(año))
    #Si la lista tiene contenido, entonces si hubo nombres neutros    
    else:
        print("")
        print("En {}, los nombres neutros que se usaron fueoron: ".format(año), end="")
        for nombre in nombre_neutro:
            print(nombre, end="  ")
        print("")
"""Complicaciones:
Tuve un poco de problemas al hacer que el programa corriera pues no tomaba en cuenta 
los archivos _BoysNames.txt y _Girls.txt entonces me acorde de como se abrieron 
los archivos en el ejercicio 157, pues no habia puesto la ruta(direccion) de la carpeta
BabysNames, al colocarla me funciono el codigo
"""

#%%Ejericio 156:La mayoría de los nacimientos en un período de tiempo dado(ya)
"""Ejercicio 156: La Mayoría de Nacimientos en un Período de Tiempo determinado
Escriba un programa que use el conjunto de datos de nombres de bebés descrito en el 
ejercicio 154 para determinar qué nombres se usaron con más frecuencia dentro de un 
período de tiempo.
Haga que el usuario proporcione el primer y último año del rango a analizar. Muestre
el nombre del niño y el nombre de la niña dado a la mayoría de los niños durante los
años indicados."""
import sys
#Ingresamos la direccion de la carpeta para abrir los archivos de texto
carpeta = "C:/Users/pc1/Documents/programacion-2021-2/Scripts/Datos para los ejercicios del capitulo 7/BabyNames/" 
#Le pedimos al usuario los rangos de los años a analizar
primern = int(input("Escriba el primer parametro de año del rango a analizar(1900-2012)"))
segundon = int(input("Escriba el ultimo parametro(1900-2012)"))
#Creamos dos lista para ingresar los nombres de las ninñas y de los niños en esos años
ninas = []
ninos = []
#Creamos dos listas para alamacenar los nombres de las niñas y niños ocupados en esos años
nina_ocupados =[]
nino_ocupados = []
#Creamos dos listas para almacenar los nombres mas ocupados en ese rango de años
popu_nina = []
popu_nino = []
#Creamos un ciclo para almacenar los nombres de las niñas en el rango ingresado en una lista
for n in range(primern, segundon+1):
    a = open(carpeta + str(n) + "_GirlsNames.txt","r")
    ninas.append(a.readlines())
    a.close()
#Creamos un ciclo que va a verificar si el nombre de nina en la lista se ha usado 
#si se ha usado se agrega a la lista nina_ocupados
for m in ninas: 
    for o in m:
        nina = o.split()[0]
        if nina not in nina_ocupados:
            nina_ocupados.append(nina)
#Creamos un ciclo para almacenar los nombres de las niños en el rango ingresado en una lista
for ni in range(primern, segundon+1):
    b = open(carpeta + str(ni) + "_BoysNames.txt","r")
    ninos.append(b.readlines())
    b.close()
#Creamos un ciclo que va a verificar si el nombre de nino en la lista se ha usado 
#si se ha usado se agrega a la lista nino_ocupados
for m in ninos: 
    for o in m:
        nino = o.split()[0]
        if nino not in nino_ocupados:
            nino_ocupados.append(nino)
#Convertimos las listas que contienen los nombres de los niños y niñas ocupados
Strnina_ocupados = " ".join(nina_ocupados)
Strnino_ocupados= " ".join(nino_ocupados)
#Obtenemos los nombres de las listas
parts_strnina = Strnina_ocupados.split()
parts_strnino = Strnino_ocupados.split()
#Obtenemos los nombres mas populares
name1 = parts_strnina[0]
name2 = parts_strnino[0]
#Guardamos los nombres mas populares en las listas popu_nina y popu_nino
if name1 not in popu_nina:
    popu_nina.append(name1)
if name2 not in popu_nino:
    popu_nino.append(name2)
#Imprimimos los nombres mas ocupados en esos rangos de años
print ("Los nombres de ninas de ano",primern, "al", segundon,"mas ocupados fueron", popu_nina)
print ("Los nombres de ninas de ano",primern, "al", segundon,"mas ocupados fueron", popu_nino)
"""Complicaciones:
Tuve algunas complicaciones al comprender el problema pero despues de buscar palabra por palabra
en el traductor me quedo mas claro el problema, hice uso del codigo del ejercicio 154 para
obetener los nombres mas frecuentes(populares)"""

#%%Ejercicio 157:Nombres Distintos(ya)
"""
@autor: Bianca Ramirez Mejia  no.cuenta:421117321
En este ejercicio, creará un programa que lea cada archivo en el conjunto de datos de nombres
de bebés descrito en el Ejercicio 154. A medida que su programa lea los archivos, debe realizar
un seguimiento de cada nombre usado para un niño y cada nombre usado para una niña. Su programa
debe generar dos listas.
Una lista contendrá todos los nombres que se han usado para niñas.
La otra lista contendrá todos los nombres que se han usado para niños. Ninguna de sus listas 
debe contener valores repetidos."""
#Definimos la carpeta con la direccion de la carpeta de archivos de BabyNames
carpeta = "C:/Users/pc1/Documents/programacion-2021-2/Scripts/Datos para los ejercicios del capitulo 7/BabyNames/"
#Creamos una lista vacia donde se agregaran los nombres de las niñas
nombres_ninas = []
solo_nombre_nina = []
nombres_ninos = []
solo_nombre_nino = []
#Para cada año de GirlsNames abrimos el archivo y agregamos los nombres en la lista 
#nombres_ninas
for n in range(1900, 2013):
    a = open(carpeta + str(n) + "_GirlsNames.txt","r")
    nombres_ninas.append(a.readlines())
    a.close()
#Creamos un ciclo que va a verificar si el nombre de nina en la lista se ha usado 
#si se ha usado se agrega a la lista solo_nombre_nina
for m in nombres_ninas: 
    for o in m:
        nombre_nina = o.split()[0]
        if nombre_nina not in solo_nombre_nina:
            solo_nombre_nina.append(nombre_nina)
#Para cada año de _BoysNames abrimos el archivo y agregamos los nombres en la lista 
#nombres_ninas
for n in range(1900, 2013):
    a = open(carpeta + str(n) + "_BoysNames.txt","r")
    nombres_ninos.append(a.readlines())
    a.close()
#Creamos un ciclo que va a verificar si el nombre del nino en la lista se ha usado 
#si se ha usado se agrega a la lista solo_nombre_nino    
for m in nombres_ninos: 
    for o in m:
        nombre_nino = o.split()[0]
        if nombre_nino not in solo_nombre_nino:
            solo_nombre_nino.append(nombre_nino)
#Imprimimos las listas con los nombres de niñas y niños que se han usado en los años
#de 1990 a 2012           
print("Los nombres de niñas usados del año 1990 - 2012 fueron: ")
print(solo_nombre_nina)            
print("Los nombres de niños usados del año 1990 - 2012 fueron: ")
print(solo_nombre_nino)
"""Complicaciones:
No hubo complicaciones"""
    

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

#%%Ejercicio 162: longitudes de línea consistentes(45 líneas)
"""Si bien 80 caracteres es un ancho común para una ventana de terminal, algunos 
terminales son estrechos o más anchos. Esto puede presentar desafíos cuando se 
muestran documentos que contienen párrafos de texto. Las líneas pueden ser demasiado 
largas y apretadas, lo que las hace difíciles de leer, o pueden ser demasiado cortas 
y no aprovechar el espacio disponible.
Escriba un programa que abra un archivo y lo muestre para que cada línea se llene 
lo más posible. Si lee una línea que es demasiado larga, su programa debería dividirla
 en palabras y agregar palabras a la línea actual hasta que esté llena. Luego, 
 su programa debería comenzar una nueva línea y mostrar las palabras restantes.
De manera similar, si lee una línea que es demasiado corto, entonces necesitará usar
palabras de la siguiente línea del archivo para terminar de llenar la línea actual 
de salida. Por ejemplo, considere un archivo que contenga las siguientes líneas de 
"Las aventuras de Alicia en el país de las maravillas":
    Alice was
    beginning to get very tired of sitting by her
    sister
    on the bank, and of having nothing to do: once
    or twice she had peeped into the book her sister
    was reading, but it had
    no
    pictures or conversations in it,"and what is
    the use of a book," thought Alice, "without
    pictures or conversations?"
Cuando se formatea para una longitud de línea de 50 caracteres, debe mostrarse como:
    Alice was beginning to get very tired of sitting
    by her sister on the bank, and of having nothing
    to do: once or twice she had peeped into the book
    her sister was reading, but it had no pictures or
    conversations in it, "and what is the use of a
    book," thought Alice, "without pictures or
    conversations?"
Asegúrese de que su programa funcione correctamente para archivos que contengan 
varios párrafos de texto. Puede detectar el final de un párrafo y el comienzo del 
siguiente buscando líneas que estén vacías una vez que se haya eliminado el marcador 
de final de línea. Puede realizar una comprobación de errores si lo desea, pero 
no es necesario para este ejercicio.

Sugerencia: use una constante para representar la longitud máxima de la línea. 
Esto facilitará la actualización del programa cuando cambie el tamaño de la ventana.
"""
#Le pedimos al usuario la direccion del archivo
archivo=input("Ingrese la direccion del archivo ")
#Abrimos el archivo
with open(archivo, 'r') as f:
    #Leemos el archivo
    texto=f.read()
    #Convertimos el texto a uno plano
    texto_plano=texto.replace('\n', " ")
    f.close()
    #Hacemos una lista con el texto plano obtenido
    lista=list(texto_plano)
    lineas = 50
    #Definimos a la salida que toma los 50 caracteres en cada linea 
    salida=[lista[i:i + lineas] for i in range(0, len(lista), lineas)]
    #Cuando se llegan a los 50 le agregamos un salto de linea
    for listaa in range(len(salida)):
        salida[listaa].append('\n')
    #Creamos una lista vacia para almacenar el texto completo
    listacompleta=[]
    #Ocupamos todas las lineas que tienen 50 caracteres y los unimos, las agregamos
    #a la lista vacia 
    for lista_nueva in range(len(salida)):
        listacompleta.extend(salida[lista_nueva])
    #Convertimos nuestra lista a una cadena
    texto_nuevo="".join(listacompleta)
    #Imprimimos el texto nuevo
    print(texto_nuevo)
"""Complicaciones:
Tuve muchas complicaciones al aplicar el salto de linea pues no se me ocurria nada,
pero despues de recordar que el metodo append, todo fue mas facil, por lo que me 
di cuenta que necesitaba un repaso de los metodos de listas. En lo demas todo estuvo bien"""



    
archivo=input("Ingrese la direccion del archivo ")   
f=open(archivo,"r")
texto=f.read()
texto_plano=texto.replace('\n', " ")
f.close()
v=list(texto_plano)
n_listas=len(v)//50
#for n in range(n_listas):
n=50

output=[v[i:i + n] for i in range(0, len(v), n)]
for lista in range(len(output)):
    output[lista].append('\n')
    
listacompleta=[]
for lista_nueva in range(len(output)):
    listacompleta.extend(output[lista_nueva])
texto_nuevo="".join(listacompleta)
print(texto_nuevo)



#%%Ejercicio 163:Palabras con Seis Vocales en Orden(ya)
"""Hay al menos una palabra en el idioma inglés que contiene cada una de las vocales a, 
e, i, o, u e y exactamente una vez y en orden. Escriba un programa que busque un archivo 
que contenga una lista de palabras y muestre todas las palabras que cumplan con esta 
restricción.
El usuario proporcionará el nombre del archivo que se buscará. Muestre un mensaje de 
error apropiado y salga del programa si el usuario proporciona un nombre de archivo no 
válido o si algo sale mal mientras busca palabras con seis vocales en orden.
Solucion:
 """

import sys


#Le preguntamos al usuario la direccion del archivo
file_dir = input("Ingresa la direccion del archivo:\n")
#Creamos una lista vacia donde se guararan las palabras leidas linea por linea del archivo
words_array = []
#Abrimos el archivo y almacenamos las palabras en la lista words_array, despues lo cerramos
try:
    file_words = open(file_dir, "r")
    words_array = file_words.readlines()
    file_words.close()
#Si el archivo no es valido, la ruta no es correcta, entonces se imprimira que no se puede abrir
except OSError as e:
     print ("El archivo no se pudo abrir, porfavor escribe un nombre de archivo valido")
     sys.exit(0)

try:
    #Para las palabras en la lista vamos a checar los siguientes si se encuentran las vocales y si
    #estan en  orden
    for word in words_array:
        #Creamos un diccionario donde se agregaran las vocales con los indices como valor
        voc_indices = {}
        #Definimos a una palabra como las palabras en la lista sin espacio y con minusculas,
        #Convertimos a los elementos en minusculas y sin espacios
        palabra = word.strip().lower()
        #Revisamos que las vocales esten en la palabra y que solo este una vez, posteriormente
        #buscamos su indice y decimos que ese es su valor en el diccionario
        if ('a' in palabra) and palabra.count('a') == 1:
            voc_indices['a'] = palabra.index('a')
    
        if ('e' in palabra) and palabra.count('e') == 1:
            voc_indices['e'] = palabra.index('e')
        
        if ('i' in palabra) and palabra.count('i') == 1: 
            voc_indices['i'] = palabra.index('i')
        
        if ('o' in palabra) and palabra.count('o') == 1:
            voc_indices['o'] = palabra.index('o')
        
        if ('u' in palabra) and palabra.count('u') == 1:  
            voc_indices['u'] = palabra.index('u')
    
        if ('y' in palabra) and palabra.count('y') == 1:
            voc_indices['y'] = palabra.index('y')
        #Despues revisamos que los indices sean 6, es decir los indices de las vocales en la palabra
        if len(voc_indices) == 6:
            #Ahora revisamos si estan en orden es decir,si se encuentra de la forma a, e, i, o, u, y esto lo hacemos
            #comparando sus indices
            if voc_indices['a'] < voc_indices['e'] <  voc_indices['i'] < palabra.index('o') < palabra.index('u') < palabra.index('y'):
                #Si se encuentran en el orden correcto imprimimos las palabra
                print (palabra)
#Si no se puede leer el archivo no se podra seguir con los pasos
except:
    print ("Algo salio mal no se que")
    sys.exit(0)
"""Solo tuve un pequeño problema al principio pues no sabia como poner que solo se repitiera una vez
la vocal, pero despues me acorde del metodo count, pero en lo demas estuvo mas facil"""

