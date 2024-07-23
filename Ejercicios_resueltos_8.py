# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 16:32:43 2022

@author: pc1
"""

#%%Ejercicio 164:Total de los valores
"""
@autor: Bianca Ramirez Mejia  no.cuenta:421117321
Ejercicio 164:Total de los valores
Descripcion del ejercicio:
Escriba un programa que lea los valores del usuario hasta que se ingrese una línea en blanco.
Muestra el total de todos los valores ingresados por el usuario (o 0.0 si el primer valor 
ingresado es una línea en blanco). Complete esta tarea usando la recursividad. Es posible
que su programa no utilice bucles.

Sugerencia: el cuerpo de su función recursiva necesitará leer un valor del usuario y luego 
determinar si debe o no realizar una llamada recursiva. Su función no necesita tomar ningún 
parámetro, pero deberá devolver un resultado numérico.
"""
from mer_8 import main1
if __name__ =="__main__":
    main1()
"""No hubo complicacion alguna,estuvo muy bien explicado"""

#%%Ejercicio 167: Palindromo
"""
@autor: Bianca Ramirez Mejia no.cuenta:421117321
Ejercicio 167: Palíndromo recursivo
Descripcion del ejercicio:
La noción de palíndromo se introdujo previamente en el ejercicio 72. En este ejercicio 
escribirás una función recursiva que determina si una cuerda es un palíndromo o no. 
La cadena vacía es un palíndromo, al igual que cualquier cadena que contenga solo un 
carácter. Cualquier cadena más larga es un palíndromo si su primer y último carácter 
coinciden, y si la cadena formada al eliminar el primer y último carácter también es 
un palíndromo.
Escriba un programa principal que lea una cadena del usuario. Utilice su función
recursiva para determinar si la cadena es un palíndromo o no. Luego muestre un mensaje 
apropiado para el usuario.
Escriba una función recursiva que calcule la distancia de edición entre dos cadenas.
Utilice el siguiente algoritmo:
    Sean s y t las cadenas
    Si la longitud de s es 0
      Return la longitud de t
    Else if si la longitud de t es 0 entonces
      Return la longitud de s
    Else
      Establecer el costo en 0
      If el ultimo caracter en s no es igual al ultimo caracter en t entonces 
         Establecer el costo en 1
      Establecer d1 igual a la distancia de edicion entre todos los caracteres excepto 
      la ultima en s, y todos los caracteres en t, mas 1
      Establecer d2 igual a la distancia de edicion entre todos los caracteres en s y 
      todos los caracteres excepto el ultimo en t, mas 1
      Establecer d3 igual a la distancia de edicion entre todos los caracteres excepto
      el ultimo en s, y todos los caracteres excepto el ultimo en t, mas costo
    Return el minimo de d1,d2 y d3
"""
from mer_8 import main
if __name__ =="__main__":
    main()
"""Solo tuve algunas complicaciones en entender a que se referia con palindromo, y en la
traduccion pero me sirvio mucho buscar algunas palabras en solitario para entender el sentido
de la traduccion"""
#%%Ejercicio 169:Distancia de edicion entre dos cadenas
"""
@autor: Bianca Ramirez Mejia no.cuenta:421117321
Ejercicio 169: Distancia de edicion de cadena
Descripcion del ejercicio:
La distancia de edición entre dos cadenas es una medida de su similitud: cuanto menor es 
la distancia de edición, más similares son las cadenas con respecto al número mínimo de 
operaciones de inserción, eliminación y sustitución necesarias para transformar una cadena
en la otra.
Piense en las cadenas kitten and sitting. La primera cadena se puede transformar en 
la segunda cadena con las siguientes operaciones: Sustituya la k por una s, sustituya la 
e por una i e inserte una g al final de la cadena. Este es el menor número de operaciones
que se pueden realizar para transformar a un gatito en un asiento.
Como resultado, la distancia de edición es 3.
"""
from mer_8 import main2
if __name__="__main__":
    main2()
    
"""La unica complicacion que tuve en este problema fue comprender a lo que se referia 
a distancia de edicion, y un poco en la traduccion pero igualmente busque las palabras
para poder entender el sentido de la traduccion"""

#%% 
"""
@autor: Flores Cruz Daniela 318099567

Ejercicio 172: Secuencias de elementos
(Resuelto-83 líneas)

Otro juego al que juegan algunas personas con los nombres de los elementos químicos
consiste en construir una secuencia de elementos en la que cada elemento de la
secuencia comienza con la última letra de su predecesor. Por ejemplo, si una
secuencia empieza por Hidrógeno, el siguiente elemento debe ser un elemento que
empiece por N, como el Níquel. El elemento que sigue al Níquel debe empezar por L,
como el Litio. La secuencia de elementos que se construye no puede contener ningún duplicado.

Escriba un programa que lea el nombre de un elemento del usuario. Su programa
debe utilizar una función recursiva para encontrar la secuencia más larga de
elementos que comienza con el elemento introducido. Luego debe mostrar la secuencia.
Asegúrese de que su programa responda de forma razonable si el usuario no introduce 
un nombre de elemento válido.

Sugerencia: Su programa puede tardar hasta dos minutos en encontrar la secuencia
más larga para algunos elementos. Como resultado, usted podría querer usar elementos
como el Molibdeno y el Magnesio como sus primeros casos de prueba. Cada uno tiene una
secuencia más larga de sólo 8 elementos que su programa debería encontrar en una
fracción de segundo.
"""
from mer_8 import principal
principal()

"""
Para el llamado de esta función no tuve problemas, pues simplemente es llamar 
a nuestra función principal la cual ya pide el elemento y hace uso de las 
funciones que nos permiten hacer el ejercicio.
"""
#%%
"""
@autor: Flores Cruz Daniela 318099567

Ejercicio 174: Codificación de longitud de ejecución
(Resuelto-36 Líneas)

Escriba una función recursiva que implemente la técnica de compresión de longitud
de carrera descrita en el Ejercicio 173. Su función tomará una lista o una cadena
como único parámetro. Deberá devolver la lista comprimida de longitud de ejecución
como único resultado. Incluya un programa principal que lea una cadena del usuario,
la comprima y muestre el resultado codificado en longitud de recorrido.

Sugerencia: Puede incluir un bucle dentro del cuerpo de su función recursiva.
"""

from mer_8 import main4
main4()

"""
Para el llamado de esta función no tuve prblemas
"""