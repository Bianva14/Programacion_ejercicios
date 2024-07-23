# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 22:35:21 2022

@author: pc1
"""

#%%Ejercicio 141:Display the Head of a File(Mostrar el encabezado de un archivo)
"""
@author: Rojas Trejo Agustin Santiago, 318056045
Ben Stephenson. (2014). The python workbook : a brief introduction with 
exercises and solutions.
Ejercicio 141: Display the Head of a File (Mostrar el encabezado de un archivo)

Descripción del problema:
Los sistemas operativos basados en Unix suelen incluir una herramienta llamada 
head. Esta herramienta muestra las 10 primeras líneas de un archivo cuyo nombre 
se proporciona como parámetro en la línea de comandos. Escriba un programa en 
Python que proporcione el mismo comportamiento. Muestra un mensaje de error 
apropiado si el archivo solicitado por el usuario no existe o si se omite el 
parámetro de la línea de comandos.

Descripción de la solución del problema:
Primero comprobamos que se han ingresado los parametros correctos en la linea 
de comandos para que nuestro programa funcione con un condicional if, si no 
sucede esto terminamos el programa.
Despues con la funcion try intentamos abrir el programa en modo lectura y a traves
de un ciclo vamos leyendo e imprimiendo 10 lineas del archivo que no 
sean vacias, una vez que finiliza el ciclo cerramos el archivo. Finalmente 
mostramos un mensaje de error si el archivo solicitado por el usuario no existe 
o si se omite el parámetro de la línea de comandos.
"""

##
# Muestra el encabezado (las 10 primeras líneas) de un archivo cuyo nombre se 
# proporciona como parámetro en la línea de comandos.

import sys

NUM_LINES = 10

# Compruebe que se ha suministrado exactamente un parámetro de la línea de 
# comandos (además del archivo .py)
if len(sys.argv) != 2:
    print("Debe proporcionar el nombre del archivo como parámetro de la línea de comandos.")
    quit()
"""
Cuando se llama a la función quit el programa termina inmediatamente.
"""
try:
    # Abrir el archivo para su lectura
    inf = open(sys.argv[1], "r")
    
    # Lea la primera línea del archivo
    line = inf.readline()
    
    # Sigue buscando hasta que hayamos leído y mostrado 10 líneas o hayamos 
    # llegado al final del archivo
     
    count = 0
    while count < NUM_LINES and line != "":
        # Eliminar el carácter de nueva línea final y contar la línea
        line = line.rstrip()
        count = count + 1
        
        # Mostrar la línea
        print(line)
        
        # Lea la siguiente línea del archivo
        line = inf.readline()
    # Cerrar el archivo
    inf.close()
except IOError:
    # Mostrar un mensaje si algo va mal al acceder al archivo
    print("Se ha producido un error al acceder al archivo.")

"""
La traducción de este ejercicio fue sencilla y en algunas partes del código 
tuve pequeños errores por omitir o cambiar algún punto por un guión bajo. El 
entendiemiento de la solución fue un poco complicado, pero investigando en internet
encontre estos links que me facilitaron esa tarea:
    https://programmerclick.com/article/79711369194/
    https://adictec.com/como-abrir-archivos-y-carpetas-con-cmd/
    http://www.eumus.edu.uy/eme/ensenanza/electivas/python/2020/clase_08a.html
    https://docs.python.org/es/3.10/library/sys.html
"""
#%%Ejercicio 142: Display the Tail of a File (Mostrar la cola de un archivo)
"""
@author: Rojas Trejo Agustin Santiago, 318056045
Ben Stephenson. (2014). The python workbook : a brief introduction with 
exercises and solutions.
Ejercicio 142: Display the Tail of a File (Mostrar la cola de un archivo)

Descripción del problema:
Los sistemas operativos basados en Unix también suelen incluir una herramienta 
llamada tail. Esta herramienta muestra las últimas 10 líneas de un archivo cuyo 
nombre se proporciona como parámetro en la línea de comandos.
Escriba un programa en Python que proporcione el mismo comportamiento. Muestra 
un mensaje de error apropiado si el archivo solicitado por el usuario no existe 
o si se omite el parámetro de la línea de comandos.
Hay varios enfoques diferentes que se pueden tomar para resolver este problema. 
Una opción es cargar todo el contenido del archivo en una lista y luego mostrar 
los últimos 10 elementos. Otra opción es leer el contenido del archivo dos 
veces, una para contar las líneas y otra para mostrar las últimas 10 líneas.
Sin embargo, ambas soluciones son indeseables cuando se trabaja con archivos 
grandes. Existe otra solución que sólo requiere leer el archivo una vez, y sólo 
requiere almacenar 10 líneas del archivo de una vez. Para un desafío adicional, 
desarrolle una solución de este tipo.

