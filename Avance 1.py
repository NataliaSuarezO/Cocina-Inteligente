"""
Tiempo de consumo de diversos alimentos
"""
print ("Consumo preferente de tus alimentos")
print("")
print ("TIPOS DE ALIMENTOS: Verduras y frutas(1), lácteos(2), embutido(3), carne fresca(4), huevo(5)")
print("")
print ("Por favor pon el número correspondiente de tu alimento")
print("")
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
print("")
print ("CONTEO DE TUS ALIMENTOS")
print("")
print ("COLOCA NÚMERO DE ALIMENTOS:")
print ("Verduras y frutas:")
var_1= int(input())
print("")
print ("Lácteos:")
var_2= int(input())
print("")
print ("Embutido:") 
var_3=int(input())
print("")
print("Carne fresca:")
var_4= int(input())
print("")
print("Huevos:")
var_5=int(input())
print("")
total_de_alimentos= var_1 + var_2 + var_3 + var_4 + var_5
print ("TOTAL DE ALIMENTOS:",total_de_alimentos)
print("")
print ("¿TOMASTE ALGÚN ALIMENTO?, SI ES ASÍ COLOCA LA CANTIDAD")
var_6= int(input())
total_alternativo= total_de_alimentos - var_6
print ("Nuevo total:", total_alternativo)
print ("Especifica de cuál tomaste, tus opciones son: VERDURAS Y FRUTAS, LÁCTEOS, EMBUTIDOS, CARNE FRESCA, HUEVO (colocar el nombre en mayúsculas como se indica) y cantidad que tomaste del alimento")
print("")
var_7=  str(input())
var_8= int(input())
print("")
if var_7 == "VERDURAS Y FRUTAS":
    print ("NUEVA CANTIDAD DE FRUTAS Y VERDURAS:",var_1 - var_8)
if var_7 == "LÁCTEOS":
    print ("NUEVA CANTIDAD DE LÁCTEOS:",var_2 - var_8)
if var_7 == "EMBUTIDOS":
    print ("NUEVA CANTIDAD DE EMBUTIDOS:",var_3 - var_8)
if var_7 == "CARNE FRESCA":
    print ("NUEVA CANTIDAD DE CARNE FRESCA:",var_4 - var_8)
if var_7 == "HUEVO":
    print ("NUEVA CANTIDAD DE HUEVO:",var_5 - var_8)

    



