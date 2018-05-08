import numpy as np
import matplotlib.pyplot as plt

#Sortea la lista de opciones y la retorna
def sort_doors():
    #Lista de opciones
    ls = ["goat","goat","car"]
    #Cambia posiciones de lista aleatoriamente
    np.random.shuffle(ls)
    return ls
    

#Escoge una puerta aleatoriamente
def choose_door():
    #Se elige un numero entre 0,1,2 aleatoriamente
    ans = np.random.choice(3)
    return ans

#Revela donde hay cabra
#Se recorre la lista para posiciones diferentes a choice
# - Choice- es la elegida por el participante
#La primera cabra encontrada se reemplaza por Goat Monty
def reveal_door(lista,choice):

    #Se recorre la lista. Para indice diferente de choice
    #se reemplaza valor si tiene una cabra 
    for i in range(3):
        if(i != choice):
            if(lista[i] == "goat"):
	          lista[i] = "GOAT_MONTY"
                  break

    return lista

#Revela la puerta elegida por jugador, teniendo en cuenta si cambio 
# su eleccion inicial
#Choice: puerta elegida por jugador, numero entre 0,1,2
#Change: falso si jugador no cambio de puerta     
def finish_game(lista, choice, change):
    ans = -1
    cc = -20
    if(change == False):
        ans = lista[choice]
    else:
        for i in range(3):
            if(lista[i] == "GOAT_MONTY"):
                cc = i
        for k in range(3):
            if((k != cc) and (k != choice)):
                ans = lista[k] 
 
    return ans    
      
#Simular juego 100 veces para True y 100 para False
N = 100
ansT = list()
ansF = list()

#Se realiza todo el procedimiento para True
#Jugador cambia de puerta
for i in range(N):
    lsi = sort_doors()
    ele = choose_door()
    lsm = reveal_door(lsi,ele)
    anss = finish_game(lsm,ele,True)
    ansT.append(anss)
    
#Se realiza todo el procedimiento para False
#Jugador NO cambia de puerta
for i in range(N):
    lsi = sort_doors()
    ele = choose_door()
    lsm = reveal_door(lsi,ele)
    anss = finish_game(lsm,ele,False)
    ansF.append(anss)

#Cuenta las veces en que se obtiene "Car" -Gana
#Si cambia de puerta -True
wwT = 0
for i in ansT:
    if(i == "car"):
        wwT += 1
#Cuenta las veces en que se obtiene "Car" -Gana
#Si NO cambia de puerta -False
wwF = 0
for i in ansF:
    if(i == "car"):
        wwF += 1      

#Totalidad de eventos tanto para true como para false
TT = len(ansT)
TF = len(ansF)

#Probabilidad ganar si hay cambio
pT = float(wwT)/TT

#Probabilidad ganar si NO hay cambio
pF = float(wwF)/TF

#Mensajes finales de probabilidad
print "Probabilidad de ganar si jugador realiza cambio " + str(pT)
print "Probabilidad de ganar si jugador NO realiza cambio " + str(pF)