Descripción de la solución del problema:
Primero comprobamos que se han ingresado los parametros correctos en la linea 
de comandos para que nuestro programa funcione con un condicional if, si no 
sucede esto terminamos el programa.
Despues con la funcion try intentamos abrir el programa en modo lectura y creamos
una lista vacia que contendra todas las lineas que hay en nuestro archivo, despues 
a traves de un ciclo iremos añadiendo las todas las lineas del archivo a la lista
e iremos eliminando los primeros elementos de la lista si esta contiene mas de 
10 elementos, una vez que finalice el ciclo y obtengamos nuestra lista con 10 
elementos cerramos el archivo. Despues mostramos un mensaje de error apropiado 
si el archivo solicitado por el usuario no existe, si se omite el parámetro de 
la línea de comandos o si sucede algun error al procesar el archivo. Finalmente
mostramos las lineas que se hayan guardado en nuestra lista.
"""

##
# Muestra la cola (últimas líneas) de un archivo cuyo nombre se proporciona 
# como parámetro en la línea de comandos.

import sys

NUM_LINES = 10

# Compruebe que se ha proporcionado exactamente un parámetro de línea de 
# comandos (además del archivo .py)
if len(sys.argv) != 2:
    print("El nombre del archivo debe proporcionarse como un parámetro de la línea de comandos.")
    quit()

try:
    # Abrir el archivo para su lectura
    inf = open(sys.argv[1], "r")
    
    # Lee el archivo, guardando siempre las líneas más recientes de NUM_LINES
    lines = []
    for line in inf:
        # Añadir la línea más reciente al final de la lista
        lines.append(line)
        # Si ahora tenemos más de NUM_LINES líneas, eliminamos la más antigua
        if len(lines) > NUM_LINES:
            lines.pop(0)
    
    # Cerrar el archivo
    inf.close()

except:
    print("Se ha producido un error al procesar el archivo.")
    quit()
    
# Mostrar las últimas líneas del archivo
for line in lines:
    print(line, end="")

"""
La traducción de este ejercicio fue sencilla y en algunas partes del código 
tuve pequeños errores por omitir o cambiar algunas letras u olvidar agregar los 
parentesis. El entendiemiento de la solución fue un poco complicado, pero 
investigando en internet encontre estos links que me facilitaron esa tarea:
    https://programmerclick.com/article/79711369194/
    https://adictec.com/como-abrir-archivos-y-carpetas-con-cmd/
    http://www.eumus.edu.uy/eme/ensenanza/electivas/python/2020/clase_08a.html
    https://docs.python.org/es/3.10/library/sys.html
"""
#%%Ejercicio 143: Concatenate Multiple Files (Concatenar varios archivos)
"""
@author: Rojas Trejo Agustin Santiago, 318056045
Ben Stephenson. (2014). The python workbook : a brief introduction with 
exercises and solutions.
Ejercicio 143: Concatenate Multiple Files (Concatenar varios archivos)

Descripción del problema:
Los sistemas operativos basados en Unix suelen incluir una herramienta llamada 
cat, que es la abreviatura de concatenación. Su propósito es concatenar y 
mostrar uno o más archivos cuyos nombres se proporcionan como parámetros de la 
línea de comandos. Los archivos se muestran en el mismo orden en que aparecen 
en la línea de comandos.
Crea un programa en Python que realice esta tarea. Debe generar un mensaje de 
error apropiado para cualquier archivo que no pueda ser mostrado, y luego 
proceder al siguiente archivo. Muestra un mensaje de error apropiado si su 
programa se inicia sin ningún parámetro de línea de comandos.

Descripción de la solución del problema:
Primero comprobamos que se han ingresado los parametros correctos en la linea 
de comandos para que nuestro programa funcione con un condicional if, si no 
sucede esto terminamos el programa.
Despues a traves de un ciclo iremos iterando sobre los archivos, los cuales
abriremos, uno por uno en orden, en modo lectura y mostraremos una por una todas
las lineas que contenga ese archivo y depues lo cerraremos. Finamente mostraremos
un mensaje de error apropiado para cualquier archivo que no pueda ser mostrado.
"""

##
# Concatenar uno o más archivos, mostrando el resultado.
#
import sys

# Asegúrese de que se ha proporcionado al menos un parámetro de línea de 
# comandos (además del archivo .py)
if len(sys.argv) == 1:
    print("Debe proporcionar al menos un nombre de archivo")
    quit()
    
# Procesar todos los archivos proporcionados en la línea de comandos
for i in range(1, len(sys.argv)):
    fname = sys.argv[i]
    """
    El elemento en la posición 0 de sys.argv es el archivo de Python que se está ejecutando. 
    Como resultado, nuestro bucle for comienza a procesar los archivos en la posición 1 de la lista.
    """
    try:
        # Abrir el archivo actual para su lectura
        inf = open(fname, "r")
        
        # Mostrar el archivo
        for line in inf:
            print(line, end="")
            
        # Cerrar el archivo
        inf.close()
    
    except:
        # Mostrar un mensaje, pero no salir para que el programa siga procesando los siguientes archivos
        print("No se puede abrir/mostrar", fname)

"""
La traducción de este ejercicio fue sencilla y en algunas partes del código 
tuve pequeños errores al cambiar alguna letra u omitir los dos puntos. El 
entendiemiento de la solución fue un poco complicado, pero investigando en internet
encontre estos links que me facilitaron esa tarea:
    https://programmerclick.com/article/79711369194/
    https://adictec.com/como-abrir-archivos-y-carpetas-con-cmd/
    http://www.eumus.edu.uy/eme/ensenanza/electivas/python/2020/clase_08a.html
    https://docs.python.org/es/3.10/library/sys.html
"""
#%% Ejercicio 148: Sum a List of Numbers (Suma de una lista de números)
"""
@author: Vasquez Matias Cynthia Noemi, 318218364
Ben Stephenson. (2014). The Python Workbook. Switzerland: Springer., 
Ejercicio 148: Sum a List of Numbers (Suma de una lista de números)

