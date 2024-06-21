print("Ingrese el primer numero: ")
a1 = float(input())
print("Ingrese el segundo numero: ")
a2 = float(input())
print("Ingrese el tercer numero: ")
a3 = float(input())

num = [a1, a2, a3]
menormayor = sorted(num)
print(menormayor)
mayormenor = sorted(num, reverse=True)
print(mayormenor)