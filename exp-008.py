print("Ingrese el primer numero: ")
n1 = float(input())
print("Ingrese el segundo numero: ")
n2 = float(input())

print("Ingrese que tipo de operacion desea realizar")
print("1. Suma")
print("2. Resta")
print("3. Division")
print("4. Multiplicacion")
opcion = int(input())

if opcion == 1:
    print("La suma es: ", n1 + n2)

if opcion == 2:
    print("La resta es: ", n1 - n2)

if opcion == 3:
    print("La division: ", n1 / n2)

if opcion == 4:
    print("La multiplicacion es: ", n1 * n2)

else:  print("Opcion no valida")