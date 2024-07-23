# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 10:48:29 2021

@author: pc1
"""

#%%Ejercicio 131: Codigo Morse:(INDIVIUAL)
"""El código Morse es un esquema de codificación que usa guiones y puntos para 
representar números y letras. En este ejercicio, escribirá un programa que usa 
un diccionario para almacenar el mapeo de letras y números al código Morse. 
Utilice un punto para representar un punto y un guión para representar un guión. 
El mapeo de letras y números a guiones y puntos se muestra en la Tabla 6.1.
Su programa debería leer un mensaje del usuario. Luego, debe traducir cada letra
y número del mensaje al código Morse, dejando un espacio entre cada secuencia de 
guiones y puntos. Su programa debe ignorar cualquier carácter que no sea letras 
ni números. El código Morse para Hello, World! se muestra a continuación:
    .... . .-.. .-.. --- .-- --- .-. .-.. -..
Tabla6.1:
    Letter Code Letter Code Letter Code Number Code
       A   .-     J    .- - -  S   ...    1    .- - - -
       B   -...   K    -.-     T   -      2    ..- - -
       C   -.-.   L    .-..    U   ..-    3    ...- -
       D   -..    M    - -     V   ...-   4    ....-
       E   .      N    -.      W   .- -   5    .....
       F   ..-.   O    ---     X   -..-   6    -....
       G   - -.   P    .- -.   Y   -.- -  7    - -...
       H   ....   Q    - -.-   Z   - -..  8    - - -..
       I   ..     R    .-.     0   -----  9    - - - -.
