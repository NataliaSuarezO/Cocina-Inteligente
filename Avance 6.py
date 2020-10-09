print ("Menús semanales")

menus = [
    ["Desayuno 1", "Ensalada", "Comida 1"],
    ["Desayuno 2", "Comida 2", "Ensalada"],
    ["Desayuno 2", "Comida 2", "Ensalada"],
    ["Desayuno 3", "Comida 3"],
    ["Desayuno 2", "Comida 3", "Ensalada"],
    ["Desayuno 1", "Comida 2"],
    ["Desayuno 2", "Comida 1"]
    ]

def menu_semana (menus, comida):
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
            val = (input())
            lis.append(val)
            j = j + 1
        matriz.append(lis)
        i = i + 1
    return matriz
            
print ("Ingresa un elemento que quieras en el día")
print ("Las opciones son:")
print ("""Desayuno 1, Desayuno 2, Desayuno 3, Ensalada,
Comida 1, Comida 2, Comida 3""")
print (menu_semana(menus, input ()))
print ("¡Ahora crea tus propios menus!")
print ("Las opciones son:")
print ("""Desayuno 1, Desayuno 2, Desayuno 3, Ensalada,
Comida 1, Comida 2, Comida 3""")
print ("Coloca el numero de menus y el numero de comidas")
print ("y después coloca los elementos que quieres agregar")
print (crea_tu_menu(int(input()), int(input())))
        