Descripción del problema:
Cree un programa que sume todos los números introducidos por el usuario, ignorando
cualquier línea introducida por el usuario que no sea un número válido. Su
programa debería mostrar la suma actual después de introducir cada número. Debe
mostrar un mensaje de error apropiado después de cualquier entrada no válida, y
luego continuar sumando cualquier número adicional introducido por el usuario. 
Su programa debe salir cuando el usuario introduzca una línea en blanco. Asegúrese
de que su programa funciona correctamente tanto con números enteros como con
números de coma flotante.
Sugerencia: Este ejercicio requiere que uses excepciones sin usar archivos.

Descripción de la solución del problema:
Lo primero que se hará será crear una variable en la que se almacenará un valor
que se le pedirá al usuario y otra variable que irá almacenando el total de la
suma. Después generaremos un ciclo que le pida a el usuario que introduzca un
número y así hasta que introduzca una línea en blanco o de un valor no valído,
para lo cual usaremos un try y except. Cada número que se introduzca se irá
sumando a nuestra variable creada en un principio. Y finalmente cuando el usuario
termine de introducir todos sus números se le mostrará un mensaje con el valor
final de la suma.
"""
#
# Calcule la suma de números ingresados por el usuario, ignorando la entrada no numérica.
#

# Lea la primera línea de entrada del usuario
linea = input("Ingrese un número: ")
total = 0

# Siga leyendo hasta que el usuario ingrese una línea en blanco
while linea != "":
    try:
        # Probar y convertir la línea en un número
        numero = float(linea)
        # Si la conversión tiene éxito, agréguela al total y visualícela
        total = total + numero
        print("El total ahora es: ", total)
    
    except ValueError:
        # Muestre un mensaje de error antes de continuar con la lectura del siguiente
        print("Eso no era un número.")
    
    # Leer el siguiente número
    linea = input("Introduzca un número: ")
    
# Muestre el total
print("El gran total es: ", total)

"""
No hubo mayor complicación para este ejercicio, pues son temas que ya habíamos
visto con anterioridad y cuyo procedimiento fue fácil de analizar.
"""


#%% Ejercicio 150: Remove Comments (Eliminar comentarios)
"""
@author: Vasquez Matias Cynthia Noemi, 318218364
Ben Stephenson. (2014). The Python Workbook. Switzerland: Springer., 
Ejercicio 150: Remove Comments (Eliminar comentarios)

Descripción del problema:
Python utiliza el carácter # para marcar el comienzo de un comentario. El
comentario termina al final de la línea que contiene el carácter #. En este
ejercicio, crearás un programa que elimine todos los comentarios de un archivo
fuente de Python. Comprueba cada línea del archivo para determinar si el carácter
# está presente. Si lo está, tu programa debe eliminar todos los caracteres desde
el carácter # hasta el final de la línea (ignoraremos la situación en la que el
carácter de comentario ocurre dentro de una cadena). Guarde el modificado
utilizando un nuevo nombre que será introducido por el usuario. El usuario también
introducirá el nombre del archivo de entrada. Asegúrese de que se muestra un
mensaje de error adecuado si se encuentra un problema al acceder a los archivos.

Descripción de la solución del problema:
Para este ejercicio vamos a ocupar try y except varias veces pues se nos pide
que abramos el archivo que introduzca el usario y en caso de que no sea válido
lo que se introdujo mostremos un mensaje de error. Por lo que primero vamos a
usar un try para que le pida a el usuario ingresar el nombre del archivo y un
except en caso de que no sea válido, después usaremos otro try para que ingrese
el archivo de salida e igual un excpet en caso de que no sea válido.
Una vez que tenemos el archivo abierto lo que harémos será usar nuestra función
find para que busque los símbolos # en caso de que los encuentre eliminará el
texto que contenga y los almacenará en otra variable para que sólo se muestre
el texto ya sin los comentarios.
Finalmente cerraremos los archivos que se introdujeron.
"""
##
# Elimina todos los comentarios de un archivo de Python, ignorando el caso donde
# aparece un carácter de comentario dentro de una cadena.
#

# Lea y abra el archivo de entrada, asegurándose de que se abrió correctamente
try:
    en_nombre = input("Ingrese el nombre de un archivo Python: ")
    inf = open(en_nombre, "r")
except:
    print("Se encontró un problema al abrir el archivo de entrada")
    print("Saliendo...")
    quit()
# Lea y abra el archivo de salida, asegurándose de que se abrió correctamente
try:
    out_nombre = input("Ingrese el nombre del archivo de salida: ")
    outf = open(out_nombre, "w")
except:
    print("Se encontró un problema al abrir el archivo de salida")
    print("Saliendo...")
    quit()
    
try:
    # Leer todas las líneas del archivo de entrada, procesarlas para eliminar
    # comentarios y guardar las líneas en un nuevo archivo
    for line in inf:
        # Buscar la posición del carácter del comentario (-1 si no hay uno)
        pos = line.find("#")
        
        # Si hay un comentario, forme una porción de la
        # cadena que lo excluye, sobresaliendo la línea
        if pos > -1:
            line = line[0 : pos]
            line = line + "\n"

        """
        La posición del caracter del comentario se almacena en pos. Como
        resultado, la línea [0 : pos]  son todos los caracteres hasta el
        carácter de comentario, pero sin incluirlo.
        """
        
        # Escriba la línea (potencialmente modificada en el archivo)
        outf.write(line)
    
    # Cerrar los archivos
    inf.close()
    outf.close()
except:
    print("Se encontró un problema al procesar el archivo")
    print("Saliendo...")
"""
Al momento de traducir la descripción del problema no hubo mayor complicación,
sólo una de las cosas que no sabía cómo funcionaba fue la terminación .find por
lo que investigué y esta página me ayudó a entender su funcionamiento:
    https://www.w3schools.com/python/ref_string_find.asp
