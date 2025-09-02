# Solicita la edad al usuario
edad = int(input("Introduce tu edad: "))

# Determina el estado de la persona según su edad
if edad < 17:
    print("Eres menor de edad.")
elif edad == 17:
    print("Eres casi mayor de edad.")
else:
    print("Eres mayor de edad.")

