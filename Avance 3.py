#Ingresa el tiempo que se tiene y lanza que opción es la mejor
def tiempo_desayuno(td):
    #Define que desayuno se puede hacer dependiendo del tiempo.
    if td < 20 and td > 4:
        if td == 5 and td < 10:
            return ("desayuno uno")
        else:
            return ("desayuno dos")
    else:
        if td == 60 and td > 20:
            return ("desayuno tres")
        else:
            return ("No se encontraron desayunos")
        
def tiempo_comida(tc):
    #Define que comida se puede hacer dependiendo del tiempo.
    if tc == 20 and tc > 15:
        return ("comida uno")
    else:
        if tc == 40 and tc > 20:
            if tc > 20 and tc < 30:
                return ("comida dos")
            else:
                return ("comida tres")
        else:
            return ("No se encontraron comidas")
            
print ("Inserta tiempo de desayuno")
print (tiempo_desayuno(int(input())))
print ("Inserta tiempo de comida")
print (tiempo_comida(int(input())))
