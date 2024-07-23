# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 18:12:21 2022

@author: Bianca Ramirez Mejia 421117321
"""

#%%Ejercicio 165: Máximo común divisor
"""
Euclides fue un matemático griego que vivió hace aproximadamente 2.300 años. 
Su algoritmo para calcular el máximo común divisor de dos enteros positivos, a y b,
es eficiente y recursivo. Se describe a continuación:
    Si b es 0, entonces
       Devuelve a
    Si no,
       Establecer c como el resto de la división de a por b
       Devuelve el máximo común divisor de b y c
       
Escribe un programa que implemente el algoritmo de Euclides y lo utilice para 
determinar el mayor común divisor de dos enteros introducidos por el usuario.

Traducción realizada con la versión gratuita del traductor www.DeepL.com/Translator"""

def MCD(a, b):
    """
    Muestra el maximo cumun divisor de dos enteros

    Parameters
    ----------
    a :type int:
        primer numero entero
    b: TYPE, int:
        segundo numero entero

    Returns
    -------
    None.

    """
    #Vemos que si el valor b es igual a cero entonces el maximo comun divisor el el otro 
    #numero ingresado, este seria nuestro caso base
    if b ==0:
        return a
    #Cuando el valor es distinto de cero, entonces definimos una nueva variable c que es el
    #residuo de dividir nuestro valores, ahora con esta nueva variable se repetira el ciclo
    #MCD para obtener el maximo cumun divisor
    else:
        c = a%b
        return MCD(b, c)
#Hacemos nuestra funcion main1 para pedirle al usuario los datos y con estos tomar la funcion
#MCD de estos datos
def main1():
    a = int(input("Escribe el primer entero"))
    b = int(input("Escribe el segundo entero"))
    print(MCD(a, b))
#Mandamos a llamar a la funcion main1 para que se ejecute nuestro codigo
main1()

"""Complicaciones:
Tuve un pequeño problema en comprender a lo que se referia el enunciado pues pense que 
debiamos modificar el algoritmo de Euclides pero despues de releerlo me di cuenta que
solo era implementar ese mismo"""

#%%Ejercicio 166:Decimal recursiva a binaria
"""En el Ejercicio 78 escribiste un programa que utiliza un bucle para convertir 
un número decimal a su representación binaria. 
En este ejercicio realizarás la misma tarea usando recursividad.
Escribe una función recursiva que convierta un número decimal no negativo a binario.
Trata el 0 y el 1 como casos base que devuelven una cadena que contiene el dígito 
apropiado. Para todos los demás enteros positivos, n, debe calcular el siguiente 
dígito utilizando el operador de resto y luego hacer una llamada recursiva a 
calcular los dígitos de n // 2. Por último, debe concatenar el resultado de la 
llamada recursiva (que será una cadena) y el siguiente dígito (que tendrá que 
convertir en una cadena) y devolver esta cadena como el resultado de la función. 
Escribe un programa principal que utilice tu función recursiva para convertir un 
entero no negativo  introducido por el usuario de decimal a binario. 
Su programa debe mostrar un mensaje de error apropiado si el usuario introduce un 
valor negativo.

