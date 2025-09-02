# Solicita un número entero al usuario
numero = int(input("Introduce un número entero: "))

# Variable para almacenar la suma de los dígitos
suma_digitos = 0

# Usamos el valor absoluto para manejar números negativos
num = abs(numero)

# Bucle while para extraer y sumar cada dígito
while num > 0:
    digito = num % 10          # Extrae el último dígito
    suma_digitos += digito     # Suma el dígito
    num = num // 10            # Elimina el último dígito

# Muestra el resultado
print("La suma de los dígitos de", numero, "es:", suma_digitos)

