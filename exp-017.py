from typing import List

ltM = [] #Lista temperatura maxima
ltm = [] #Lista temperatura minima
ltMe = [] #Lista temperatura maxima con error
ltme = [] #Lista temperatura minima con error
det = [] #Lista dias con error de temperatura
dset = [] #Lista dias sin errores de temperatura
tde = 0 #Temperatura doble error
d = 0 #Dias
mm = 0 #Media temperatura minima
mM = 0 #Media temperatura maxima
p = 0 #promedio

#Se realiza el ciclo while para ingresar las temperaturas
while True:
    tM = float(input("Ingrese la temperatura maxima: "))
    tm = float(input("Ingrese la temperatura minima: "))

    #Se realizan los condicionales propuestos por el ejercicio
    if tM == 0 and tm == 0:
        break
    elif tM <= 35 and tm >= 5:
        ltM.append(tM)
        ltm.append(tm)
        dset.append(1)
    elif tM > 35 and tm >= 5:
        ltMe.append(tM)
        ltm.append(tm)
        det.append(1)
    elif tM <= 35 and tm < 5:
        ltM.append(tM)
        ltme.append(tm)
        det.append(1)
    elif tM > 35 and tm < 5:
        ltMe.append(tM)
        ltme.append(tm)
        det.append(1)
        tde = tde + 1

d = sum(dset) + sum(det) #Calcular dias totales
mm = sum(ltm) / len(ltm) #Calcular media temperatura minima
mM = sum(ltM) / len(ltM) #Calcular media temperatura maxima
p = ( len(det) / d ) * 100 #Calcular promedio

#Imprimimos respuestas
print("La salida de campo duro ", d, " dias")
print("Dias con error de temperatura ", len(det))
print("Dias temperaturas error menos de 5 grados ", len(ltme))
print("Dias temperaturas error maximo de 35 grados ", len(ltMe))
print("Dias con errores en ambas temperaturas ", tde)
print("Temperatura media minima es ", mm," y la temperatura media maxima es ", mM)
print("El porcentaje de dias que se reportaron errores es de ",p,"%")