# Diccionario inicial de contactos
contactos = {
    "Adrian": "642166118",
    "Jhon":  "612426049",
    "Carlos": "555123456"
}
# Función para mostrar todos los contactos
def mostrar_contactos():
    print("Lista de contactos:")
    for nombre, telefono in contactos.items():
        print(f"- {nombre}: {telefono}")

# --- Código que se ejecuta al correr el archivo ---
if __name__ == "__main__":
    mostrar_contactos()
