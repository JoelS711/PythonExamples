ht = int(input("Ingrese horas trabajadas: "))
vh = float(input("Ingrese valor hora: "))

def horas_normales():
    hn = ht * vh
    print("Las horas extras ",hn)
    return

def horas_extras():
    he = (ht-40)*1.5*vh
    print("Las horas extras ",he)
    return

def sueldo_bruto():
    sb = (ht * vh) + ((ht-40)*1.5*vh)
    print("El sueldo bruto es: ",sb)
    return 

def dparafiscales():
    dp = ((ht * vh) + ((ht-40)*1.5*vh)) * 0.09
    print("Descuentos parafiscales ",dp)
    return

def dsalud():
    ds = ((ht * vh) + ((ht-40)*1.5*vh)) * 0.04
    print("Descuento salud: ",ds)
    return dsalud