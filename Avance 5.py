
print ("Las porciones que se indiquen están en gramos")
desayuno1 = [125,250]
print ("Indique porción de desayuno 1")
print ("El orden es : yogurt y manzana")
porcion = int (input())
for i in desayuno1:
    acum = i * porcion
    print (acum)
    
print ("Las porciones están en piezas")
print ("El orden es : huevo y jamón")
desayuno2 = [2,1]
print ("Indique porción de desayuno 2")
porcion = int (input())
for i in desayuno2:
    acum = i * porcion
    print (acum)
    
print ("Las porciones están en piezas y gramos")
print ("El orden es : huevo, jamón, yogurt y manzana")
desayuno3 = [2,1,125,250]
print ("Indique porción de desayuno 3")
porcion = int (input())
for i in desayuno3:
    acum = i * porcion
    print (acum)     

print ("Las porciones están en gramos y piezas")
print ("El orden es : pepino, lechuga jitomate")
ensalada = [1,200,1]
print ("Indique porción de ensalada")
porcion = int (input())
for i in ensalada:
    acum = i * porcion
    print (acum)
    
print ("Las porciones están en gramos y piezas")
print ("El orden es : pepino, lechuga jitomate, pollo")
comida1 = [1,200,1,100]
print ("Indique porción de comida 1")
porcion = int (input())
for i in comida1:
    acum = i * porcion
    print (acum)

print ("Las porciones están en gramos")
print ("El orden es :pollo, res y repollo")
comida2 = [50,50,200]
print ("Indique porción de comida 2 ")
porcion = int (input())
for i in comida2:
    acum = i * porcion
    print (acum)

print ("Las porciones están en piezas y gramos")
print ("El orden es : pepino, lechuga jitomate, res")
comida3 = [1,200,1,100]
print ("Indique porción de comida 3")
porcion = int (input())
for i in comida3:
    acum = i * porcion
    print (acum)     