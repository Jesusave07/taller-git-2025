# Diccionario de contactos inicial
contactos = {
    "Adrian": "642166118",
    "Jhon": "612426049",
    "Carlos": "555123456"
}

# Función para agregar un nuevo contacto
def agregar_contacto(nombre, telefono):
    if nombre in contactos:
        print(f"El contacto '{nombre}' ya existe con el número {contactos[nombre]}")
    else:
        contactos[nombre] = telefono
        print(f"Contacto '{nombre}' agregado con éxito.")

# Función para eliminar un contacto
def eliminar_contacto(nombre):
    if nombre in contactos:
        del contactos[nombre]
        print(f"Contacto '{nombre}' eliminado con éxito.")
    else:
        print(f"El contacto '{nombre}' no existe.")

# Agregar contacto Jackelin
agregar_contacto("Jackelin", "04242038259")

# Eliminar contacto Carlos
eliminar_contacto("Carlos")

# Mostrar lista de contactos actualizada
print("\nLista de contactos actualizada:")
for nombre, telefono in contactos.items():
    print(f"{nombre}: {telefono}")
