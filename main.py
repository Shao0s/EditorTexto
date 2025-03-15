import tkinter as tk
from tkinter import filedialog,colorchooser
from lib.archivo import *

class EditorTexto:
    def __init__(self, Ventana):
        self.Ventana = Ventana                     # Es la ventana principal del editor.
        self.ruta = None                           #Almacena la ruta del archivo actualmente abierto.
        self.texto = tk.Text(self.Ventana)         #muestra el contenido del archivo.
        self.texto.pack(fill='both', expand=1)

        # Menú superior
        menubar = tk.Menu(self.Ventana)
        self.Ventana.config(menu=menubar)

        #Menu archivo
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Abrir", accelerator="ctrl+O", command=self.abrir_archivo)
        filemenu.add_command(label="Guardar",accelerator="Ctrl+S",command=self.guardar_archivo)
        filemenu.add_command(label="Guardar como", accelerator="Ctrl+Shift+S",command=self.guardar_como)
        filemenu.add_command(label="Eliminar", accelerator="Ctrl+Del",command=self.eliminar_archivo)
        filemenu.add_separator()
        filemenu.add_command(label="Salir", accelerator="Ctrl+Q",command=self.Ventana.quit)
        menubar.add_cascade(label="Archivo", menu=filemenu)

        # Menú Editar
        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Cambiar color de texto", accelerator="Ctrl+C",command=self.cambiar_color)
        menubar.add_cascade(label="Editar", menu=edit_menu)

        # Configurar los atajos de teclado
        self.Ventana.bind_all("<Control-o>", lambda e: self.abrir_archivo())
        self.Ventana.bind_all("<Control-s>", lambda e: self.guardar_archivo())
        self.Ventana.bind_all("<Control-Shift-s>", lambda e: self.guardar_como())
        self.Ventana.bind_all("<Control-Delete>", lambda e: self.eliminar_archivo())
        self.Ventana.bind_all("<Control-q>", lambda e: self.Ventana.quit())
        self.Ventana.bind_all("<Control-c>", lambda e: self.cambiar_color())

        #Funciones
    def abrir_archivo(self):
        self.ruta = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("Todos los archivos", "*.*"), ("Archivos de texto", "*.txt")]
        )
        if self.ruta:
            contenido = abrir_archivo(self.ruta)
            self.texto.delete(1.0, tk.END)
            self.texto.insert(tk.END, contenido)

    def guardar_archivo(self):
        if self.ruta:
            contenido = self.texto.get(1.0, tk.END)
            guardar_archivo(self.ruta, contenido)
        else:
            self.guardar_como()

    def guardar_como(self):
        self.ruta = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Todos los archivos", "*.*"), ("Archivos de texto", "*.txt")]
        )
        if self.ruta:
            contenido = self.texto.get(1.0, tk.END)
            guardar_archivo(self.ruta, contenido)

    def eliminar_archivo(self):
        if self.ruta:
            eliminar_archivo(self.ruta)
            self.ruta = None
            self.texto.delete(1.0, tk.END)
        else:
            print("No hay archivo seleccionado.")


    def cambiar_color(self):
        color = colorchooser.askcolor(title="Seleccione un color")[1]
        if color:
            self.texto.config(fg=color)

#Inicialización del Editor
#se crea una instancia de la clase EditorTexto
if __name__ == "__main__":
    Ventana = tk.Tk()
    Ventana.title("Editor de Texto")
    app = EditorTexto(Ventana)
    Ventana.mainloop()