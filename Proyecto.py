"""
Título de proyecto : Cocina Inteligente.
Autor              : Natalia Suárez Olmos.
Matrícula          : A01707445.
python_version     : 3.7.7
"""

import time
"""Esta función hace que la consola imprima después de un cierto
tiempo dado. El número que se inserta en la función está dado en segundos,
puede ser en números enteros o flotantes."""

"""
Tiempo de consumo de diversos alimentos
"""
print ("Consumo preferente de tus alimentos")
print ("Tipos de alimentos: verduras y frutas(1), lacteos(2)")
print ("embutido(3), carne fresca(4), huevo(5)")
print ("Por favor pon el número correspondiente de tu alimento")
alimento = int(input())
if alimento == 1:
    print ("Verdura y fruta:","","Consumir dentro de una semana.")
if alimento == 2:
    print ("Lácteo:","","Consumir en 5 días")
if alimento == 3:
    print ("Embutido:","","Consumir dentro de una semana")
if alimento == 4:
    print ("Carne fresca:","","Consumir en 4 días")
if alimento == 5:
    print ("Huevo:","","Consumir en 1 mes")

"""
Conteo de los alimentos
"""
print ("")
print ("Conteo de los alimentos")
print ("")
print ("Coloca tu numero de alimentos en general:")

print ("Verduras y frutas:")
var_1= int(input())
print ("")

print ("Lácteos:")
var_2= int(input())
print ("")

print ("Embutido:")
var_3=int(input())
print ("")

print("Carne fresca:")
var_4= int(input())
print ("")

print("Huevos:")
var_5=int(input())
print ("")

total_de_alimentos= var_1 + var_2 + var_3 + var_4 + var_5
print ("Total de alimentos:",total_de_alimentos)
print ("")
print ("Indica si tomaste un alimento después del registro")
print ("Responde con sí o no")

a = input()
if a == "sí":
    print ("Indica la cantidad")
    var_6= int(input())
    total_alternativo= total_de_alimentos - var_6
    print ("Nuevo total:", total_alternativo)
    print ("""Especifica de cuál tomaste, tus opciones son:
verduras y frutas, lácteos, huevo, embutidos y carne fresca""")
    var_7=  str(input())
    print ("Indica que cantidad tomaste del alimento")
    var_8= int(input())
    if var_7 == "Verduras y frutas":
        print ("Nueva cantidad de verduras y frutas:")
        var_1 = var_1 - var_8
        print (var_1)
    if var_7 == "Lácteos":
        print ("Nueva cantidad de lacteos:")
        var_2 = var_2 - var_8
        print (var_2)
    if var_7 == "Embutidos":
        print ("Nueva cantidad de embutidos:")
        var_3 = var_3 - var_8
        print (var_3)
    if var_7 == "Carne fresca":
        print ("Nueva cantidad de carne fresca:")
        var_4 = var_4 - var_8
        print (var_4)
    if var_7 == "Huevo":
        print ("Nueva cantidad de huevo:")
        var_5 = var_5 - var_8
        print (var_5)
else:
    print ("Ok")
print ("")
print ("""Ahora te indicaremos si es posible realizar las opciones
de comidas que tenemos para ti""")

print ("Indica el número de los diferentes alimentos")
print (" Anteriormente indicaste la cantidad de huevo")
print (" Pon la cantidad de jitomates:")
jitomate = int(input())
print ("")
print (" Pon la cantidad de pepino:")
pepino = int(input())
print ("")
print (" Pon la cantidad de lechuga:")
lechuga = int(input())
print ("")
print (" Pon la cantidad de yogurt:")
yogurt = int(input())
print ("")
print (" Pon la cantidad de manzanas:")
manzana = int(input())
print ("")
print (" Pon la cantidad de jamón:")
jamon = int(input())
print ("")
print (" Pon la cantidad de pollo:")
pollo = int(input())
print ("")
print (" Pon la cantidad de res:")
res = int(input())
print ("")
print (" Pon la cantidad de repollo:")
repollo = int(input())
print ("")

"""
Opciones de comida
"""
def ensalada(pepino,lechuga,jitomate):
    #Devueleve si es posible hacer una ensalada
    if pepino >= 1 and lechuga >= 1 and jitomate >= 1:
        return ("Haz tu ensalada de lechuga, pepino y jitomate, ")
    else:
        return("No hay ingredientes suficientes")
    
