import os

#Abre un archivo y devuelve su contenido
def abrir_archivo(ruta):
    try:
        with open(ruta, 'r') as archivo:
            return archivo.read()
    except FileNotFoundError:
        print("El archivo no existe.")
        return None

#Guarda contenido en un archivo
def guardar_archivo(ruta, contenido):
    with open(ruta, 'w') as archivo:
        archivo.write(contenido)

#Edita el contenido de un archivo
def editar_contenido(ruta, nuevo_contenido):
    guardar_archivo(ruta, nuevo_contenido)

#Elimina un archivo
def eliminar_archivo(ruta):
    try:
        os.remove(ruta)
        print("Archivo eliminado con éxito.")
    except FileNotFoundError:
        print("El archivo no existe.")