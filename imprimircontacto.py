contactos = {
    "Adrian": "642166118",
    "Jhon": "612426049",
    "Carlos": "555123456"
}

def agregar_contacto(nombre, telefono):
    if nombre in contactos:
        print(f"El contacto '{nombre}' ya existe con el número {contactos[nombre]}")
    else:
        contactos[nombre] = telefono
        print(f"Contacto '{nombre}' agregado con éxito.")

def eliminar_contacto(nombre):
    if nombre in contactos:
        del contactos[nombre]
        print(f"Contacto '{nombre}' eliminado con éxito.")
    else:
        print(f"El contacto '{nombre}' no existe.")

def mostrar_contactos():
    if contactos:
        print("\nLista de contactos:")
        for nombre, telefono in contactos.items():
            print(f"{nombre}: {telefono}")
    else:
        print("No hay contactos en la agenda.")

# Agregar contacto Jackelin
agregar_contacto("Jackelin", "04242038259")

# Eliminar contacto Carlos
eliminar_contacto("Carlos")

# Mostrar todos los contactos
mostrar_contactos()