def desayuno_1(yogurt,manzana):
    #Devueleve si es posible hacer el desayuno uno
    if yogurt >= 2 and manzana >= 2:
        return ("Haz tu yogurt con manzana, ")
    else:
        return ("No hay ingredientes suficientes")
    
def desayuno_2(huevo,jamon):
    #Devueleve si es posible hacer el desayuno dos
    if huevo >= 2 and jamon >= 1:
        return ("Haz tu huevo con jamón, ")
    else:
        return ("No hay ingredientes suficientes")
    
def desayuno_3(huevo,jamon,yogurt,manzana):
    if huevo >= 2 and jamon >= 1 and yogurt >= 2 and manzana >= 2:
        return ("Desayuno completo (Huevo con jamón y yogurt con manzana, )")
    else:
        return ("No hay ingredientes suficientes")

def comida_1(pepino,lechuga,jitomate,pollo):
    #Devueleve si es posible hacer la comida uno
    if pepino >= 1 and lechuga >= 1 and jitomate >= 1 and pollo >= 2:
        return("Haz pollo con ensalada, ")
    else:
        return ("No hay ingredientes suficientes")
    
def comida_2(pollo,res,repollo):
    #Devueleve si es posible hacer la comida dos
    if pollo >= 2 and res >= 2 and repollo >=1:
        return ("Haz  un stirfry, ")
    else:
        return ("No hay ingredientes suficientes")

def comida_3(pepino,lechuga,jitomate,res):
    #Devueleve si es posible hacer la comida tres 
    if res >= 2 and pepino >= 1 and lechuga >= 1 and jitomate >= 1:
        return ("Haz salpicón de res, ")
    else:
        return ("No hay ingredientes suficientes")
    
print (ensalada(pepino,lechuga,jitomate), """
esta opción se denominará ensalada""")
print ("")
print (desayuno_1 (yogurt,manzana),"este desayuno se denominará desayuno 1")
print ("")
print (desayuno_2 (var_5,jamon),"este desayuno se denominará desayuno 2")
print ("")
print (desayuno_3 (var_5,jamon,yogurt,manzana),"""
este desayuno se denominará desayuno 3""")
print ("")
print (comida_1 (pepino,lechuga,jitomate,pollo),"""
esta comida se denominará comida 1""")
print ("")
print (comida_2 (pollo,res,repollo),"esta comida se denominará comida 2")
print ("")
print (comida_3(pepino,lechuga,jitomate,res),"""
esta comida se denominará comida 3""")
print ("")

"""
Despliega recetas dependiendo de el tiempo
"""
print ("""En esta sección indicaras el tiempo con el que cuentas
para realizar tu comida""")
print ("Indica si quieres desayuno (1) o comida (2)")
def tiempo_desayuno(td):
    #Define que desayuno se puede hacer dependiendo del tiempo.
    if td < 20 and td > 4:
        if td >= 5 and td < 10:
            return ("Te recomendamos hacer el desayuno uno")
        else:
            return ("Te recomendamos hacer el desayuno dos")
    else:
        if td < 60 and td > 20:
            return ("Te recomendamos hacer el desayuno tres")
        else:
            return ("No se encontraron desayunos")
        
def tiempo_comida(tc):
    #Define que comida se puede hacer dependiendo del tiempo.
    if tc < 20 and tc > 15:
        return ("Te recomendamos hacer la comida uno")
    else:
        if tc < 40 and tc > 20:
            if tc >= 20 and tc < 30:
                return ("Te recomendamos hacer la comida dos")
            else:
                return ("Te recomendamos hacer la comida tres")
        else:
            return ("No se encontraron comidas")
        
opcion = int(input())
if (opcion == 1):
    print ("Inserta tiempo de desayuno")
    td = int(input())
    print (tiempo_desayuno(td))
     
if (opcion == 2):
    print ("Inserta tiempo de comida")
    tc = int(input())
    print (tiempo_comida(tc))

"""
Porciones de comidas y desayunos
"""

print ("Aquí tienes la opción de hacer más porciones de tus diversas comidas")
print ("Solo podrás preparar una comida a la vez")
print ("Selecciona la que te hayamos recomendado o la que te guste")
print ("¿Quieres hacer más porciones del desayuno 1?")
print ("Responde con sí o no")
ans1 = input()
if ans1 == "sí":
    desayuno1 = [125,250]
    print ("Indique porción de desayuno 1")
    print ("El orden es : yogurt (gramos) y manzana (gramos)")
    porcion = int (input())
    des1 =[]
    for i in desayuno1:
        acum = i * porcion
        des1.append (acum)
    print ("Nueva porción",des1)
