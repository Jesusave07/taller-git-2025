# Solicita al usuario dos números y los convierte a flotantes
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))

# Realiza las operaciones
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2

# Para evitar error de división por cero
if numero2 != 0:
    division = numero1 / numero2
else:
    division = "No se puede dividir entre cero."

# Muestra los resultados
print("\nResultados:")
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)

# Evalúa si la suma es mayor que 100 usando operadores lógicos
if suma > 100 and isinstance(suma, (int, float)):
    print("La suma es mayor que 100.")
else:
    print("La suma no es mayor que 100.")

