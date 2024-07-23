# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 00:56:09 2021

@author: Bianca Ramirez Mejia 421117321 Octaedros Dorados
"""

#%% Ejercicio 129: Simulación de dos dados
"""
@author: Daniela Flores Cruz 318099567
Ejercicio 129: Simulación de dos dados
(Resuelto-42 líneas)

En este ejercicio vas a simular 1.000 tiradas de dos dados. Comience escribiendo
una función que simule el lanzamiento de un par de dados de seis caras.
Tu función no tomará ningún parámetro. Devolverá como único resultado el total 
que se ha tirado en los dos dados.

Escribe un programa principal que utilice tu función para simular 
el lanzamiento de dos dados de seis caras 1.000 veces. Mientras tu programa 
se ejecuta, debe contar el número de veces que se produce cada total. 
Luego debe mostrar una tabla que resuma estos datos. Expresa la frecuencia de 
cada total como un porcentaje del número total de tiradas. Su programa también
debe mostrar el porcentaje esperado por la teoría de la probabilidad para cada
total. A continuación se muestra un ejemplo de salida.

Total Porcentaje simulado Porcentaje esperado
2                 2.90           2.74
3                 6.20           5.56
4                 9.40           8.33
5                11.90          11.11
6                14.20          13.89
7                14.20          16.67
8                15.00          13.89
9                10.50          11.11
10                7.90           8.33
11                4.50           5.56
12                2.60           2.76

solución: 
    primero hacemos un funcion que nos devuelve el total de veces al tirar dos
    dados, consideramos dos variables una es nuesro dado 1 y el otro es el dado 2, 
    considemaros su rango que es el total de caras y los sumamos.
    Luego considemaros otra fuancion la cual los va a regresar la tabla, 
    es una función sin parametros donde creamos dos diccionarios una con
    la proporcion esperada y la otra con las ocurrencias,luego de nuestras 
    1000 tiradas empezamos un clico que nos mostrará las tiradas con un contador
    de cada una. Luego mostramos la trabla.
"""
from mer_6 import main_dosDados

main_dosDados()

"""
En este ejercicio igual tuve un problema que no note tan facil, una vez que 
acabe de transcribir el código de la función main_dosDados en la ultima linea
me marcaba un erro pero no entendia el porqué, entonces pensé que se trataba de
un parentesis, o de una coma, pero no, igual revise que lo estuviera escribiendo
bien, que  no me ubiera comido una letra y si había un error, cuando cree el
diccionario de las porciones esperadas, yo le puse expeted y en la ultima parte
estaba usando o poniendo expected pero, ya una vez que lo cambie me seguía marcando
error, entonces ya no sabía porque, luego le mande un correo al profesor 
porqur ya tenía dos problemas, pero cuando estabamos revisando me di cuenta que 
cuando estaba definiendo mi diccionario expected estaba poniendo : en 
vez de poner = , una vez que lo cambie ya no me marcaba error, ese fue mi unico problema.
"""          
#%% Ejercicio 130: Mensaje de texto(HUGO)
"""
Descripción del problema: Algunos celulares basicos, los mensajes de texto pueden
    ser enviados usando el teclado númerico. Como cada llave tienen multiples 
    letras asociadas con sigo misma, precionar multipoles veces una llave es necesario
    para más letras. Presionar el número una vez genera la primer letra de la llave,
    presionar 2, 3, 4, o 5, veces generan el segundo, tercero, cuarto o quinto 
    caracter listado para la llave.
        llave   símbolos   
         #1      .,?!:
         #2      ABC
         #3      DEF
         #4      GHI
         #5      JKL
         #6      MNO
         #7      PQRS
         #8      TUV
         #9      XYZ
         #0      ESPACIO 
    
    Escriba un programa que muestre las pulsaciones de teclas que hay que hacer para introducir un texto
    leído por el usuario. Construya un diccionario que mapee desde cada letra o
    símbolo a las pulsaciones de las teclas. A continuación, utilice el diccionario para generar y mostrar las pulsaciones
    para el mensaje del usuario. Por ejemplo, si el usuario introduce ¡Hola, Mundo! entonces su
    debería mostrar 44335555666110966677755531111. Asegúrese de que
    su programa maneja tanto las letras mayúsculas como las minúsculas. Ignore los caracteres
    que no aparezcan en la tabla anterior, como el punto y coma y los paréntesis.