else:
    print ("Ok")
print ("")   
print ("¿Quieres hacer más porciones del desayuno 2?")
print ("Responde con sí o no")
ans2 = input()
if ans2 == "sí":
    print ("El orden es : huevo (pieza) y jamón (pieza)")
    desayuno2 = [2,1]
    print ("Indique porción de desayuno 2")
    porcion = int (input())
    des2 =[]
    for i in desayuno2:
        acum = i * porcion
        des2.append(acum)
    print ("Nueva porción",des2)
else:
    print ("Ok")
print ("")    
print ("¿Quieres hacer más porciones del desayuno 3?")
print ("Responde con sí o no")
ans3 = input()
if ans3 == "sí":
    print ("""El orden es : huevo (pieza), jamón (pieza),
yogurt (gramos) y manzana (gramos)""")
    desayuno3 = [2,1,125,250]
    print ("Indique porción de desayuno 3")
    porcion = int (input())
    des3 =[]
    for i in desayuno3:
        acum = i * porcion
        des3.append (acum)
    print ("Nueva porción",des3)
else:
    print ("Ok")
print ("")   
print ("¿Quieres hacer más porciones de la ensalada?")
print ("Responde con sí o no")
ans4 = input()
if ans4 == "sí":
    print ("El orden es : pepino (pieza), lechuga (gramos), jitomate (pieza)")
    ensalada = [1,200,1]
    print ("Indique porción de ensalada")
    porcion = int (input())
    ens = []
    for i in ensalada:
        acum = i * porcion
        ens.append(acum)
    print (ens)
else:
    print ("Ok")
print ("")
print ("¿Quieres hacer más porciones de la comida 1?")
print ("Responde con sí o no")
ans5 = input()
if ans5 == "sí":
    print ("""El orden es : pepino (pieza), lechuga (gramos),
jitomate (pieza), pollo (gramos)""")
    comida1 = [1,200,1,120]
    print ("Indique porción de comida 1")
    porcion = int (input())
    com1 = []
    for i in comida1:
        acum = i * porcion
        com1.append (acum)
    print ("Nueva porción",com1)
else:
    print ("Ok")
print ("")
print ("¿Quieres hacer más porciones de la comida 2?")
print ("Responde con sí o no")
ans6 = input()
if ans6 == "sí":
    print ("El orden es :pollo (gramos), res (gramos) y repollo (gramos)")
    comida2 = [50,50,200]
    print ("Indique porción de comida 2 ")
    porcion = int (input())
    com2 = []
    for i in comida2:
        acum = i * porcion
        com2.append (acum)
    print ("Nueva porción",com2)
else:
    print ("Ok")
print ("")    
print ("¿Quieres hacer más porciones de la comida 3?")
print ("Responde con sí o no")
ans7 = input()
if ans7 == "sí":
    print ("""El orden es : pepino (pieza), lechuga (gramos),
jitomate (pieza), res (gramos)""")
    comida3 = [1,200,1,100]
    print ("Indique porción de comida 3")
    porcion = int (input())
    com3 = []
    for i in comida3:
        acum = i * porcion
        com3.append (acum)
    print ("Nueva porción",com3)
else:
    print ("Ok")
    
"""
Instrucciones de recetas
"""

print ("""De la comida que elegiste anteriormente,
coloca el número correspondiente""")
print ("""Si quieres el desayuno 1, coloca 1
Si quieres el desayuno 2, coloca 2.
Si quieres el desayuno 3, coloca 3.
Si quieres la ensalada, coloca 4.
Si quieres la comida 1, coloca 5.
Si quieres la comida 2, colaca 6.
Si quieres la comida 3 coloca 7.""")

def time_desayuno1 (tiempo):
#Define tiempo para hacer el desayuno 1
    lim = 9
    while tiempo < lim:
        print( "Minutos:",tiempo)
        if tiempo == 1:
            print("Del minuto 1-4, pica la manzana")
            time.sleep (20)
        elif tiempo == 5:
            print("Pon la manzana en un bowl")
            time.sleep (5)
        elif tiempo == 6:
            print("Coloca el yogurt")
            time.sleep (10)
        elif tiempo == 8:
            print("Disfruta")
        tiempo = tiempo + 1
        
