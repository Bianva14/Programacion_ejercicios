# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 18:36:34 2022

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
import sys
sys.path.append(r'C:/Users/pc1/Documents/programacion-2021-2/fc/matematicas')

from me_8 import main1
if __name__ == "__main__":
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
from me_8 import main2
if __name__ == "__main__":
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
from me_8 import main3
if __name__ == "__main__":
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
from me_8 import main4
if __name__ == "__main__":
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
from me_8 import main5
main5()
if __name__ == "__main__":
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
