print(" ")#sirve para dejar un espacio a la hora de ejecutar
print("reyes yañez oscar alonso 3_w : pracica de loteria")
print(" ")#sirve para dejar un espacio a la hora de ejecutar
numeros_triunfadores = []
print(" ")#sirve para dejar un espacio a la hora de ejecutar
# Preguntar al usuario cuántos números quiere ingresar
cantidad = int(input("¿Cuántos números triunfadores desea ingresar? "))#te pide que coloques la cantidad de numeros que participaran
print(" ")#sirve para dejar un espacio a la hora de ejecutar
# Llenar la lista con los números ingresados por el usuario
for i in range(cantidad):
    numero = int(input(f"Ingrese el número triunfador #{i + 1}: "))
    numeros_triunfadores.append(numero)
print(" ")#sirve para dejar un espacio a la hora de ejecutar
# Ordenar la lista de menor a mayor
numeros_triunfadores.sort()#realiza el sorteo del numero ganador
print(" ")#sirve para dejar un espacio a la hora de ejecutar
# Mostrar los números triunfadores en pantalla
print("\nNúmeros triunfadores (de menor a mayor):")
print(numeros_triunfadores)
print(" ")#sirve para dejar un espacio a la hora de ejecutar