Y gracias también a eso entendí otras cosas que estaban dentro del problema.
También no me había quedado muy claro cómo funcionaba .write, pero en la
siguiente página encontré principalmente su objetivo:
    https://www.w3schools.com/python/python_file_write.asp
"""
#%% Ejercicio 151: Two Word Random Password (Contraseña aleatoria de dos palabras)
"""
@author: Vasquez Matias Cynthia Noemi, 318218364
Ben Stephenson. (2014). The Python Workbook. Switzerland: Springer., 
Ejercicio 151: Two Word Random Password (Contraseña aleatoria de dos palabras)

Descripción del problema:
Aunque generar una contraseña seleccionando caracteres aleatorios generalmente
da una contraseña relativamente segura, también suele dar una contraseña difícil
de memorizar. Como alternativa, algunos sistemas construyen una contraseña tomando
dos palabras en inglés y concatenándolas. Aunque esta contraseña no es tan segura,
es mucho más fácil de memorizar.
Escriba un programa que lea un archivo que contenga una lista de palabras,
seleccione al azar dos de ellas, y las concatene para producir una nueva
contraseña. Al producir la contraseña asegúrese de que la longitud total esté
entre 8 y 10 caracteres, y que cada palabra utilizada tenga al menos tres letras.
Escriba en mayúsculas cada palabra de la contraseña para que el usuario pueda ver
fácilmente dónde termina una palabra y empieza la siguiente. Muestre la contraseña
para el usuario.

Descripción de la solución del problema:
Primero creamos una variable en la que se guardará el directorio del archivo de
donde obtendremos nuestras palabras y otra variable para guardar las palabras
que irémos obteniendo de acuerdo a las especificaciones que le pidamos, una vez
obtenido esto usaremos el modo lectura solamente y usaremos un for para
eliminar los caracteres de nuestra nueva línea; después otro requisito que vamos
a pedir es que las palabras tengan una longitud de entre 3 y 7 caracteres y
aquellas palabras que cumplan con esto las irémos agregando a nuestra variable
creada en un principio. Ahora escogeremos las dos palabras que queremos para
formar nuestra contraseña, para esto eligiremos primero una palabra al azar con
ayuda de 'randrange' y después harémos lo mismo para escoger la segunda palabra
para que finalmente podamos formar nuestra contraseña final formada por estas
últimas dos palabras obtenidas.
"""
## 
# Genere una contraseña concatenando dos palabras al azar. La contraseña tendrá
# entre 8 y 10 caracteres y cada palabra tendrá al menos tres letras.
#
from random import randrange

WORD_FILE = "C:/Users/cynth.DESKTOP-EVMIHC6/OneDrive/Documentos/programacion-2021-2/Ayudantias/words/"

# Lea todas las palabras del archivo, conservando solo las que tengan
# entre 3 y 7 caracteres de longitud y almacénelas en una lista.
words = []
inf = open(WORD_FILE, "r")
for line in inf:
    # Eliminar el caracter de nueva línea
    line = line.rstrip()
    
    # Mantenga las palabras que tengan entre 3 y 7 letras de longitud
    if len(line) >= 3 and len(line) <= 7:
        words.append(line)
# Cierra el archivo
inf.close()

"""
La contraseña que estamos creando tendrá entre 8 y 10 caracteres de longitud.
Dado que la palabra más corta aceptable tienen 3 letras y una contraseña debe
tener 2 palabras, una contraseña nunca puede contener una palabra de más de 7
letras.
"""

# Seleccione aleatoriamente la primera palabra para la contraseña. Puede ser cualquier palabra
first = words[randrange(0, len(words))]
first = first.capitalize()

# Siga seleccionando una segunda palabra hasta que encontremos una que no haga la
# contraseña demasiado corta o demasiado larga
password = first
while len(password) < 8 or len(password) > 10:
    second = words[randrange(0, len(words))]
    second = second.capitalize()
    password = first + second

# Mostrar la contraseña generada
print("La contraseña aleatoria es: ", password)

"""
Con la traducción no tuve ningún problema, sólo un detalle que tuve al momento
de estar revisando el procedimiento fue que no sabía a qué se refería el método
.rstrip por lo que busqué y supe que era para eliminar cualquier tipo de
caracteres que pidamos o por default elimina todos los que están después de una
cierta palabra y aquí es donde pude entenderlo mejor:
    https://www.w3schools.com/python/ref_string_rstrip.asp
