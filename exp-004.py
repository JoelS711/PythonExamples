salir = False
while not salir:
    print("1. Ver listado")
    print("2. Ver listado filtrado")
    print("3. Agregar beneficiario")
    print("4. Buscar beneficiario")
    print("5. Borra beneficiario")
    print("6. Salir")
    opcion = int(input("Ingrese la opcion que desea ejecutar: "))
    nombres = []
    #cedula = []
    #tel = []

    if opcion == 1:
        print("Listado de beneficiarios: ")
        archivo = open('agenda.txt','r')
        mensaje = archivo.read()
        print(mensaje)
        archivo.close()
    elif opcion == 2:
        lb = str(input("Digite la letra por la que empiezan los beneficiarios: "))
    elif opcion == 3:
        print("Digite la información del beneficiario a agregar: ")
        nombres.append(input())
        nombres.append(input())
        nombres.append(input())
        archivo = open('agenda.txt','a')
        archivo.write(str(nombres[0]+"\n"))
        archivo.write(str(nombres[1]+"\n"))
        archivo.write(str(nombres[2]+"\n"))
        archivo.write("\n")
        #archivo.write(str(cedula))
        #archivo.write(str(tel))
        archivo.close()
        print("El beneficiario ha sido agregado al listado\n")
    elif opcion == 5:
        borrar = str(input("Digite la cedula del beneficiario a borrar: "))
        archivo = open('agenda.txt','r')
        for x in range(len(nombres)-1,-1,-1):
            if nombres[x] == borrar:
                nombres.pop(x)
                nombres.pop(x-1)
                nombres.pop(x+1)
        archivo.write(str(nombres))
        archivo.close()
    elif opcion == 6:
        print("Hasta pronto")
        break