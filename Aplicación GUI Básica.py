import tkinter as tk
from tkinter import messagebox

# Función para agregar información a la lista
def agregar_info():
    info = campo_texto.get()
    if info:
        lista_datos.insert(tk.END, info)
        campo_texto.delete(0, tk.END)  # Limpiar el campo de texto
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingrese información.")

# Función para limpiar la lista
def limpiar_lista():
    lista_datos.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI Básica")

# Crear componentes
etiqueta = tk.Label(ventana, text="Ingrese información:")
etiqueta.pack(pady=10)

campo_texto = tk.Entry(ventana, width=30)
campo_texto.pack(pady=5)

boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_info)
boton_agregar.pack(pady=5)

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
boton_limpiar.pack(pady=5)

lista_datos = tk.Listbox(ventana, width=50, height=10)
lista_datos.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()