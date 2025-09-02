# Lista inicial de tareas
tareas = ["Estudiar", "Comprar", "Limpiar" , "lavar ropa"]

# Función para eliminar una tarea si existe
def eliminar_tarea(tarea):
    if tarea in tareas:
        tareas.remove(tarea)
        print(f"Tarea '{tarea}' eliminada.")
    else:
        print(f"La tarea '{tarea}' no existe en la lista.")

# Mostrar lista antes de eliminar
print("Tareas antes de eliminar:")
print(tareas)

# Intentar eliminar una tarea que sí existe
eliminar_tarea("Comprar")

# Intentar eliminar una tarea que no existe
eliminar_tarea("Correr")

# Mostrar lista después de eliminar
print("Tareas después de eliminar:")
print(tareas)
