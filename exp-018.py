nombres = []
salir = False
while not salir:
    print("Menu Principal")
    print("1. Ver listado")
    print("2. Ver Listado filtrado")
    print("3. Agregar beneficiario")
    print("4. Buscar beneficiario")
    print("5. Borra beneficiario")
    print("6. Salir\n")
    opcion = int(input())
    
    if opcion == 1:
        print("Listado de beneficiarios\n")
        archivo = open('agenda.txt','r')
        mensaje = archivo.read()
        print(mensaje)
        archivo.close()
    elif opcion == 2:
        lb = str(input("Digite la letra por la que empiezan los beneficiarios:\n"))
        print("Listado filtrado de beneficiarios:\n")
        for i in range (len(nombres)-1):
            if nombres[i][0] == lb:
               print(nombres[i])
               print(nombres[i+1])
               print(nombres[i+2] + "\n")
    elif opcion == 3:
        print("Digite la información del beneficiario a agregar:")
        nombres.append(input())
        nombres.append(input())
        nombres.append(input())
        archivo = open('agenda.txt','a')
        archivo.write(str(nombres[len(nombres)-3] +"\n"))
        archivo.write(str(nombres[len(nombres)-2] +"\n"))
        archivo.write(str(nombres[len(nombres)-1] +"\n"))
        archivo.close()
        print("El beneficiario ha sido agregado\n")
    elif opcion == 4:
        bb = str(input("Digite el nombre y apellido del beneficiario a buscar:\n"))
        for i in range (len(nombres)-1):
            if nombres[i] == bb:
               print(nombres[i])
               print(nombres[i+1])
               print(nombres[i+2] + "\n")
    elif opcion == 5:
        borrar = str(input("Digite la cedula del beneficiario a borrar:\n"))
        archivo = open('agenda.txt','w')
        for x in range(len(nombres)-1):
            if x < len(nombres):
                if nombres[x] == borrar:
                    nombres.pop(x)
                    nombres.pop(x)
                    nombres.pop(x-1)
                    for i in nombres:
                        archivo.write(i+"\n")
        print("El usuario ha sido eliminado del listado\n")
        archivo.close()
        
        
    elif opcion == 6:
        print("Hasta pronto")
        break