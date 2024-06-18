#Escribir un programa que solicite 
# capturar por consola o pantalla las notas 
# de 6 estudiantes y nos informe 
# cuantos tienen notas mayores o iguales a 
# 3.0 y cuantos menores a 3.0

z = 6
notam = 0
notaM = 0
while 0 < z <= 6:
    print("Ingrese la nota del estudiante: ")
    nota = float(input())
    if nota < 3:
        notam = notam + 1
        z = z - 1
    elif 3<= nota <=5:
        notaM = notaM + 1
        z = z - 1
    elif nota > 5:
        print("La nota tiene que ser menor o igual a 5 o mayor e  igual a 0")
    elif nota < 0:
        print("La nota tiene que ser mayor o igual a 0")

print("Estudiantes con una nota de mas o igual de 3 son: ",notaM)
print("Estudiantes con una nota menor a 3 son: ",notam)