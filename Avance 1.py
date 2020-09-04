"""
ESTE AVANCE SE CENTRA EN EVITAR EL DESPERDICIO DE ALIMENTOS
Tiempo de consumo de diversos alimentos
"""
print ("consumo preferente de tus alimentos")
print ("tipos de alimentos: verduras y frutas(1), lacteos(2)")
print ("embutido(3), carne fresca(4), huevo(5)")
print ("por favor pon el numero correspondiente de tu alimento")
alimento = int(input())
if alimento == 1:
    print ("verdura y fruta:","","Consumir dentro de una semana.")
if alimento == 2:
    print ("lacteo:","","Consumir en 5 dias")
if alimento == 3:
    print ("embutido:","","Consumir dentro de una semana")
if alimento == 4:
    print ("carne fresca:","","Consumir en 4 días")
if alimento == 5:
    print ("huevo:","","Consumir en 1 mes")

"""
Conteo de los alimentos
"""
print ("conteo de los alimentos")
print ("coloca tu numero de alimentos:")
print ("verduras y frutas:")
var_1= int(input())
print ("lacteos:")
var_2= int(input())
print ("embutido:") 
var_3=int(input())
print("carne fresca:")
var_4= int(input())
print("Huevos:")
var_5=int(input())
total_de_alimentos= var_1 + var_2 + var_3 + var_4 + var_5
print ("total de alimentos:",total_de_alimentos)
print ("indica la cantidad de alimentos que utilizaste")
var_6= int(input())
total_alternativo= total_de_alimentos - var_6
print ("Nuevo total:", total_alternativo)
print ("Especifica de cuál tomaste, tus opciones son: verduras y frutas,")
print ("lacteos, embutidos y carne fresca")
print ("indica que cantidad tomaste del alimento")
var_7=  str(input())
var_8= int(input())
if var_7 == "verduras y frutas":
    print ("nueva cantidad de verduras y frutas:",var_1 - var_8)
if var_7 == "lacteos":
    print ("nueva cantidad de lacteos:",var_2 - var_8)
if var_7 == "embutidos":
    print ("nueva cantidad de embutidos:",var_3 - var_8)
if var_7 == "carne fresca":
    print ("nueva cantidad de carne fresca:",var_4 - var_8)
if var_7 == "huevo":
    print ("nueva cantidad de huevo:",var_5 - var_8)

    



