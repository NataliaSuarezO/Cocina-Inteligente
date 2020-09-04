def ensalada(pepino,lechuga,jitomate):
    #Devueleve si es posible hacer una ensalada
    if pepino and lechuga and jitomate >= 1:
        return ("Haz tu ensalada")
    else:
        return("No hay ingredientes suficientes")
    
def desayuno_1(yogurt,manzana):
    #Devueleve si es posible hacer el desayuno uno
    if yogurt and manzana >= 2:
        return ("Haz tu desayuno uno")
    else:
        return ("No hay ingredientes suficientes")
    
def desayuno_2(huevo,jamon):
    #Devueleve si es posible hacer el desayuno dos
    if huevo >= 2 and jamon >= 1:
        return ("Haz tu desayuno dos")
    else:
        return ("No hay ingredientes suficientes")
    
def desayuno_3(huevo,jamon,yogurt,manzana):
    return (desayuno_1(yogurt,manzana) + desayuno_2 (huevo,jamon))

def comida_1(pepino,lechuga,jitomate,pollo,mantequilla):
    #Devueleve si es posible hacer la comida uno
    if pepino and lechuga and jitomate >= 1 and pollo and mantequilla >= 2:
        return (ensalada(pepino,lechuga,jitomate) and "Haz pollo con ensalada")
    else:
        return ("No hay ingredientes suficientes")
    
def comida_2(pollo,res,repollo):
    #Devueleve si es posible hacer la comida dos
    if pollo and res >= 2 and repollo >=1:
        return ("Haz comida dos")
    else:
        return ("No hay ingredientes suficientes")

def comida_3(pepino,lechuga,jitomate,pollo,mantequilla,repollo,res):
    #Devueleve si es posible hacer la comida tres 
    if pollo and res and mantequilla >= 2 and repollo and pepino and lechuga and jitomate >= 1:
        return (comida_1(pepino,lechuga,jitomate,pollo,mantequilla) + comida_2(pollo,res,repollo))
    else:
        return ("No hay ingredientes suficientes")
    
print (ensalada(2,3,1))
print (desayuno_1 (3,2))
print (desayuno_2 (5,5))
print (desayuno_3 (6,10,9,7))
print (comida_1 (2,3,1,4,3))
print (comida_2 (2,1,10))
print (comida_3 (3,4,2,4,1,3,5))



