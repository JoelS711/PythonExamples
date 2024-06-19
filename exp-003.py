salir = False
while not salir:
    print("--------MENU--------")
    print("-----1. SUMA--------")
    print("-----2. RESTA--------")
    print("----3. DIVISION------")
    print("--4. MULTIPLICACION--")
    print("-----5. RESIDUO-----")
    print("-----6. ELEVADO-----")
    print("-----7. SALIR-------")

    print("Ingrese la opcion que desea ejecutar")
    opcion = int(input())


    if opcion == 1:
        print("Ingrese el primer numero")
        x = float(input())
        print("Ingrese el segundo numero")
        y = float(input())
        resultado = x + y
        print("El resultado es: ",resultado)
    elif opcion == 2:
        print("Ingrese el primer numero")
        x = float(input())
        print("Ingrese el segundo numero")
        y = float(input())
        resultado = x - y
        print("El resultado es: ",resultado)   
    elif opcion == 3:
        print("Ingrese el primer numero")
        x = float(input())
        print("Ingrese el segundo numero")
        y = float(input())
        resultado = x / y
        print("El resultado es: ",resultado)
    elif opcion == 4:
        print("Ingrese el primer numero")
        x = float(input())
        print("Ingrese el segundo numero")
        y = float(input())
        resultado = x * y
        print("El resultado es: ",resultado)
    elif opcion == 5:
        print("Ingrese el primer numero")
        x = float(input())
        print("Ingrese el segundo numero")
        y = float(input())
        resultado = x % y
        print("El resultado es: ",resultado)
    elif opcion == 6:
        print("Ingrese el primer numero")
        x = float(input())
        print("Ingrese el segundo numero")
        y = float(input())
        resultado = x ** y
        print("El resultado es: ",resultado)
    elif opcion == 7:
        break
    elif opcion > 7:
        print("¡Ingrese una opcion valida!")