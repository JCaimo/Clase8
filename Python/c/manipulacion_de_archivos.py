# Crear y escribir en un archivo
# with open("archivo.txt", "w") as archivo:
#     archivo.write("Hola, este es un archivo de ejemplo.\n")
#     archivo.write("Estamos escribiendo múltiples líneas en el archivo.\n")

# # Leer el contenido de un archivo
# with open("archivo.txt", "r") as archivo:
#     contenido = archivo.read()
#     print("Contenido del archivo:")
#     print(contenido)

# # Manipulación de texto: contar palabras en el archivo
# with open("archivo.txt", "r") as archivo:
#     lineas = archivo.readlines()
#     contador_palabras = 0
#     for linea in lineas:
#         palabras = linea.split()  # Divide la línea en palabras
#         contador_palabras += len(palabras)  # Cuenta el número de palabras

# print("Numero total de palabras en el archivo:", contador_palabras)
