# # Importación del módulo os
# import os

# # Importación del módulo sys
# import sys

# # Uso del módulo os para obtener el directorio actual
# directorio_actual = os.getcwd()
# print("El directorio actual es:", directorio_actual)

# # Uso del módulo sys para obtener el tamaño máximo de un entero
# tamano_maximo_entero = sys.maxsize
# print("El tamaño máximo de un entero en este sistema es:", tamano_maximo_entero)

# def buscar_archivo(directorio, nombre_archivo):
#     for raiz, dirs, archivos in os.walk(directorio):
#         if nombre_archivo in archivos:
#             return os.path.join(raiz, nombre_archivo)
#     return None