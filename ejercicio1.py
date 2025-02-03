titulo = """\t
************************************
        Simulador de restaurante 
*************************************
"""
print(titulo)
entradas = input("Ingrese el numero de entradas\n")
platos= input("Ingrese el numero de platos\n")
postre = input("Ingrese el numero de postres\n")

entradas = int(entradas)
platos = int(platos)
postre = int(postre)

if 0 < entradas <=100:
    tiempo_entradas = entradas * 12
    print("Se ha de demorar", tiempo_entradas, "minutos en entradas")
else:
    tiempo_entradas = 0
    print("Entradas no validas\n")
    
if 0 <platos <=1000:
    tiempo_platos = platos * 15
    print("Se ha de demorar", tiempo_platos, "minutos en platos")
else:
    tiempo_platos = 0
    print("Platos no validos\n")
    
if 0 < postre <=100:
    tiempo_postres = postre * 10
    print("Se ha de demorar", tiempo_postres, "minutos en postres")
else: 
    tiempo_postres = 0
    print("Postres no validos\n")
    
tiempo_total = tiempo_entradas + tiempo_platos + tiempo_postres
if tiempo_entradas != 0  or tiempo_platos != 0 or tiempo_postres != 0:
    print("Se ha de demorar", tiempo_total, "minutos en total")
else:
    print("No han ingresado 3 datos validos")