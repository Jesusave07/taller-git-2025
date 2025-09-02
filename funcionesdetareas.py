# Lista inicial de tareas
tareas = ["Estudiar", "Comprar", "Limpiar"]

# Función para agregar una tarea
def agregar_tarea(tarea):
    tareas.append(tarea)
    print(f"Tarea '{tarea}' agregada.")

# Función para eliminar una tarea si existe
def eliminar_tarea(tarea):
    if tarea in tareas:
        tareas.remove(tarea)
        print(f"Tarea '{tarea}' eliminada.")
    else:
        print(f"La tarea '{tarea}' no existe en la lista.")

# Función para mostrar todas las tareas
def mostrar_tareas():
    print("\nLista de tareas:")
    for tarea in tareas:
        print(f"- {tarea}")
    print()  # Línea en blanco para separar

# --- PRUEBA DE FUNCIONES ---

# Mostrar tareas iniciales
mostrar_tareas()

# Agregar una tarea
agregar_tarea("Lavar ropa")

# Eliminar una tarea existente
eliminar_tarea("Comprar")

# Eliminar una tarea que no existe
eliminar_tarea("Correr")

# Mostrar tareas actualizadas
mostrar_tareas()
