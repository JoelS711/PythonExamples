from typing import List

tn = 0 #temperatura normal
tde = 0 #temperatura doble error
tme = 0 #temperatura minima error
tMe = 0 #temperatua maxima error
d = 0 #Dia
mm = 0 #Media minima
mM = 0 #Media maxima
det = 0 #Dias con errores totales
ltM = [] #Lista temperatura maxima
ltm = [] #Lista temperatura minima

while True:
    tM = float(input("Ingrese la temperatura maxima: "))
    tm = float(input("Ingrese la temperatura minima: "))

    if tM == 0 and tm == 0:
        break
    elif tM <= 35 and tm >= 5:
        ltM.append(tM)
        ltm.append(tm)
        tn = tn + 1
    elif tM > 35 and tm >= 5:
        tMe = tMe + 1  
    elif tM <= 35 and tm < 5:
        tme = tme + 1
    elif tM > 35 and tm < 5:
        tde = tde + 1
        tMe = tMe + 1
        tme = tme + 1

d = tn + tMe + tme + tde
mm = sum(ltm) / tn #Calcular media temperatura minima
mM = sum(ltM) / tn #Calcular media temperatura maxima
p = (tde + tme + tMe) / d  * 100 #Calcular porcentaje
det = tMe + tme + tde

print("La salida de campo duro ", d, " dias")
print("Dias con error de temperatura ",det )
print("Dias temperaturas error menos de 5 grados ", tme)
print("Dias temperaturas error maximo de 35 grados ",tMe)
print("Dias con errores en ambas temperaturas ", tde)
print("Temperatura media minima es ", mm," y la temperatura media maxima es ", mM)
print("El porcentaje de dias que se reportaron errores es de ",p,"%")