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
        print(f"La tarea '{tarea}' no se encontró.")

# Función para mostrar todas las tareas
def mostrar_tareas():
    print("Lista de tareas:")
    for tarea in tareas:
        print(f"- {tarea}")

# Programa principal: ejemplo de uso
if __name__ == "__main__":
    mostrar_tareas()
    agregar_tarea("Lavar ropa")
    eliminar_tarea("Comprar")
    mostrar_tareas()

