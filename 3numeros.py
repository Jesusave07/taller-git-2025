# Solicita tres números al usuario
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))
numero3 = float(input("Introduce el tercer número: "))

# Determina cuál es el mayor usando if, elif y else
if numero1 > numero2 and numero1 > numero3:
    mayor = numero1
    print("El primer número es el mayor:", mayor)
elif numero2 > numero1 and numero2 > numero3:
    mayor = numero2
    print("El segundo número es el mayor:", mayor)
elif numero3 > numero1 and numero3 > numero2:
    mayor = numero3
    print("El tercer número es el mayor:", mayor)
else:
    print("Hay al menos dos números iguales y mayores, o todos son iguales.")

