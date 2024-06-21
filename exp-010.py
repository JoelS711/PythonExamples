nombre = input("Ingrese nombre del trabajador: ")
horas = int(input("Ingrese horas trabajadas: "))
tarifa = int(input("Ingrese la tarifa: "))
if horas <= 35 :
    sbruto = horas * tarifa
else:
    sbruto = (35 * tarifa) + ((horas - 35)* 1.5 * tarifa)
if sbruto <= 2000:
    impuesto = 0
else:
    if sbruto <= 2200:
        impuesto = (sbruto - 2000) * 0.20
    else:
        impuesto = (220 * 0.20) + (sbruto - 2220) * 0.30

sneto = sbruto - impuesto
print("Trabajador: "+nombre)
print("Sueldo bruto: "+str(sbruto))
print("Impuesto: "+str(impuesto))
print("Sueldo neto: "+str(sneto))