Pero por lo demás no tuve mayor problema en entender qué es lo que se estaba
haciendo.
"""

#%%Ejercicio 153
"""
Christian Feldhaus Hagemeister, 318665050
Ejercicio 153:
La novlea "Gadsby" tiene mas de 50,000 palabras de longitud. Mientras que 50,000 palabras
no son remarcables para una novela, lo es en este caso porque ninguna de las palabras usan
la letra "e". Esta particularidad es muy notable ya que la letra "e" es la más común
en ingles.
Escribe un programa que lea una lista de palabras de un archivo y determine cual
es la proporcion de las palabras que usan cada letra del alfabeto. Muestra el resultado
para todas las 26 letras. Incluye un mensaje adicional verificando la letra que es usada
en menor proporcion en las palabras. Tu programa debe ignorar signos de puntuacion y
debe tratar letras mayusculas y minusculas por igual.
"""
# Dterminar la proporcion de las palabras que incluyen cada letra en el alfabeto
# La letra que es menos usada en las palabras
word_file = 'D:/Documentos/programacion-2021-2/Data/words.txt'
# Un diccionario que contiene el numero de palabras que contienen cada letra
# Iniciar la cuenta de cada letra en 0
contains = {}
for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    contains[ch] = 0

# Abrir el archivo, procesar cada palabra, actualizando los contenidos del diccionario
num_words = 0
inf = open(word_file,"r")
for word in inf:
    # Convertir la palabra a mayusculas y remover el caracter de linea nueva.
    word = word.upper().rstrip()
    
    # Antes de poder actualizar los valores del diccionario necesitamos generar una lista
    # de las letras unicas contenidas en la palabra. De otro modo, aumentariamos los
    # contadores varias veces para palabras que contienen una letra más de una vez.
    # Tambien necesitamos remover guiones que puedan aparecer.
    
    unique = []
    for ch in word:
        if ch not in unique and ch != "-":
            unique.append(ch)
            
    # Ahora incrementamos los contadores para todas las letras úncias en nuestra palabra
    for ch in unique:
        contains[ch] = contains[ch] + 1
    # Contamos el número de palabras que hemos procesado
    num_words += 1
# Cerramos el archivo
inf.close()

# Mostramos el resultado de cada letra. Mientras mostramos el resultado también determinamos
# cual caracter tuvo el contador menor para mostrarlo después.
smallest_count = min(contains.values())
for ch in sorted(contains):
    if contains[ch] == smallest_count:
        smallest_count = ch
    percentage = contains[ch] / num_words * 100
    print(ch,"ocurre en el %.2f por ciento de las palabras." % percentage)

# Mostrar la letra que es más facil de evitar basado en el número de palabras en las que aparece
print()
print("La letra que es más facil de evitar es:" ,smallest_count)    

"""
La transcripcion de este ejercicio fue bastante sencilla. La manera en que se creo y
definió el diccionario me parecio muy ingeniosa y rápida, de haberla visto antes la hubiese
utilizado en la resolución de otro ejercicio.
Los ciclos y condicionales fueron muy sencillos y claros gracias al planteamiento.
La manera de ver cual era la letra menos utilizada fue sencillo así como calcular el
porcentaje en el que aparece cada letra en las palabras.
Me sorprendió la rapidez con la que se procesaron tantas palabras.
No hubo mayores complicaciones.
"""
    
#%%Ejercicio 154
"""
Christian Feldhaus Hagemeister, 318665050
Ejercicio 154:    
La data de nombres de bebes consiste de más de 200 archivos. Cada archivo contiene una
lista de 100 nombres, así como el número de veces que se usaron. Hay dos archivos por año,
uno que contiene los nombres usados para los niños, y otro para los nombres de niñas.
Los datos incluyen informacion de cada año desde 1900 hasta 2012.
Escriba un programa que lea todos los archivos del conjunto de datos e identifique 
todos los nombres que fueron más populares en al menos un año. 
Su programa debería generar dos listas:
una que contiene los nombres más populares para los niños y el otro que contiene los
nombres populares para niñas. Ninguna de sus listas debe incluir valores repetidos 
"""
# Mostrar los nombres de niñas y niños que fueron más populares al menos un año entre 
# 1900 y 2012
path = 'D:/Documentos/programacion-2021-2/Data/BabyNames/'
FIRST_YEAR = 1900
LAST_YEAR = 2012

# Cargar la primera linea del archivo, extraer el nombre y añadirlo a la lista de nombres

from fc.tpw.mer_7 import LoadAndAdd as lad
# Mostrar los nombres de niñas y niños que fueron más populares al menos un año entre 
# 1900 y 2012
def mainLoad():
    # Crear dos listas para almacenar los nombres populares
    girls = []
    boys = []
    # Procesar cada año en el rango, leyendo la primera linea de cada archivo
    for year in range(FIRST_YEAR, LAST_YEAR+1):
        girl_fname = path + str(year) + "_GirlsNames.txt"
        boy_fname = path + str(year) + "_BoysNames.txt"
        lad(girl_fname, girls)
        lad(boy_fname, boys)
    
    # Mostrar las listas
    print("Los nombres de niñas que alcanzaron el #1: ")
    for name in girls:
        print(" ", name)
    print()
        
    print("Los nombres de niños que alcanzaron el #1: ")
    for name in boys:
        print(" ", name)
    print()
    
if __name__ == "__main__":
    mainLoad()


"""
La transcripcion de este ejercicio fue bastante sencilla, trabajamos con este ejercicio en
las ayudantías y esta solución me pareció un poco más complicada ya que hay que definir una
funcion. El código y la solucion me parecieron sencillos.
No hubo mayores complicaciones.
"""
#%%Ejercicio 158: Corrector Ortográfico
"""
@author: Erika Giebele Martinez Mares
Ben Stephenson. (2014). The Python Workbook. Switzerland: Springer., 
Exercise 158: Spell Checker (Corrector Ortográfico)

Descripción del problema:
Un corrector ortográfico puede ser una herramienta útil para las personas que 
luchan por deletrear correctamente las palabras. En este ejercicio, usted escribirá 
un programa que lea un archivo y muestre todas las palabras en él que están mal 
escritas. Las palabras mal escritas se identificarán comprobando cada palabra 
del archivo con una lista de palabras conocidas. Cualquier palabra en el archivo 
del usuario que no aparezca en la lista de palabras conocidas será reportada 
como error ortográfico. 