def temp_desayuno2 (temp,gas,fuego):
#Define temperatura de cocción de desayuno 2
    lim = 70
    while temp < lim:
        gas = gas + 1
        temp = fuego * gas
    return (temp)

def time_desayuno2 (tiempo):
#Define tiempo de cocción de desayuno 2
    lim = 11
    while tiempo < lim:
        print( "Minutos:",tiempo)
        if tiempo == 1:
            print("Pon el jamon")
            time.sleep (5)
        elif tiempo == 2:
            print("Deja que se dore")
            time.sleep (5)
        elif tiempo == 3:
            print("Coloca los huevos")
            time.sleep (5)
        elif tiempo == 4:
            print("Del minuto 4-9, dejar que se cocine")
            time.sleep (25)
        elif tiempo == 10:
            print("Servir desayuno")
            time.sleep (5)
        tiempo = tiempo + 1
        
def time_ensalada (tiempo):
#Define tiempo para realizar la ensalada
    lim = 20
    while tiempo < lim:
        print( "Minutos:",tiempo)
        if tiempo == 1:
            print("Del minuto 1-17 corta los vegetales")
            time.sleep (50)
        elif tiempo == 18:
            print("Sirve tu ensalada")
        tiempo = tiempo + 1

def coccion_comida_1 (temp,gas,fuego):
#Define temperatura de cocción de comida 1
    lim = 74
    while temp < lim:
        gas = gas + 1
        temp = fuego * gas
    return (temp)

def time_comida1 (tiempo):
#Define tiempo de cocción de comida 1
    lim = 16
    while tiempo < lim:
        print( "Minutos:",tiempo)
        if tiempo == 1:
            print("Pon el pollo para asar")
            time.sleep (5)
        elif tiempo == 2:
            print("""Del minuto 2-4, deja que se dore,
mientras corta vegetales""")
            time.sleep (15)
        elif tiempo == 5:
            print("Girar el pollo para que se cocine del otro lado")
            time.sleep (5)
        elif tiempo == 6:
            print("""Del minuto 6-7, deja que se dore el pollo,
mientras corta vegetales""")
            time.sleep (10)
        elif tiempo == 8:
            print("Retira el pollo del sartén y deja enfriar")
            time.sleep (5)
        elif tiempo == 9:
            print ("Del minuto 9-12")
            print("Deja enfriar el pollo")
            print ("Y sigue cortando los vegetales que faltan")
            time.sleep (20)
        elif tiempo == 13:
            print("Corta el pollo en tiritas")
            time.sleep (5)
        elif tiempo == 14:
            print("Mezcla el pollo y los vegetales en un bowl")
            time.sleep (5)
        elif tiempo == 15:
            print("Sirve tu comida")
            time.sleep (5)
        tiempo = tiempo + 1

def coccion_comida_2 (temp,gas,fuego):
#Define temperatura de cocción de comida 2
    lim = 80
    while temp < lim:
        gas = gas + 1
        temp = fuego * gas
    return (temp)

def time_comida2 (tiempo):
#Define tiempo de cocción de comida 2
    lim = 23
    while tiempo < lim:
        print( "Minutos:",tiempo)
        if tiempo == 1:
            print ("Pon el pollo y la carne para asar")
            time.sleep (5)
        elif tiempo == 2:
            print ("Del minuto 2-10")
            print("Deja que se doren, mientras corta el repollo")
            time.sleep (50)
        elif tiempo == 11:
            print("Incorpora el repollo y sigue cocinando")
            time.sleep (5)
        elif tiempo == 12:
            print ("Del minuto 12-20")
            print("Dejar que se cocine")
            time.sleep (45)
        elif tiempo == 21:
            print("Servir")
            time.sleep (5)
        elif tiempo == 22:
            print("Disfruta tu comida")
            time.sleep (5)
        tiempo = tiempo + 1

def coccion_comida_3 (temp,gas,fuego):
#Define temperatura de cocción de comida 3
    lim = 100
    while temp < lim:
        gas = gas + 1
        temp = fuego * gas
    return (temp)

