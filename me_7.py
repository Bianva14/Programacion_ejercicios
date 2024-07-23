# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 14:00:28 2022

@author: pc1
"""

#%%Ejercicio 145:Encuentra la palabra más larga en un archivo
"""En este ejercicio, creará un programa de Python que identifique la(s) palabra(s) más 
larga(s) en un archivo.
Su programa debe generar un mensaje apropiado que incluya la longitud de la palabra más 
larga, junto con todas las palabras de esa longitud que se produjeron en el archivo.
Trate cualquier grupo de caracteres que no sean espacios en blanco como una palabra, 
incluso si incluye números o signos de puntuación."""
#Me falta poner a todas las palabras con esa misma longitud de larga solo me aparece una
def palabra_mas_largas(archivo):
    try:        
        with open(archivo, 'r') as f:
            contenido = f.readline()
            
            palabras = contenido.split()
            
            print('Cantidad de palabras:', len(palabras))
            
            indice = 0 
            palabra = palabras[indice]
            longitud = len(palabra)
            
            for i in range(1, len(palabras)):
                if len(palabras[i]) > longitud:
                    indice = i
                    palabra = palabras[i]
                    longitud = len(palabra)
            return palabra, indice           
    except FileNotFoundError as e:
        print('El archivo especificado no existe.')
        
archivo = input("Escriba la direccion del archivo")        
#archivo = 'C:\Users\pc1\.spyder-py3\autosave\example.txt'
resultado = palabra_mas_largas(archivo)
print(resultado)

    
#%%Ejercicio 146:Frecuencias de letras
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
archivo = input("Escribe la direcion")
with open(archivoo, 'r') as f_in:
    lines = list(line for line in (l.strip() for l in f_in) if line)
    texto = "".join(lines)
    print(texto)

def Frecuencia(archivoo):
    try:
        with open(archivoo, 'r') as f_in:
            lines = list(line for line in (l.strip() for l in f_in) if line)
            texto = "".join(lines)
            print(texto)
            conteo = {}
            texto_sin = texto.replace(" ","") 
            for letra in texto_sin.lower():
                if letra not in conteo:
                    conteo[letra]=1
                else:
                    conteo[letra] +=1
            print(conteo)
            #for k, v in conteo.items():
                #x ="{}: {}".format(k,v)
            #print(x)
    except FileNotFoundError as e:
        print('El archivo especificado no existe.')
archivoo = input("Escribe la direccion del archivo")
print(Frecuencia(archivoo))         



file = open ("C:\Users\pc1\.spyder-py3\autosave\example.txt", "r")
lines=file.readlines()[1:]
file.close()

#Este programa se enfoca en descifrar un mensaje que ha sido codificado usando un 
#cifrado de Cesar.
#En primer lugra se hizo un recuento del texto cifrado para posteriormente conocer 
#la letra que es
#mas frecuente y con esto obtener el desplazamiento con una tecnica ocupada hace mil años. Ademas de que
#ocupamos una funcion para identificar las mayusculas y minusculas, y por ultimo 
#decodificamos cada
#carácter del texto cifrado e imprimimos el resultado

#Nombre de los integrantes y números de cuenta:

#Lucía Sosa Méndez 317522026
#Bianca Ramírez Mejía 421117321
#Natalia Javlyn Solorio Hérnandez 318094067

#Número de equipo: 22
 

#Pasamos el texto cifrado sin espacios
texto_cifrado = "vikpew hi pe zmhe pe zmhe rs iw nywxe egswxyqfvexi e ipps Ep qyrhs rs pi mqtsvxe xy eyxsiwxmqe ip qyrhs iwtiveve uyi pskviw epks erxiw hi uyi xi wmirxew fmir gsrxmks qmwqs Rs kerevew qygls hmrivs nywxs hiwtyiw hi lefiv wepmhs hi pe yrmzivwmheh c rs wivew zmgitviwmhirxi lewxe uyi gsr xy iwjyivds xi lecew kerehs eqfsw Wm tmirwew uyi xy qeiwxvs iw hyvs iwtive lewxe uyi xirkew yr niji iwi wm uyi rs xirhve zsgegmsr hi irwirerde rm pe tegmirgme viuyivmhe Hihmgevwi e jvimv leqfyvkyiwew rs xi uymxe hmkrmheh xyw efyipsw xirmer yre tepefve hmjivirxi teve hiwgvmfmvps ps ppeqefer stsvxyrmheh Wm qixiw pe texe rs iw gypte hi xyw tehviw ewm uyi rs xi peqirxiw tsv xyw ivvsviw c etvirhi hi ippsw Erxiw hi uyi regmivew xyw tehviw rs iver xer efyvvmhsw gsqs ps wsr elsve ippsw iqtidevsr e wivps ep tekev xyw gyirxew pmqtmev xy vste c iwgyglevxi lefpev egivge hi xyw tvsfpiqew ewm uyi mrmgme ip geqmrs pmqtmerhs pew gswew hi xy tvstme zmhe iqtiderhs tsv xy lefmxegmsr Ir ip gspikms tyihi lefivwi ipmqmrehs pe hmjivirgme irxvi kerehsviw c tivhihsviw tivs ir pe zmhe viep rs Pe zmhe rs wi hmzmhi ir wiqiwxviw rs xirhvew zegegmsriw hi zivers pevkew ir pykeviw pinersw c qyc tsgsw nijiw wi mrxiviwever ir ecyhevxi e uyi xi irgyirxviw e xm qmwqs xshs iwxs xirhvew uyi legivps ir xy xmiqts pmfvi Pe xipizmwmsr rs iw pe zmhe hmevme ir pe zmhe gsxmhmere pe kirxi hi zivheh xmiri uyi wepmv hip geji hi pe tipmgype teve mv e xvefenev Wi eqefpi gsr psw rivhw ibmwxir qyglew tswmfmpmhehiw hi uyi xivqmriw xvefenerhs teve yrs hi ippsw Epkyrew jvewiw qsxmzegmsrepiw Rs rigiwmxeqsw qekme teve geqfmev ip qyrhs tsvuyi ce xiriqsw xshs ip tshiv uyi rigiwmxeqsw ir ryiwxvs mrxivmsv pe getegmheh hi mqekmrev yr qyrhs qinsv Lsc gyerhs qmvs legme exvew tyihs ejmvqev uyi rs geqfmevme rehe tivhiv xshs jyi jyrheqirxep teve qm tsvuyi qi qswxvs uyi ps qew mqtsvxerxi iw wiv wmrgivs gsr yrs qmwqs c jyi ps uyi tvigmweqirxi qi gsrhyns lewxe euym rs zmzs gsr xiqsv wsc pmfvi rs xirks wigvixsw c wi uyi wmiqtvi iwxevi fmir tsvuyi wmr mqtsvxev ps uyi tewi, wi uymir wsc Rs hiniw uyi rehmi xi hmke uyi rs tyihiw legiv epks wm xmiriw yr mhiep xmiriw uyi tvsxikivps Gyerhs rs tyihir legiv epks e pew tivwsrew piw kywxe higmvpiw e psw hiqew uyi xeqtsgs tshver legivps Wm uymiviw epks zi c fywgeps gehe ibtivmqirxs jeppmhs xi egivge yr tews qew ep ibmxs Ir ip qyrhs rs xshs iw epikvme c jipmgmheh ip qyrhs iw yr pykev gvyip c qepmgmsws c rs mqtsvxe ps jyivxi uyi wiew xi hivvsxeve xi tsrhve hi vshmppew c xi qerxirhve ewm ir xerxs xy ps tivqmxew Rehmi xi ksptieve xer hyvs gsqs pe zmhe tivs rs wi xvexe hi pe jyivde gsr pe uyi ksptiiw wi xvexe hi pe jyivde gsr pe uyi pe zmhe xi ksptii c xy wmkew ezerderhs Gyerxs tyihiw wstsvxev c wikymv ehiperxi ewm iw gsqs wi kere Rs tyihiw hinev uyi ip qmihs ep jvegews e pew gsqtevegmsriw s e pew gvmxmgew xi mqtmhe legiv xshs euyipps uyi xi tivqmxmve hiwxegevxi Rs tyihiw xvmyrjev wmr ip vmiwks hi jvegewev Rs tyihiw xiriv yre zsd tvstme wmr ip vmiwks hi wiv gvmxmgehs Rs tyihiw eqev wmr ip vmiwks hi tivhiv hifiw gsvviv iwxsw vmiwksw"

plain_text = ""
#Para ver cuál es la letra más común hacemos un recuento de las primeras seis letras más comunes en el español para ver cuales eran las más repetidas en el texto cifrado
#print(texto_cifrado.count('a')):hubieron 0
#print(texto_cifrado.count('o')):hubieron 0
#print(texto_cifrado.count('r')): hubieron 154

print("\n El número total de letras es de: ", len(texto_cifrado)-texto_cifrado.count(' '))#Al total de caracteres le restamos el total de espacios
print("\n El recuento de la letra e en el texto cifrado es de:  ",texto_cifrado.count('e'))
print("\n El recuento de la letra i en el texto cifrado es de:  ",texto_cifrado.count('i')) #La i es el 14.2% de todo el texto cifrado
print("\n El recuento de la letra s en el texto cifrado es de:  ",texto_cifrado.count('s'))

print("\n Por lo tanto la letra más común en el texto cifrado es la i")
shift = ord('i')- ord('e') #Le restamos la letra más común del texto a la letra más común que generalmente es la e 

ord('e')-ord('a') #Hacemos una prueba con la seunda letra más común que es la e para checar si el desplazamiento es el mismo 

print('\n El desplazamiento es = ', shift)

#Usamos la función for para hacer las condiciones en caso de si la letra es minúscula o mayúscula 
for c in texto_cifrado:

    #checamos si las letras son minúsculas
    if c.islower():

        #encontramos el número de posición que va del 0-25
        c_unicode = ord(c)
        c_index = ord(c) - ord("a")

        #Se hace el desplazamiento negativo
        new_index = (c_index - shift) % 26

        #Convertimos a un nuevo caracter 
        new_unicode = new_index + ord("a")
        new_character = chr(new_unicode)

        #Hacemos una cadena 
        plain_text = plain_text + new_character

    #Repetimos el procedimiento anterior pero con las letras mayúsculas 
    elif c.isupper():
         c_unicode = ord(c)
         c_index = ord(c) - ord("A")
         new_index = (c_index - shift) % 26
         new_unicode = new_index + ord("A")
         new_character = chr(new_unicode)
         plain_text = plain_text + new_character 

    else:
        plain_text += c

#Imprimimos el texto antes y después de ser decifrado 
print("\n Texto cifrado:",texto_cifrado) 

print("\n Texto decifrado:",plain_text)

#%%Ejercicio 147:Words that Occur Most
"""Escriba un programa que muestre la palabra (o palabras) que ocurren con mayor 
frecuencia en un archivo. Su programa debe comenzar leyendo el nombre del archivo 
del usuario. Luego, debe encontrar la(s) palabra(s) dividiendo cada línea en el 
archivo en cada espacio.
Finalmente, cualquier signo de puntuación inicial o final debe eliminarse de cada
palabra. Además, su programa debe ignorar las mayúsculas. Como resultado, aplee,
manzana!,Apple y ApPle deben tratarse como la misma palabra. Probablemente encontrará
útil su solución al Ejercicio 111 cuando complete este problema."""
def Ocurrir(archivooo):
    try:        
        with open(archivo, 'r') as f:
            contenido = f.readline()
            
            palabras = contenido.split()
            
            contador = {}
            for palabra in palabras:
                if palabra in contador:
                    contador[palabra] += 1
                else:
                    contador[palabra] = 1
            #contador = sorted(contador.items(), key = lambda item: item[1])
            #return contador[-2]
            print(contador)
            for t in contador.:
                if t 
            for valor in contador:
                if valor = 
    except FileNotFoundError as e:
        print('El archivo especificado no existe.') 
               
archivooo = input("Escribe la direccion del archivo")
Ocurrir(archivooo)
#%%Ejercicio 149:Calificaciones de letras y puntos de calificación
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
def cambiaraLetras(puntoscalificacion):
    puntoscalificacion = input("Escribe una cadena"\n)
    if puntoscalificacion = " ":
        break
cambiaraLetras(puntoscalificacion)