El usuario proporcionará el nombre del archivo para comprobar los errores 
ortográficos como un parámetro de la línea de comandos. Su programa debe mostrar 
un mensaje de error apropiado si falta el parámetro de la línea de comandos. 
También debe mostrarse un mensaje de error si su programa no puede abrir el 
archivo del usuario. Utilice su solución al Ejercicio 111 cuando cree su solución 
a este ejercicio para que las palabras seguidas de una coma, punto u otro signo 
de puntuación no sean reportadas como errores ortográficos. Ignore las mayúsculas 
de las palabras al comprobar su ortografía. 

Sugerencia: Aunque podría cargar todas las palabras en inglés del conjunto de 
datos de palabras en una lista, la búsqueda en una lista es lenta si utiliza el 
operador in de Python. Es mucho más rápido comprobar si una clave está presente 
en un diccionario, o si un valor está presente en un conjunto. Si utiliza un 
diccionario, las palabras serán las claves. Los valores pueden ser el entero 0 
(o cualquier otro valor) porque los valores nunca serán utilizados.

Descripción de la solución: Este ejercicio se encarga de leer un archivo 
proporcionado por el usuario y detecta los errores en este haciendo uso de un 
módulo que contiene todas la palabras a verificar, si alguna de las palabras 
del archivo del usuario es incorrecta y por lo tanto no se encuentra en el 
archivo principal la marcará como un error. Para esto primero importaremos el 
catálogo de palabras, después el usuario proporcionará el nombre del archivo a 
corregir, a continuación nos aseguraremos de que el programa tiene el número 
correcto de parámetros, después el programa deberá asegurarse de que el archivo 
proporcionado se puede abrir correctamente de los contrario se avisará al usuario. 
Lo siguiente será cargar todas las palabras en un diccionario de palabras válidas, 
para esto se creará una el diccionario “valido”, después nombraremos al archivo 
abierto como archivo_palabras y cada palabra en el archivo se convertirá a 
minúsculas y se eliminará el espacio al final, esto con .lower() y con .rstrip(), 
a continuación se asocia el valor cero a las palabras válidas y cerraremos el 
archivo palabras. Después se leerá cada línea del archivo, añadiendo las 
palabras mal escritas a la lista de errores ortográficos, para esto se 
descartaran los signos de puntuación haciendo uso de la función creada en el 
ejercicio 111 eliminarCaracteres(), si alguna palabra es errónea se agregara a 
la lista malescrita y después se cerrará el archivo. Por último se mostrarán las 
palabras mal escritas o se avisará que no hay errores en el documento.
"""
##
# Encuentra y lista todas las palabras de un archivo que están mal escritas.
#

from me_5 import eliminarCaracteres
from sys import argv

WORDS_FILE = "../Data/words.txt"

#Asegúrate de que el programa tiene el número correcto de parámetros en la línea de comandos
if len(argv) != 2:
    print("Debe proporcionarse un parámetro de línea de comandos. Saliendo...")
    quit()

#Abrir el archivo. Salir si el archivo no se abre con éxito.
try:
    inf = open(argv[1], "r")
except: 
    print("Fallo al abrir '%s' para lectura. Saliendo..." % argv[1])
    quit()
    
#Carga todas las palabras en un diccionario de palabras válidas. El
# valor 0 se asocia a cada palabra, pero nunca se utiliza.
valido = {}
archivo_palabras = open(WORDS_FILE, "r")
for palabra in archivo_palabras:
    palabra = palabra.lower().rstrip()
    valido[palabra] = 0
archivo_palabras.close()

# Leer cada línea del archivo, añadiendo las palabras mal escritas
# a la lista de errores ortográficos
malescritas = []
for linea in inf:
    #Descartar los signos de puntuación llamando a la función desarrollada en el Ejercicio 111
    palabras = eliminarCaracteres(linea)
    for palabra in palabras:
        #Sólo añadir a la lista de palabras mal escritas si la palabra está mal escrita y no está ya en la lista
        if palabra.lower() not in valido and palabra not in malescritas:
            malescritas.append(palabra)
#Cierre el archivo que se está comprobando
inf.close()

#Mostrar las palabras mal escritas, o un mensaje indicando que no hay palabras mal escritas
if len(malescritas) == 0:
    print("No hay palabras mal escritas.")
else:
    print("Las siguientes palabras están mal escritas:")
    for palabra in malescritas:
        print(" ", palabra)


"""Esta solución utiliza un diccionario, pero los valores del diccionario nunca 
se utilizan. Como resultado, un conjunto sería una mejor opción si ha aprendido 
sobre esa estructura de datos. No se utiliza una lista porque comprobar si una
clave está en un diccionario es más rápido que comprobar si un elemento está en 
una lista.
Este ejercicio fue un poco más complicado de lo que parece, pues me confundí un 
poco con los nombres de las funciones importadas, el primero lo cambié a español 
para que fuera más claro y más fácil de entender, por eso en la traducción me 
confundí un poco. También tuve que recordar un poco las siguientes funciones 
básicas y otra que no recordaba: lower se utiliza para hacer una copia de la 
cadena en minúsculas. El rstrip()método elimina cualquier carácter final 
(caracteres al final de una cadena), el espacio es el carácter final 
predeterminado para eliminar y append() este método nos permite agregar nuevos 
elementos a una lista. 