El código Morse se desarrolló originalmente en el siglo XIX para su uso a través de
cables de telégrafo. Todavía se utiliza hoy en día, más de 160 años después de su creación.
"""

MorseCodigos = {"A": ".- ",  "J": ".- - - ", "S": "... ",  "1": ".- - - - ",
        "B": "-... ", "K": "-.- ",   "T": "- ",     "2": "..- - - ",
        "C": "-.-. ", "L": ".-.. ",  "U": "..- ",   "3": "...- - ",
        "D": "-.. ",  "M": "- - ",   "V": "...- ",  "4": "....- ",
        "E": ". ",    "N": "-. ",    "W": ".- - ",  "5": "..... ",
        "F": "..-. ", "O": "--- ",   "X": "-..- ",  "6": "-.... ",
        "G": "- -. ", "P": ".- -. ", "Y": "-.- - ", "7": "- -... ",
        "H": ".... ", "Q": "- -.- ", "Z": "- -.. ", "8": "- - -.. ",
        "I": ".. ",   "R": ".-. ",   "0": "----- ", "9": "- - - -. " }
#El usuario coloca la cadena
cadena = input("Ingresa la cadena que quieres convertir a codigo morse: ") 
signos_de_orto = ",.!¿?¡; :" # nombremos una cadena con los signos de ortografia
cadenaNueva = "" # creamos una cadena vacia
#Para el elemento de la cadena que sea un signo se lo quitamos
for i in signos_de_orto:
    cadena = cadena.replace(i, "")
#Revisamos si cada simbolo de la cadena esta en el diccionario
for simbolo in cadena:
    if not simbolo.upper() in morse.keys():
        print("El simbolo " + simbolo + " no se reconoce")
        break
    cadenaNueva += morse[simbolo.upper()]#Agregamos los codigos en morse a la cadena
print(cadenaNueva)
"No hubo complicaciones"
#%%Ejercicio 132: Codigo Postal (INIVIDUAL)
"""En un código postal canadiense, el primer, tercer y quinto carácter son letras, 
mientras que el segundo, cuarto y sexto caracteres son números. La provincia se 
puede determinar a partir del primer carácter de un código postal, como se muestra 
en la siguiente tabla. Actualmente, no hay códigos postales válidos que comiencen 
con D, F, I, O, Q, U, W o Z.
El segundo carácter de un código postal identifica si la dirección es rural o urbana. 
Si ese carácter es un 0, entonces la dirección es rural. De lo contrario, es urbano.
Cree un programa que lea un código postal del usuario y muestre la provincia asociada
a él, junto con si la dirección es urbana o rural. Por ejemplo, si el usuario ingresa 
T2N 1N4, su programa debe indicar que el código postal es para una dirección urbana 
en Alberta. Si el usuario ingresa X0A 1B2, entonces su programa debe indicar que el 
código postal es para una dirección rural en Nunavut o Territorios del Noroeste. 
Utilice un diccionario para mapear desde el primer carácter del código postal hasta 
el nombre de la provincia. Muestra un mensaje de error significativo si el código 
postal comienza con un carácter no válido."""
Provincias = {   
        "A":"Newfoundland",
        "B" : "Nova Scotia",
        "C" : "Prince Edward Island",
        "E" : "New Brunswick",
        "G" : "Quebec",
        "H" : "Quebec",
        "J" : "Quebec",
        "K" : "Ontario",
        "L" : "Ontario",
        "M" : "Ontario",
        "N" : "Ontario",
        "P" : "Ontario",
        "R" : "Manitoba",
        "S" : "Saskatchewan",
        "T" : "Alberta",
        "V" : "British Columbia",
        "X" : "Nunavut o en Northwest Territories",
        "Y" : "Yukon" }
#Le pedimos al usuario la cadena del codigo postal
cadena = input("Escribe el codigo postal de que se quiere residencia")
#Definimos una cadena con las letras que no tiene valor en el codigo postal
invalidos = "D, F, I, O, Q, U, W, Z"
#Revisamos si la primera letra esta en invalidos para avisar que ese no esta definido en el codigo postal
for j in invalidos:
    if cadena[0] == j: 
        print("Codígo postal invalido")
#Revisamos si el primer simbolo es una llave en el diccionario y definimos una variable con el valor de esa llave
for simbolo in Provincias.keys():
    if cadena[0]==simbolo:
        i=Provincias[simbolo]
#Revisamos si el segundo simbolo es 0 imprimimos que se trata de una direccion rural
if cadena[1]=="0":
    print("LA DIRECCION RURAL:",i)
else:
    print("LA DIRECCION URBANA:",i)# Imprime una direccion urbana
"No hubo complicaciones"
 
 
#%%Ejercicios 135:Anagramas(HUGO)
"""Dos palabras son anagramas si contienen todas las mismas letras, pero en diferentes
pedido. Por ejemplo, "evil" y "life" son anagramas porque cada uno contiene una e, una
i, una l y una v. Cree un programa que lea dos cadenas del usuario, determina
sean o no anagramas, e informa el resultado."""
from me_6 import main
main()
#%%Ejercicio 136:(INDIVIDUAL)
"""La noción de anagramas se puede extender a varias palabras. Por ejemplo, 
"William Shakespeare" y "Soy un ortográfico débil" son anagramas cuando se 
ignoran las mayúsculas y los espacios.
Amplíe su programa del ejercicio 135 para que pueda comprobar si dos frases son anagramas.
Su programa debe ignorar las mayúsculas, los signos de puntuación y el espaciado al tomar 
la determinación."""
from me_6 import mainn
main()
#%%Ejercicio 140:
"""En este ejercicio escribirás un programa que simule un juego de Bingo para un solo
tarjeta. Comience generando una lista de todas las llamadas válidas de Bingo (B1 a O75).
Una vez la lista ha sido creada, puede aleatorizar el orden de sus elementos llamando a la
función aleatoria en el módulo aleatorio. Entonces su programa debería consumir llamadas
fuera de la lista, tachando los números de la tarjeta, hasta que la tarjeta contenga un
línea (horizontal, vertical o diagonal). Simule 1,000 juegos e informe el mínimo,
número máximo y promedio de llamadas que se deben realizar antes de que gane la tarjeta. 
Importar sus soluciones a los Ejercicios 138 y 139 al completar este ejercicio"""
import 
while k in range(1000):
    a=crearcarta()
    resultados = revisar(cartas_creadas)
    for i in ['B','I','N','G','O']:
        for j in range(5):
            if resultados[1][i][j] == 0:
                n+=1  
    val.append(n)
    n=0