Traducción realizada con la versión gratuita del traductor www.DeepL.com/Translator

"""
"Solución del ejercicio:"
# creamos el diccionario para el valor (numeros) y el simbolo
dicti1 = {"." : "1", ",": "11", "?": "111", "!": "1111", ":": "11111" ,
        "A": "2", "B": "22", "C": "222",
        "D": "3", "E": "33", "F": "333",
        "G": "4", "H": "44", "I": "444",
        "J": "5", "K": "55", "L": "555",
        "M": "6", "N": "66", "O": "666",
        "P": "7", "Q": "77", "R": "777", "S": "7777",
        "T": "8", "U": "88", "V": "888",
        "W": "9", "X": "99", "Y": "999", "Z": "9999",
        " ": "0"
        }
cadena = input("Ingresa una texto ") # pedimos una cadena del usuario
cadenadtap = "" # creamos una cadena vacia
for simbolo in cadena: # para cada simbolo de la cadena 
    if not simbolo.upper() in dicti1.keys(): # comvertimos en mayúsculas y llamamos al diccionario
        print("El simbolo " + simbolo + " no esta en el dicccionario") # si no está en el diccionario imprimimos que no está
        break

    cadenadtap += dicti1[simbolo.upper()]
    # agregamos los simbolos que estan en el diccionario a una cadena para imprimirla
print(cadenadtap)

"No hubo problemas con este código"
#%%Ejercicio 133(HUGO)
"""Descripcion del problema:
Si bien la popularidad de los cheques como método de pago ha disminuido en los últimos
años, algunas empresas todavía los emiten para pagar a los empleados o proveedores.
La cantidad es pagada normalmente aparece en un cheque dos veces, con una ocurrencia 
escrita con dígitos, y el otro caso escrito con palabras en inglés. Repitiendo la 
cantidad en dos las diferentes formas lo hacen mucho más difícil para un empleado o 
proveedor sin escrúpulos,para modificar el monto del cheque antes de depositarlo.
En este ejercicio, su tarea es crear una función que tome un número entero entre 0 y
999 como su único parámetro, y devuelve una cadena que contiene las palabras en inglés 
para ese número. Por ejemplo, si el parámetro de la función es 142, entonces su función 
debería devolver "ciento cuarenta y dos". Utilice uno o más diccionarios para implementar
su solución en lugar de grandes construcciones if / elif / else. Incluya un programa
principal que lee un número entero del usuario y muestra su valor en palabras en inglés."""
cientos = {100:"One Hundred", 
           200:"Two Hundred",
           300:"Three Hundred",
           400:"Four Hundred",
           500:"Five Hundred",
           600:"Six Hundred",
           700:"Seven Hundred",
           800:"Eight Hundred",
           900:"Nine Hundred",
          }

decenas = {20:"Twenty",
           30:"Thirty",
           40:"Fourty",
           50:"Fifty",
           60:"Sixty",
           70:"Seventy",
           80:"Eighty",
           90:"Ninety",
          }

unidades = {1:"One",
            2:"Two",
            3:"Three",
            4:"Four",
            5:"Five",
            6:"Six",
            7:"Seven",
            8:"Eight",
            9:"Nine",
            10:"Ten",
            11:"Eleven",
            12:"Twelve",
            13:"Thirteen",
            14:"Fourteen",
            15:"Fifteen",
            16:"Sixteen",
            17:"Seventeen",
            18:"Eighteen",
            19:"NineTeen"}
def numeroIngles(numero):
    numero = int(input("Escribe el numero del que quieres su nombre en ingles"))
    if 1<numero<=100:
        parteADosDigitosDelNumero = (numero % 100)
        cientosEnElNumeros = (numero - parteADosDigitosDelNumero)
        if cientosEnElNumeros in cientos:
            print(cientos[cientosEnElNumeros])

        parteAUnDigitoDelNumero = parteADosDigitosDelNumero % 10
        decenasEnElNumero = parteADosDigitosDelNumero - parteAUnDigitoDelNumero
        if decenasEnElNumero in decenas:
            print(numerodecenas[decenasEnElNumero])
            if parteAUnDigitoDelNumero in unidades:
                print(unidades[parteAUnDigitoDelNumero])
        else:
            if parteADosDigitosDelNumero in unidades:
                print(unidades[parteADosDigitosDelNumero])
        if numero == 0:
            print ("Zero")
    else:
        print("ERROR")

numeroIngles(numero)
#%%Ejercicio 134:Unicos caracteres
"""@author: Bianca Ramirez Mejia"""

""" DESCRIPCION DEL EJERCICIO 134
Cree un programa que determine y muestre el número de caracteres únicos en un
cadena ingresada por el usuario. Por ejemplo, ¡Hola, mundo! tiene 10 caracteres 
únicos, whilezzz tiene un solo carácter único. Utilice un diccionario o un set 
para resolver este problema."""


"""Primero crearemos una funcion llamada numcaracteresunicos para mostrar el numero
de caracateres unicos de la cadena que se ingrese"""
def numcaracteresunicos(s): 
    #Definimos a la cadena ingresada como "s"
    s=input("escribe una cadena sin espacios")
    #Creamos una lista vacia para ir agregando cuales son los caracteres unicos
    unico_caracter = []
    #Creamos un ciclo for para repetir el proceso del if hasta que termine con todos los simbolos
    for simbolo in s:
        #Con el if not vemos que simbolos no estan en unico_caracter, si estan ya no se agregan
        if not simbolo in unico_caracter:
            unico_caracter.append(simbolo)
    #Este print nos muestra los caracteres unicos que tiene "s"         
    print(unico_caracter)        
    #La variable numcaracter obtiene la longitud de la lista unico_caracter       
    numcaracter=len(unico_caracter)
    print(numcaracter)  
#%% Ejercicio 137: Puntuación de Scrabble
"""
@author: Daniela Flores Cruz 318099567
Ejercicio 137: Puntuación de Scrabble™
(Resuelto-18 líneas)