En cuanto a la traducción no hubo más que un pequeño problema ocasionado por los 
espacios a la hora de traducirlo. El código es claro, además de que los 
comentarios ayudan mucho a comprender mejor lo que está a continuación de ellos. 
La implementación de los ciclos y las condicionales es clara.  

uniwebsidad. (s. f.). 6.1. Métodos de formato (Python para principiantes). 
Recuperado 10 de enero de 2022, de 
https://uniwebsidad.com/libros/python/capitulo-6/metodos-de-formato
Python String rstrip() Method. (s. f.). W3schools. Recuperado 10 de enero de 
2022, de https://www.w3schools.com/python/ref_string_rstrip.asp
Listas en Python. (2017, 19 septiembre). DevCode Tutoriales. Recuperado 10 de 
enero de 2022, de https://devcode.la/tutoriales/listas-python/
"""      

#%%Ejercicio 160: Redactar Texto en un Archivo
"""
@author: Erika Giebele Martinez Mares
Ben Stephenson. (2014). The Python Workbook. Switzerland: Springer.,
Exercise 160: Redacting Text in a File (Redactar Texto en un Archivo)

Descripción del problemma:
La información sensible es a menudo eliminada, o redactada, de los documentos 
antes de que sean liberados al público. Cuando los documentos se publican, es 
común que el texto redactado sea reemplazado por barras negras. 

En este ejercicio escribirás un programa que redacte todas las apariciones de 
palabras sensibles en un archivo de texto sustituyéndolas por asteriscos. Su 
programa debe redactar las palabras sensibles dondequiera que aparezcan, incluso 
si aparecen en medio de otra palabra. La lista de palabras sensibles se 
proporcionará en un archivo de texto separado. Guarde la versión redactada del 
texto original en un nuevo archivo. Los nombres del archivo de texto original, 
del archivo de palabras sensibles y del archivo redactado serán proporcionados 
por el usuario. 

El método de reemplazo de cadenas puede resultarle útil para realizar este ejercicio. 
Puede encontrar información sobre el método de reemplazo en su libro de texto o 
en Internet.

Para un desafío adicional, amplíe su programa para que redacte las palabras sin 
tener en cuenta las mayúsculas y minúsculas. Por ejemplo, si examen aparece en 
la lista de palabras sensibles, entonces redacte examen, Exam, ExaM y EXAM, 
entre otras posibles mayúsculas.

Descripción de la solución:
Este ejercicio tiene como objetivo sustituir las palabras sensibles por 
asteriscos de un archivo de texto sin importar en qué lugar se encuentren. La 
lista de palabras sensibles será proporcionada en un archivo aparte y recordemos 
que los nombres del archivo de texto original, del archivo de palabras sensibles 
y del archivo redactado serán proporcionados 
por el usuario. 

Para primero obtendremos el nombre del archivo por parte del usuario y lo 
abriremos después cargaremos todas las palabras sensibles y las almacenaremos 
en una lista, en este paso se creará un ciclo while para agregar las palabras 
y en el cuerpo de este se quitaran los espacios finales y se utilizara el método 
append para agregar las palabras a dicha lista por último cerraremos el archivo, 
después de obtendra el nombre del archivo de salida y se abrirá, a continuación 
se leerá el archivo de entrada y se reemplazarán las palabras sensibles por 
asteriscos, el número de asteriscos coincidirá con el número de letras en la 
palabra sensible reemplazada. Por último se cerrarán los archivos de entrada y 
de salida.

"""
##
# Redactar un archivo de texto eliminando todas las apariciones de palabras sensibles.
# La versión rediseñada del texto se escribe en un nuevo archivo.
#
# Tenga en cuenta que este programa no realiza ninguna comprobación de errores, y 
# no implementa la redacción sin distinción de mayúsculas y minúsculas.
#

# Obtenga el nombre del archivo input y ábralo

inf_name = input("Introduzca el nombre del archivo de texto a redactar:  ")
inf = open(inf_name, "r")

#Obtener el nombre del archivo de palabras sensibles y abrirlo
sen_name = input("Introduzca el nombre del archivo de palabras sensibles: ")
sen = open(sen_name, " r")

#Carga todas las palabras sensibles en una lista
palabras = []
line = sen.readline()
while line != "":
    line = line.rstrip()
    palabras.append(line)
    
    line = sen.readline()
    
sen.close()

#Obtener el nombre del archivo de salida y abrirlo 
outf_name = input("Introduzca el nombre del nuevo archivo redactado: ")
outf = open(outf_name, "w")

#Leer cada línea del archivo de entrada. Reemplazar todas las palabras sensibles
#con asteriscos. A continuación, escriba la línea en el archivo de salida.
line = inf.readline()
while line != "":
    #Comprueba y reemplaza cada palabra sensible. Utilice un número de asteriscos que
    # coincida con el número de letras de la palabra
    for palabra in palabras:
        line = line.replace(palabra, "*" * len(palabra))
    #Escribir la línea modificada en el archivo de salida
    outf.write(line)
    
    #Leer la siguiente línea del fichero de entrada
    line = inf.readline()
    
#Cerrar los archivos de entrada y salida
inf.close()
outf.close()

"""El archivo de palabras sensibles puede cerrarse ahora porque todas las 
palabras han sido leído en una lista. 
En este ejercicio no hubo ningún problema en cuanto a la traducción y tampoco 
en cuanto a la redacción de este, las instrucciones eran bastante claras excepto 
por la última parte en la que pedía que contemplara tanto las mayúsculas como a 
alas minúsculas pues al final no se si pedía que salieran de la misma forma en 
que habían entrado, es decir, si tenia que salir con mayusculas y minusculas. 
Lo más complicado de este fue hacer los documentos para corroborar que el programa 
funcionaba, tanto el archivo de texto completo como el archivo de texto con las 
palabras sensibles. 
"""        

#%%Ejercicio 161: Comentarios que faltan
"""
@author: Erika Giebele Martinez Mares
Ben Stephenson. (2014). The Python Workbook. Switzerland: Springer.,
Exercise 161: Missing Comments (Comentarios que faltan)