def time_comida3 (tiempo):
#Define tiempo de cocción de comida 3
    lim = 40
    while tiempo < lim:
        print( "Minutos:",tiempo)
        if tiempo == 1:
            print("Pon agua en una olla y coloca la carne")
            time.sleep (5)
        elif tiempo == 2:
            print ("Del minuto 2-10")
            print("Dejar cocinar la carne y mientra cortar vegetales")
            time.sleep (45)
        elif tiempo == 11:
            print ("Del minuto 11-20")
            print("Dejar cocinar la carne")
            time.sleep (50)
        elif tiempo == 21:
            print ("Del minuto 21-32 deja enfriar la carne")
            print("Y corta los vegetales que te falten")
            time.sleep (55)
        elif tiempo == 32:
            print ("Del minuto 32-37")
            print ("Desmenuzar la carne")
            time.sleep (25)
        elif tiempo == 38:
            print ("Mezcla en un bowl")
            time.sleep (5)
        elif tiempo == 39:
            print ("sirve y disfruta")
            time.sleep (5)
        tiempo = tiempo + 1

opcion2 = int(input())
if (opcion2 == 1):
    print ("DESAYUNO 1")
    print ("Pasos para realizarlo:")
    print (time_desayuno1(1))
print ("")

if (opcion2 == 2):
    print ("DESAYUNO 2")
    print ("La temperatura es","",temp_desayuno2(0,0,1))
    print ("Listo para realizar el alimento")
    print ("Pasos para realizarlo:")
    print (time_desayuno2(1))
print ("")

if (opcion2 == 3):
    print ("DESAYUNO 3")
    print ("Primero haremos el yogurt con manzana")
    print ("Pasos para realizarlo:")
    print (time_desayuno1(1))
    print ("Ahora el huevo con jamón")
    print ("La temperatura es","",temp_desayuno2(0,0,1))
    print ("Listo para realizar el alimento")
    print ("Pasos para realizarlo:")
    print (time_desayuno2(1))
print ("")

if (opcion2 == 4):
    print ("ENSALADA")
    print ("Pasos para realizarlo:")
    print (time_ensalada(1))
print ("")

if (opcion2 == 5):
    print ("COMIDA 1")
    print ("La temperatura es","",coccion_comida_1(0,0,1))
    print ("Listo para realizar el alimento")
    print ("Pasos para realizarlo:")
    print (time_comida1(1))
print ("")

if (opcion2 == 6):
    print ("COMIDA 2")
    print ("La temperatura es","",coccion_comida_2(0,0,1))
    print ("Listo para realizar el alimento")
    print ("Pasos para realizarlo:")
    print (time_comida2(1))
print ("")
    
if (opcion2 == 7):
    print ("COMIDA 3")
    print ("La temperatura es","",coccion_comida_3(0,0,1))
    print ("Listo para realizar el alimento")
    print ("Pasos para realizarlo:")
    print (time_comida3(1))
    
"""
Menús
"""
print ("")
print ("Menús por día")

menus = [
    ["Desayuno 1", "Ensalada", "Comida 1"],
    ["Desayuno 2", "Comida 2", "Ensalada"],
    ["Desayuno 2", "Comida 2", "Ensalada"],
    ["Desayuno 3", "Comida 3"],
    ["Desayuno 2", "Comida 3", "Ensalada"],
    ["Desayuno 1", "Comida 2"],
    ["Desayuno 2", "Comida 1"]
    ]

def menu_dia (menus, comida):
    #Imprime menus predeterminados que contengan la comida
    for lista in menus:
        for nom in lista:
            if (nom == comida):
                return (lista)

def crea_tu_menu(exterior, interior):
    #Crea una matriz con los gustos del usuario
    matriz= []
    i = 0
    while (i < exterior):
        j = 0
        lis = []
        while (j < interior):
            print ("Pon tu comida conforme la quieras en el día y da enter")
            val = (input())
            lis.append(val)
            j = j + 1
        matriz.append(lis)
        i = i + 1
    return matriz
            
print ("Ingresa un elemento que quieras en el día")
print ("")
print ("Las opciones son:")
print ("""Desayuno 1, Desayuno 2, Desayuno 3, Ensalada,
Comida 1, Comida 2, Comida 3""")
print ("Esta es nuestra recomendación",menu_dia(menus, input ()))
print ("")
print ("¡Ahora crea tus propios menus!")
print ("Las opciones son:")
print ("""Desayuno 1, Desayuno 2, Desayuno 3, Ensalada,
Comida 1, Comida 2, Comida 3""")
print ("")
print ("""Coloca el número de menus que quieras realizar,
después el numero de comidas del día
y finalmente coloca los elementos que quieres agregar""")
print ("")
print (crea_tu_menu(int(input()), int(input())))
print ("Ahora tienes tus menus o menú")
print ("¡Gracias por usar este sistema!")


