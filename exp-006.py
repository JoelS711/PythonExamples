salir = False
while not salir:
    print("1. Ver listado")
    print("2. Ver listado filtrado")
    print("3. Agregar beneficiario")
    print("4. Buscar beneficiario")
    print("5. Borra beneficiario")
    print("6. Salir")
    opcion = int(input("Ingrese la opcion que desea ejecutar: "))

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
        nombre = str(input())
        cedula = str(input())
        tel = str(input())
        archivo = open('agenda.txt','a')
        archivo.write(nombre + "\n")
        archivo.write(cedula + "\n")
        archivo.write(tel + "\n")
        archivo.write("\n")
        per = [nombre,cedula,tel]
        archivo.close()
        print("El beneficiario ha sido agregado al listado\n")
    elif opcion == 4:
        bb = str(input("Digite el nombre y apellido del beneficiario a buscar: "))
        archivo = open("agenda.txt","r")
        buscar = archivo.readline(bb)
        print(buscar)
        print(buscar + 1)
        print(buscar + 2)
        archivo.close()
    elif opcion == 5:
        borrar = str(print("Digite la cedula del beneficiario a borrar: "))
        archivo = open('agenda.txt','w')
        for borrar in archivo:
            xf = borrar.replace(borrar,"")
            archivo.write(xf)
        archivo.close()
    elif opcion == 6:
        print("Hasta pronto")
        break