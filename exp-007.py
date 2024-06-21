print("Ayudas Universidad del Bosque")
print("Ingrese su nombre completo: ")
nc = str(input())
print("Ingrese su edad: ")
edad = int(input())

if 15 <= edad <= 18:
    descuento1 = 25
elif 19 <= edad <= 21:
    descuento1 = 15
elif 22 <= edad <=25:
    descuento1 = 10
elif edad > 25:
    descuento1 = 0

print("Ingrese el numero de salarios minimos que recibe su familia: ")
sm = float(input())

if sm <= 1:
    descuento2 = 30
elif 1 < sm <=2:
    descuento2 = 20
elif 2 < sm <=3:
    descuento2 = 10
elif 3 < sm <=4:
    descuento2 = 5
elif sm > 4:
    descuento2 = 0

print("Ingrese calificacion de examen de ingreso (0 a 100): ")
nota = int(input())

if 80 <= nota < 86:
    descuento3 = 30
elif 86 <= nota < 91:
    descuento3 = 35
elif 91 <= nota < 96:
    descuento3 = 40
elif nota >= 96:
    descuento3 = 45
elif nota < 80:
    descuento3 = 0

print("Descuento por edad es de ",descuento1,"%")
print("Descuento por ingresos es de ",descuento2,"%")
print("Descuento por nota de examen es de ",descuento3,"%")

destotal = (descuento1 + descuento2 + descuento3)

print("El estudiante ",nc," de ",edad," anios de edad tendra un descuento total de ",destotal,"%")