En el juego de Scrabble™, cada letra tiene puntos asociados. La puntuación 
total de una palabra es la suma de las puntuaciones de sus letras. 
Las letras más comunes valen menos puntos mientras que las menos comunes 
valen más puntos. A continuación se muestran los puntos asociados a cada letra:

Un punto
A, E, I, L, N, O, R, S, T y U

Dos puntos
D y G

Tres puntos
B, C, M y P

Cuatro puntos
F, H, V, W e Y

Cinco puntos
K

Ocho puntos
J y X

Diez puntos
Q y Z

Escribe un programa que calcule y muestre la puntuación de Scrabble™ de una palabra.
Crea un diccionario que relacione las letras con los valores de los puntos. 
A continuación, utiliza el diccionario para calcular la puntuación.

Un tablero de Scrabble™ incluye algunas casillas que multiplican el valor de
una letra o el valor de una palabra entera. En este ejercicio ignoraremos 
estas casillas.
Solución:
    Primero creamos un diccionario que tenga los valores que le corresponde
    a cada una de las letras en el abecedario, luego le pedimos al 
    usuaro la palabra que quiere que se calcule y la volvemos mayuscalas
    todas sus letras para no tener problema al momento de asignarle un valor, 
    igual creamos una variable que nos va a ir sumando los valores que tiene 
    cada una de las letras en la palabra, con un ciclo vamos recorriendo cada 
    una de las letrs de nuestra palabra y con un contador vamos agregando
    los valores, por ultimo mostramos su palabra y su valor.
"""
##
# Utiliza un diccionario para calcular la puntuación Scrable TM de una palabra.
#

#Inicializar el diccionario para que mapee las letras de la forma a los pines
puntos ={"A":1, "B":3, "C":3, "D":2, "E":1, "F":4,\
         "G":2,"H":4,"I":1,"J":2,"K":5,"L":1, \
        "M":3,"N":1,"O":1,"P":3,"Q":10,"R":1,\
            "S":1,"T":1,"U":1,"V":4,"W":4,"X":8,"Y":4,"Z":10}

#Leer una palabra del usuario
palabra = input("Introduzca una palabra: ")

#Calcular la puntuación de la palabra
mayusculas = palabra.upper()
puntuacion=0
for ch in mayusculas:
    puntuacion = puntuacion + puntos[ch]
    
#Mostrar el resultado
print(palabra, "vale", puntuacion, "puntos")
"""
En este ejercicio no tuve problemas, ni de traducción, ni de comprender el 
código, de hecho este programa me gusto se me hizo interesante pues
ya he jugado este juego de mesa.
"""
#%%Ejercicio 138(HUGO)
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
