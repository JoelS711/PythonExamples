print("Ingrese fecha de nacimiento")
print("Dia de nacimiento: ")
dia = int(input())
print("Mes de nacimiento: ")
mes = int(input())
print("Año de nacimiento: ")
anio = int(input())

if mes == 1:
    print("Nacio en enero")
elif mes == 2:
    print("Nacio en fenero")
elif mes == 3:
    print("Nacio en marzo")
elif mes == 4:
    print("Nacio en abril")
elif mes == 5:
    print("Nacio en mayo")
elif mes == 6:
    print("Nacio en junio")
elif mes == 7:
    print("Nacio en julio")
elif mes == 8:
    print("Nacio en agosto")
elif mes == 9:
    print("Nacio en septiembre")
elif mes == 10:
    print("Nacio en octubre")
elif mes == 11:
    print("Nacio en noviembre")
elif mes == 12:
    print("Nacio en diciembre")
else:
    print("!!!Mes incorrecto!!!")

if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
	print("Usted nacio en un anio bisiesto")
else:
	print("Usted no nacio en un anio bisiesto")

print("Usted nacio en ",dia," ",mes ," ",anio)