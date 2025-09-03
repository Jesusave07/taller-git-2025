import datetime

class Tarea:
    def __init__(self, nombre, descripcion, prioridad="ninguna", etiquetas=[]):
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = 'Pendiente'
        self.prioridad = prioridad.lower()
        self.etiquetas = etiquetas
        self.fecha_creacion = datetime.datetime.now()
    
    def marcar_completada(self):
        self.estado = 'Completada'
    
    def __str__(self):
        return (f"Nombre: {self.nombre}\n"
                f"Descripción: {self.descripcion}\n"
                f"Estado: {self.estado}\n"
                f"Prioridad: {self.prioridad.capitalize()}\n"
                f"Etiquetas: {', '.join(self.etiquetas)}\n"
                f"Creada el: {self.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')}\n")

class GestorDeTareas:
    def __init__(self):
        self.tareas = []
        self._cargar_tareas_iniciales()

    def _cargar_tareas_iniciales(self):
        # Tareas iniciales para Adrian
        self.agregar_tarea("Estudiar", "Revisar apuntes de clase", "alta", ["estudio", "escuela"], mostrar_mensaje=False)
        self.agregar_tarea("Hacer ejercicio", "Ejercicio de 30 minutos", "media", ["salud", "fitness"], mostrar_mensaje=False)
        self.agregar_tarea("Limpiar", "Limpiar la habitación", "baja", ["hogar", "orden"], mostrar_mensaje=False)
        self.agregar_tarea("Pasear", "Salir a caminar", "ninguna", ["aire libre", "relajación"], mostrar_mensaje=False)
        self.agregar_tarea("Botar la basura", "Sacar la basura", "media", ["hogar", "limpieza"], mostrar_mensaje=False)

    def agregar_tarea(self, nombre, descripcion, prioridad="ninguna", etiquetas=[], mostrar_mensaje=True):
        nueva = Tarea(nombre, descripcion, prioridad, etiquetas)
        self.tareas.append(nueva)
        if mostrar_mensaje:
            print("✅ Tarea agregada correctamente.")

    def mostrar_todas(self):
        if not self.tareas:
            print("⚠️ No hay tareas.")
        for i, tarea in enumerate(self.tareas, 1):
            print(f"\n🔹 Tarea {i}:\n{tarea}")

    def marcar_como_completada(self, nombre):
        for tarea in self.tareas:
            if tarea.nombre.lower() == nombre.lower():
                tarea.marcar_completada()
                print(f"✅ Tarea '{nombre}' marcada como completada.")
                return
        print(f"❌ Tarea '{nombre}' no encontrada.")

    def mostrar_por_prioridad(self, prioridad):
        prioridad = prioridad.lower()
        filtradas = [t for t in self.tareas if t.prioridad == prioridad]
        if not filtradas:
            print(f"⚠️ No hay tareas con prioridad '{prioridad}'.")
        else:
            for tarea in filtradas:
                print(tarea)

    def eliminar_tarea(self, nombre):
        for tarea in self.tareas:
            if tarea.nombre.lower() == nombre.lower():
                self.tareas.remove(tarea)
                print(f"🗑️ Tarea '{nombre}' eliminada.")
                return
        print(f"❌ Tarea '{nombre}' no encontrada.")

# =======================
# Menú de Interacción CLI
# =======================
def menu():
    print("👋 Hola Adrian, bienvenido a tu gestor de tareas.")
    gestor = GestorDeTareas()

    while True:
        print("\n📋 Menú de Gestión de Tareas")
        print("1. Agregar nueva tarea")
        print("2. Mostrar todas las tareas")
        print("3. Marcar tarea como completada")
        print("4. Mostrar tareas por prioridad")
        print("5. Eliminar tarea")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            nombre = input("Nombre de la nueva tarea: ")
            descripcion = input("Descripción: ")
            prioridad = input("Prioridad (alta, media, baja, ninguna): ")
            etiquetas = input("Etiquetas (separadas por comas): ").split(",")
            etiquetas = [et.strip() for et in etiquetas if et.strip()]
            gestor.agregar_tarea(nombre, descripcion, prioridad, etiquetas)

        elif opcion == '2':
            gestor.mostrar_todas()

        elif opcion == '3':
            nombre = input("Nombre de la tarea a marcar como completada: ")
            gestor.marcar_como_completada(nombre)

        elif opcion == '4':
            prioridad = input("Mostrar tareas con prioridad (alta, media, baja, ninguna): ")
            gestor.mostrar_por_prioridad(prioridad)

        elif opcion == '5':
            nombre = input("Nombre de la tarea a eliminar: ")
            gestor.eliminar_tarea(nombre)

        elif opcion == '6':
            print("👋 Hasta luego, Adrian. ¡Buena suerte con tus tareas!")
            break
        else:
            print("❌ Opción no válida. Intenta de nuevo.")

# Ejecutar menú
if __name__ == "__main__":
    menu()
