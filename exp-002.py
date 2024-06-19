invitados = [1090000180, 100000587, 63624627, 20202020, 20202021, 20212021]
ingreso = []
print("Anadir invitados SI(1) NO(0)")
anadir = int(input())

while anadir == 1:
    print("Ingrese el numero de documento: ")
    ndocumento = int(input())
    if ndocumento in invitados:
        print("Si esta invitado")
        ingreso.append(ndocumento)
        invitados.remove(ndocumento)
        print("Han ingresado estos invitados ", ingreso)
        print("Faltan por ingresar ",invitados)
    else:
        print("No se encuentra en la lista")

    print("Anadir invitados SI(1) NO(0)")
    anadir = int(input())