Descripción del problema:
Cuando uno escribe una función, generalmente es una buena idea incluir un 
comentario que describa el propósito de la función, sus parámetros y su valor 
de retorno. Sin embargo, a veces los comentarios se olvidan, o son omitidos 
por programadores bien intencionados que planean escribirlos más tarde pero 
nunca llegan a hacerlo. 

Cree un programa python que lea uno o más archivos fuente de Python e identifique 
las funciones que no están inmediatamente precedidas por un comentario. Para los 
propósitos de este ejercicio, asuma que cualquier línea que comience con def, 
seguida de un espacio, es el comienzo de una definición de función. Asume que 
el carácter de comentario, #, será el primer carácter de la línea anterior cuando 
la función tenga un comentario. Muestre los nombres de todas las funciones que 
carecen de comentarios, junto con el nombre del archivo y el número de línea donde 
se encuentra la definición de la función. 

El usuario proporcionará los nombres de uno o más archivos de Python como parámetros 
de la línea de comandos. Si el programa encuentra un archivo que no existe o 
que no se puede abrir, debe mostrar un mensaje de error apropiado antes de seguir 
adelante y procesar los archivos restantes.

Descripción de la solución:
    La idea de este ejercicio es leer archivos de python y verificar si las 
funciones definidas en estos si es que las tiene está documentadas, es decir, 
si la función está seguida por un contrario en el que se especifica el uso y 
funcionamiento de la función así como los parámetros de esta. Para esto haremos 
que el usuario ingrese el o los archivos a analizar y lo primero será ver si 
el archivo se puede abrir correctamente de lo contrario se mostrará un mensaje 
pertinente para avisar al usuario. 

Entonces los primero será verificar que se ha proporcionado el nombre de a lo 
menos un archivo, después intentaremos procesar los archivos anteriormente 
mencionados, después a medida de que nos movemos tendremos que mantener una 
copia para poder verificar si empieza con las comillas que nos indique que la 
función la prosigue un comentario y también necesitamos mantener un registro 
del número de línea dentro del archivo, después comprobaremos una por una las 
líneas del archivo y si la línea es una definición pero lo que sigue no es un 
comentario, luego buscaremos y mostraremos la información de la función a la que 
le falta el comentario.  Por último si el archivo no se abre correctamente se 
mostrará el comentario al usuario.

"""
#
# Encontrar y mostrar los nombres de las funciones de Python que no están 
# inmediatamente precedidas por un comentario.
# 
from sys import argv

#Verifica que se ha proporcionado al menos un nombre de archivo como parámetro 
#de la línea de comandos
if len(argv) == 1:
    print("Al menos un nombre de archivo debe ser proporcionado como un", \
          "parámetro de línea de comandos.")
    print("Saliendo...")
    quit()
    
#Procesar cada archivo proporcionado como parámetro de la línea de comandos
for fname in argv[1 : len(argv)]:
    #Intenta procesar el fichero
    try:
        inf = open(fname, "r")
        
        #A medida que nos movemos por el fichero necesitamos mantener una copia de la línea anterior
        #línea anterior para poder comprobar si empieza con un carácter de comentario.
        #También necesitamos mantener un registro del número de línea dentro del archivo.
        prev = " "
        lnum = 1
        
        #Comprobar cada línea en el archivo actual
        for line in inf:
            #Si la línea es una definición de función y la línea anterior no es un comentario
            if line.starswith("def ") and prev[0] != "#":
                #Busca el primero (en la línea para que sepamos dónde termina el nombre de la función)
                bracket_pos = line.index("(")
                name = line[4: bracket_pos]
                
                #Mostrar información sobre la función a la que le falta el comentario
                print("%s line %d: %s" %(fname, lnum, name))
                
        #Guarda la línea actual y actualiza el contador de líneas
        prev = line
        lnum = lnum + 1
        #Cierre el archivo actual
        inf.close()
    
    except:
       print("Se ha encontrado un problema con el fichero '%s'." % fname)
       print("Pasando al siguiente fichero...")
        
        
"""La variable prev debe ser inicializada a una cadena que tenga al menos un 
carácter de longitud. De lo contrario, el programa se bloqueará cuando la primera línea del 
archivo que se está comprobando es una definición de función.
 En este ejercicio no hubo complicaciones en cuanto a la traducción, pero sí se 
presentaron dos errores a la hora de transcribir el código, en las líneas 
siguientes: “except” y “inf.close”, volví a transcribir el código y me asegure 
de que todo estuviera bien definido y escrito pero se volvieron a presentar, al 
final resultó que el problema eran los niveles de indentación de estas dos 
partes del código, asi que volvi a analizar de nuevo el código y corregi los 
niveles. Por parte del ejercicio tampoco hubo ningún problema, después de corregir 
el código todo quedó claro.

"""

