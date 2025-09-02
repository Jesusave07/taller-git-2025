# Lista inicial de tareas
tareas = ["Estudiar", "Comprar", "Limpiar"]

# Función para agregar una tarea
def agregar_tarea(tarea):
    tareas.append(tarea)
    print(f"Tarea '{tarea}' agregada.")

# Mostrar la lista antes y después de agregar la tarea
print("Tareas antes de agregar:")
print(tareas)

# Agregar una nueva tarea
agregar_tarea("Lavar ropa")

print("Tareas después de agregar:")
print(tareas)

