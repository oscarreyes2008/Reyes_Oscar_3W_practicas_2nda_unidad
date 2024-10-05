print(" ")#sirve para dejar un espacio a la hora de ejecutar
print("reyes yañez oscar alonso 3_w : pracica de materias")
print(" ")#sirve para dejar un espacio a la hora de ejecutar
materias = ["Pensamiento matemático", "lengua y comunicacion", "Inglés", "ecosistemas", "programacion 2.1", "programacion 2.2"]#te dice que materias estas cursando
print(" ")#sirve para dejar un espacio a la hora de ejecutar

# Crear un diccionario para almacenar las calificaciones
calificaciones = {}
print(" ")#sirve para dejar un espacio a la hora de ejecutar

# Pedir al usuario la calificación de cada materia
for materia in materias:
    calificacion = input(f"Ingrese la calificación para {materia}: ")
    calificaciones[materia] = calificacion
print(" ")#sirve para dejar un espacio a la hora de ejecutar

# Mostrar las calificaciones
print("\nCalificaciones obtenidas:")
for materia, calificacion in calificaciones.items():
    print(f"En {materia} has obtenido {calificacion}.")