Traducción realizada con la versión gratuita del traductor www.DeepL.com/Translator"""
def deci_bina(numero):
    """
    Muestra el "numero" en decimal no negativo a uno binaria

    Parameters
    ----------
    numero :type float:
        numero decimal
    

    Returns
    -------
    None.
    """
    #Revisamos nuestro flotante es no negativo, es decir si es positivo
    #Cuando esto ocurre seguimos con el proceso para obtener el binario

    if numero >=0:
        #Revisamos si nuestro numero es igual a cero, entonces nos regresa al cero como binario
        if numero ==0:
            return "0"
        #Si nuestro numero es igual a 1, entonces nos regresa al 1 como su numero binario
        if numero == 1:
            return "1"
        #Si el numero es mayor a cero, vamos a crear una nueva variable que sea el resultado 
        #de la division entera de dos para despues ocuparla en la iteracion
        if numero >0:
            
            numero1 = numero//2
            #Nos regresa el str del residuo de la division de numero entre 2
            #este nos va a dar un valor 0 o 1, despues le vamos a sumar otra cadena
            #que se obtiene de hacer el llamado recursivo, evaluamos a la funcion en
            #el valor anteriormente definido
            return str(deci_bina(numero1))+ str(numero % 2) 
    #Si nuestro numero decimal es negativo no se obtiene el binario                
    else:
        print("El numero es negativo")
#Hacemos nuestra funcion main donde se le pide el numero al usuario y este se ingresa en la
#funcion deci_bina que nos muestra el numero binario
def main2():
    numero = int(input("Escribe un numero decimal"))
    print(deci_bina(numero))
#Llamamos a la funcion main2()
main2()
"""Complicaiones:
No hubo muchos problemas, pues el ejercicio nos decia lo que debiamos hacer, por lo
que me parecio un poco mas facil de realizar"""
#%%Ejercicio 168: Raíz cuadrada recursiva(20 líneas)
"""El ejercicio 71 exploró cómo se puede utilizar la iteración para calcular la raíz 
cuadrada de un número.
En ese ejercicio se generaba una mejor aproximación de la raíz cuadrada con cada 
iteración adicional de un bucle. 
En este ejercicio usarás la misma estrategia de aproximación, pero utilizarás la 
recursión en lugar de la iteración.
Crea una función de raíz cuadrada que tome dos parámetros. El primer parámetro, n, 
será el número para el que se calcula la raíz cuadrada. El segundo parámetro, guess, 
será la estimación actual de la raíz cuadrada. El parámetro guess debe tener un valor
por defecto de 1.0.
No proporcione un valor por defecto para el primer parámetro. Su función de raíz 
cuadrada será recursiva. El caso base ocurre cuando guess^2 está dentro de 10^-12
En este caso su función debería devolver guess porque está lo suficientemente cerca 
de la raíz cuadrada de n. En caso contrario, tu función debería devolver el resultado 
de llamarse a sí misma recursivamente con n como primer parámetro y ....
como segundo parámetro.
Escribe un programa principal que demuestre tu función de raíz cuadrada calculando 
la raíz cuadrada de varios valores diferentes. Cuando llames a tu función de raíz 
cuadrada desde el programa principal sólo debes pasarle un parámetro para que se 
utilice el valor por defecto de valor por defecto de la conjetura.
Traducción realizada con la versión gratuita del traductor www.DeepL.com/Translator"""

def raiz(n, guess=1):
    """
    Muestra la raiz de un numero

    Parameters
    ----------
    numero :type int:
        numero entero
    

    Returns
    -------
    None.
    """
    #Vemos si guess^2 está dentro de 10^-12 regresamos guess porque está lo 
    #suficientemente cerca de la raíz cuadrada de n
    if n-(10**(-12)) <= guess*guess <=n+(10**(-12)):
        return guess
    #Si no esta, llamaremos a la funcion raiz con n como primer parametro y 
    #guess+ n/guess)/2 como segundo parametro para que nos de la aproximacion de la raiz
    else:
        return raiz(n, (guess+ n/guess)/2)
    

def main3():
    n= int(input("Escribe un numero pasa sacarle la raiz cuadrada"))
    print(raiz(n, guess=1))
main3()

"""Complicaciones:
Tuve problemas para implementar que guess*guess estuviera dentro del parametro 10**(-12)
pero todo se soluciono cuando pude acortar a guess por ambos lados para que estuviera dentro de
este parametro"""

#%%Ejercicio 170: Cambio posible (41 Líneas)
"""
Crea un programa que determine si es posible o no construir un determinado total 
utilizando un número específico de monedas. Por ejemplo, es posible tener un total 
de $1.00 usando cuatro monedas si todas son de 25 centavos. Sin embargo, no es posible 
tener un total de $1.00 usando 5 monedas. Sin embargo, es posible tener $1.00 usando 
6 monedas si se usan 3 monedas de 25 centavos, 2 de 10 centavos y una de 5 centavos. 
Del mismo modo, se puede obtener un total de 1,25 $ con 5 monedas u 8 monedas, pero 
un total de $1.25 no puede formarse usando 4, 6 o 7 monedas.
Su programa debe leer tanto la cantidad de dólares como el número de monedas del usuario.
Debe mostrar un mensaje claro que indique si el importe en dólares introducido puede
formarse con el número de monedas indicado. 
Asuma la existencia de monedas de 25 centavos, 10 centavos, 5 centavos y 5 centavos 
al completar este problema. Su solución debe utilizar la recursividad. No puede 
contener ningún bucle."""

def cambio(monto, monedas):
    """
    Muestra los montos y cuantas modenas se ocuparan para dar cambio

    Parameters
    ----------
    monto: type float:
        Cantidad de dinero que debemos de dar cambio
    monedas: type int:
        cuantas monedas queremos regresar de cambio
    
    Returns
    -------
    None.
    """
    #Revisamos que si el monto es menor que 0 y que se ingresan 0 monedas, entonces
    #nos regresara un False
    if monto<0 or monedas==0:
        return False
    #Revisamos que si el monto se puede completar con monedas de 0.01, regresamos 
    #cuantas monedas se ocupan para completar el monto
    if monedas*0.01 == monto:
        print("Se puede obtener el monto utilizando monedas de 0.01")
    #Revisamos que si el monto se puede completar con monedas de 0.05, regresamos 
    #cuantas monedas se ocupan para completar el monto
    if monedas*0.05 == monto:
        print("Se puede obtener el monto tilizando monedas de 0.05")
    #Revisamos que si el monto se puede completar con monedas de 0.10, regresamos 
    #cuantas monedas se ocupan para completar el monto
    if monedas*0.10 == monto:
        print("Se puede obtener el monto utilizando monedas de 0.10")
    #Revisamos que si el monto se puede completar con monedas de 0.25, regresamos 
    #cuantas monedas se ocupan para completar el monto   
    if monedas*0.25 == monto:
        print("Se puede obtener el monto utilizando monedas de 0.25")
    #Si no se puede completar el monto con mondeas iguales, llamaremos a la 
    #funcion cambio para obtener de forma distribuida el cambio 
    else:
        return (cambio(monto-0.01, monedas-1) or
                cambio(monto-0.05, monedas-1) or
                cambio(monto-0.10, monedas-1) or
                cambio(monto-0.25, monedas-1))
#Definimos la funcion main5() que pide el monto y el numero de monedas, para despues
#llamar a la funcio cambio
def main4():
    monto = float(input("Escribe los dolares"))
    monedas = int(input("Escribe las monedas en que se podria dividir"))
    print(cambio(monto, monedas))
#Llamos a la funcion main5()
main4()
"""Complicaciones:
Tuve un poco de problemas al realizar la funcion recursiva, es decir el como
poner que se diera el cambio con monedas distintas"""
    
#%%Ejercicio 171: Ortografía con símbolos de elementos (68 líneas)
"""Cada elemento químico tiene un símbolo estándar de una, dos o tres letras.
Un juego al que algunas personas gustan de jugar es determinar si una palabra puede 
deletrearse utilizando sólo los símbolos de los elementos. Por ejemplo, el silicon 
puede deletrearse utilizando los símbolos Si, Li, C, O y N. Sin embargo, el hidrógeno
no puede deletrearse con ninguna combinación de símbolos de elementos.
Escribe una función recursiva que determine si una palabra puede escribirse utilizando
sólo símbolos de elementos. Tu función tomará dos parámetros: la palabra que se intenta
deletrear y una lista de los símbolos que se pueden utilizar. Su función devolverá dos
resultados: un valor booleano que indica si se ha encontrado o no una grafía, y la 
cadena de símbolos utilizada para conseguir la grafía (o una cadena vacía si no existe 
ninguna grafía). Su función debe ignorar las mayúsculas cuando busque una ortografía.
Cree un programa que utilice su función para encontrar y mostrar todos los nombres 
de elementos que puedan deletrearse utilizando sólo los símbolos de los elementos. 
Muestre los nombres de los elementos junto con las secuencias de símbolos.Por ejemplo,
una línea de su salida será:   
    Silver can be spelled as SiLvEr
