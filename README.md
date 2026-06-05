Editor de Texto en Python con Tkinter
Descripción

Este proyecto consiste en un editor de texto desarrollado en Python utilizando la biblioteca Tkinter para la interfaz gráfica. Permite crear, abrir, editar, guardar y eliminar archivos de texto mediante una interfaz sencilla y fácil de usar.

Características

Abrir archivos de texto.

Guardar cambios en archivos existentes.

Guardar archivos con un nuevo nombre.

Eliminar archivos.

Cambiar el color del texto.

Atajos de teclado para una mayor productividad.

Interfaz gráfica desarrollada con Tkinter.

Estructura del Proyecto

EditorTexto/
├── main.py
└── lib/
    ├── __init__.py
    └── archivo.py
main.py

Contiene la interfaz gráfica del editor de texto y la lógica de interacción con el usuario.

lib/archivo.py

Contiene las funciones encargadas de la gestión de archivos:

abrir_archivo()

guardar_archivo()

editar_contenido()

eliminar_archivo()

Requisitos

Python 3.x

Tkinter (incluido en la mayoría de las instalaciones de Python)

Instalación


Clona el repositorio:

git clone https://github.com/Shao0s/EditorTexto.git

Ingresa al directorio del proyecto:

cd NOMBRE_DEL_REPOSITORIO
Ejecución

Ejecuta el programa con:

python main.py

o

python3 main.py
Atajos de Teclado
Atajo	Acción

Ctrl + O	Abrir archivo


Ctrl + S	Guardar archivo

Ctrl + Shift + S	Guardar como

Ctrl + Delete	Eliminar archivo

Ctrl + C	Cambiar color del texto

Ctrl + Q	Salir

Tecnologías Utilizadas

Python

Tkinter

OS (manejo de archivos)

Desarrollado como proyecto académico para la práctica de programación orientada a objetos, interfaces gráficas y manipulación de archivos en Python.
