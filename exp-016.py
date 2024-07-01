print("Ayudas Universidad del Bosque")
#Se pide al usuario nombre completo del estudiante
print("Ingrese su nombre completo: ")
nc = str(input())
#Se pide al usuario su edad
print("Ingrese su edad: ")
edad = int(input())
#Condicion si para saber si aplica en el descuento de la edad
if 15 <= edad <= 18:
    descuento1 = 0.25
    print("Su descuento por edad es de 25%")
elif 19 <= edad <= 21:
    descuento1 = 0.15
    print("Su descuento por edad es de 15%")
elif 22 <= edad <=25:
    descuento1 = 0.10
    print("Su descuento por edad es de 10%")
elif edad > 25:
    descuento1 = 0
    print("No aplica descuento")
#Se pide el ingreso numero de salarios minimos que recibe la familia
print("Ingrese el numero de salarios minimos que recibe su familia: ")
sm = float(input())
#Condicion si para saber si aplica al descuento de los salarios minimos
if sm <= 1:
    descuento2 = 0.30
    print("Descuento por ingresos familiares es de 30%")
elif 1 < sm <=2:
    descuento2 = 0.20
    print("Descuento por ingresos familiares es de 20%")
elif 2 < sm <=3:
    descuento2 = 0.10
    print("Descuento por ingresos familiares es de 10%")
elif 3 < sm <=4:
    descuento2 = 0.05
    print("Descuento por ingresos familiares es de 5%")
elif sm > 4:
    descuento2 = 0
    print("No tiene descuentos en ingresos familiares")
#Se pide el ingreso de la calificacion del examen de ingreso
print("Ingrese calificacion de examen de ingreso (0 a 100): ")
nota = int(input())
#Condicion si para saber si aplica al descuento de la calificacion del examen
if 80 <= nota < 86:
    descuento3 = 0.30
    print("Descuento por puntaje de ingreso es de 30%")
elif 86 <= nota < 91:
    descuento3 = 0.35
    print("Descuento por puntaje de ingreso es de 35%")
elif 91 <= nota < 96:
    descuento3 = 0.40
    print("Descuento por puntaje de ingreso es de 40%")
elif nota >= 96:
    descuento3 = 0.45
    print("Descuento por puntaje de ingreso es de 45%")
elif nota < 80:
    descuento3 = 0
    print("No tiene desceunto por puntaje de ingreso")
#Se suman los descuentos para ver el descuento total
destotal = (descuento1 + descuento2 + descuento3) * 100
#Se imprime el resultado final
print("El estudiante ",nc," de ",edad," anios de edad tendra un descuento total de ",destotal,"%")