Su programa utilizará el conjunto de datos de elementos, que puede descargarse del 
sitio web del autor. Este conjunto de datos incluye los nombres y símbolos de los 118 
elementos químicos elementos químicos"""
#Escribimos el diccionario con los elementos de la tabla periodica
simboloss ={
    "H" : "Hydrogen", "He": "Helium", "Li": "Lithium", "Be": "Beryllium",
    "B" : "Boron", "C": "Carbon", "N": "Nitrogen", "O": "Oxygen",
    "F" : "Fluorine", "Ne": "Neon", "Na": "Sodium", "Mg": "Magnesium",
    "Al": "Aluminium", "Si": "Silicon", "P": "Phosphorus", "S": "Sulfur",
    "Cl": "Chlorine", "Ar": "Argon", "K": "Potassium", "Ca": "Calcium",
    "Sc": "Scandium", "Ti": "Titanium", "V": "Vanadium", "Cr": "Chromium",
    "Mn": "Manganese", "Fe": "Iron", "Co": "Cobalt", "Ni": "Nickel",
    "Cu": "Copper", "Zn": "Zinc", "Ga": "Gallium", "Ge": "Germanium",
    "As": "Arsenic", "Se": "Selenium", "Br": "Bromine", "Kr": "Krypton",
    "Rb": "Rubidium", "Sr": "Strontium", "Y": "Yttrium", "Zr": "Zirconium",
    "Nb": "Niobium", "Mo": "Molybdenum", "Tc": "Technetium", "Ru": "Ruthenium",
    "Rh": "Rhodium", "Pd": "Palladium", "Ag": "Silver", "Cd": "Cadmium",
    "In": "Indium", "Sn": "Tin", "Sb": "Antimony", "Te": "Tellurium",
    "I" : "Iodine", "Xe": "Xenon", "Cs": "Caesium", "Ba": "Barium",
    "La": "Lanthanum", "Ce": "Cerium", "Pr": "Praseodymium", "Nd": "Neodymium",
    "Pm": "Promethium", "Sm": "Samarium", "Eu": "Europium", "Gd": "Gadolinium",
    "Tb": "Terbium", "Dy": "Dysprosium", "Ho": "Holmium", "Er": "Erbium",
    "Tm": "Thulium", "Yb": "Ytterbium", "Lu": "Lutetium", "Hf": "Hafnium",
    "Ta": "Tantalum", "W": "Tungsten", "Re": "Rhenium", "Os": "Osmium",
    "Ir": "Iridium", "Pt": "Platinum", "Au": "Gold", "Hg": "Mercury",
    "Tl": "Thallium", "Pb": "Lead", "Bi": "Bismuth", "Po": "Polonium",
    "At": "Astatine", "Rn": "Radon", "Fr": "Francium", "Ra": "Radium",
    "Ac": "Actinium", "Th": "Thorium", "Pa": "Protactinium", "U": "Uranium",
    "Np": "Neptunium", "Pu": "Plutonium", "Am": "Americium", "Cm": "Curium",
    "Bk": "Berkelium", "Cf": "Californium", "Es": "Einsteinium",
    "Fm": "Fermium", "Md": "Mendelevium", "No": "Nobelium", "Lr": "Lawrencium",
    "Rf": "Rutherfordium", "Db": "Dubnium", "Sg": "Seaborgium", "Bh": "Bohrium",
    "Hs": "Hassium", "Mt": "Meitnerium", "Ds": "Darmstadtium", "Rg": "Roentgenium",
    "Cn": "Copernicium", "Uut": "Ununtrium", "Fl": "Flerovium", "Uup": "Ununpentium",
    "Lv": "Livermorium", "Uus": "Ununseptium", "Uuo": "ununoctium"
    } 

def palabra_ele(palabra, simbolos, i=0, palabra_simbolos=''):
    """ 
    Parameters
    ----------
    palabra : Type str
        Palabra que ingresa el usuario
    simbolos : Type Lista
        Lista con simbolos de la tabla periodica
    i : TYPE, optional
        DESCRIPTION. The default is 0.
    palabra_en_simbolos : TYPE, optional
        DESCRIPTION. The default is ''.

    Returns
    -------
    TYPE
        DESCRIPTION.
    """
    #A los caracteres de la cadena los convertimos a minusculas
    palabra=palabra.lower()
    #Revisamos cada letra, al capitalizar se pasa a formato en que la 
    #primera letra sea mayuscula
    #si la letra es uno de los simbolos
    #se agrega a la cadena palabra_simbolos='' 
    if palabra[i].capitalize() in simbolos: 
        palabra_simbolos += palabra[i].capitalize()
        #Aumentamos el indice en una unidad para pasar a la siguiente letra
        i+=1
        #Cuando se pasan todas las letras y en mayusculas aparecen en 
        #simbolos nos regresa la cadena palabra simbolos
        if i == len(palabra):
            return palabra_simbolos
        #Si todos no estan llamamos a la funcion palabra_ele
        else: 
            return palabra_ele(palabra, simbolos, i, palabra_simbolos)
    #Si la letra no es uno de los simbolos entonces se trabaja con la letra y 
    #la letra del indice siguiente esto debido a que los simbolos de los elementos
    #tienen maximo 2 letras
    elif (palabra[i]+palabra[i+1]).capitalize() in simbolos: 
        palabra_simbolos += (palabra[i]+palabra[i+1]).capitalize()
        i+=2
        if i==len(palabra): 
            return palabra_simbolos
        else: 
            return palabra_ele(palabra, simbolos, i, palabra_simbolos)
    #Cuando ninguno de esto pasos se cumple entonces la palabra no se puede escribir
    #con simbolos quimicos    
    else: 
        print("No se puede deletrear con simbolos de elementos quimicos")
#Creamos la funcion main4() donde se pide al usuario una palabra que se ingresara 
#en la funcion palabra_ele
def main5():
    palabra=input("Escriba la letra que quiere que se ponga en simbolos")
    simbolos = simboloss.keys()
    print(palabra_ele(palabra, simbolos, i=0, palabra_simbolos=''))
#Llamamos la funcion main5()
main5()

"""Complicaciones:
Tuve un poco de problemas al hacer que se recorriera el programa en todas las
letras de la palabra"""
    
#%%Ejercicio 173: Decodificación de longitudes de carrera(33 Líneas)
"""La codificación de longitud de carrera es una técnica simple de compresión de datos
que puede ser efectiva cuando se repiten valores en posiciones adyacentes dentro de 
una lista. La compresión se consigue sustituyendo los grupos de valores repetidos por 
una copia del valor, seguida por el número de veces que debe repetirse el valor. 
Por ejemplo, la lista ["A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "B",
                      "B", "B", "B", "A", "A", "A", "A", "A", "B"] se comprimiría 
como ["A", 12, "B", 4, "A", 6, "B", 1]. La descompresión se lleva a cabo replicando
cada valor de la lista el número de veces indicado.
Escriba una función recursiva que descomprima una lista codificada en longitud de 
recorrido. Su función recursiva tomará como único parámetro una lista comprimida a
lo largo de la carrera. Devolverá devolverá la lista descomprimida como único resultado.
Cree un programa principal que muestre una lista codificada de longitud de ejecución 
y el resultado de la decodificación."""

def descomprimir(codificado, descomprimida=[], i=0):
    """
    Descomprime una lista mostrando las repeticiones de la letra las veces
    que indica el número de su derecha y genera la lista descodificada.

    Parameters
    ----------
    codificado : Lista
        Lista con números dentro de la cadena
    descomprimida : TYPE, Lista
        DESCRIPTION. The default is []. Genera la lista con repeticiones
    i : TYPE, optional
        DESCRIPTION. The default is 0.

    Returns
    -------
    None.

    """
    #Tomamos el indice 0, que es una letra
    letra = codificado[i]
    #Tomamos la cantidad de veces que se repite esa letra que se encuentre en el 
    #siguiente indice de la lista
    repeticion = codificado[i+1]
    #
    for n in range(repeticion): 
        descomprimida.append(letra)
    #Aumentamos dos unidades el indice para que pase a la segunda letra
    i += 2
    #Si el indice es menor que la longitud de la lista con las cantidades de repeticion
    #de las letras
    if i < len(codificado):
        descomprimir(codificado, descomprimida, i)
    #Si pasa el caso contrario se imprime la lista descomprimida
    else: 
        print(descomprimida) 
#Creamos nuestra lista comprimida para descomprimirla
prueba = ["A",3,"B",5,"C",6]
#Llamamos nuestra funcion descomprimir con la lista comprimida como entrada
print(descomprimir(prueba))
"""Complicaciones:
Tuve un poco de problemas parecidos al ejercicio anterior pues no recordaba como repetir 
el proceso para la siguiente letra, pero revisando el ejercicio anterior, todo se 
soluciono"""





      
        
        
        
        
        
        
        
        
        
        
        
    
    
