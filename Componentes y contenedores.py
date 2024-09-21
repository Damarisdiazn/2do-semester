import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  # Asegúrate de instalar tkcalendar

class AgendaPersonal:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")

        # Crear contenedores
        self.frame_lista = tk.Frame(self.root)
        self.frame_lista.pack(pady=10)

        self.frame_entrada = tk.Frame(self.root)
        self.frame_entrada.pack(pady=10)

        self.frame_botones = tk.Frame(self.root)
        self.frame_botones.pack(pady=10)

        # Lista de eventos
        self.tree = ttk.Treeview(self.frame_lista, columns=("Fecha", "Hora", "Descripción"), show='headings')
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack()

        # Campos de entrada
        self.label_fecha = tk.Label(self.frame_entrada, text="Fecha:")
        self.label_fecha.grid(row=0, column=0)
        self.fecha_entry = DateEntry(self.frame_entrada)
        self.fecha_entry.grid(row=0, column=1)

        self.label_hora = tk.Label(self.frame_entrada, text="Hora:")
        self.label_hora.grid(row=1, column=0)
        self.hora_entry = tk.Entry(self.frame_entrada)
        self.hora_entry.grid(row=1, column=1)

        self.label_desc = tk.Label(self.frame_entrada, text="Descripción:")
        self.label_desc.grid(row=2, column=0)
        self.desc_entry = tk.Entry(self.frame_entrada)
        self.desc_entry.grid(row=2, column=1)

        # Botones
        self.boton_agregar = tk.Button(self.frame_botones, text="Agregar Evento", command=self.agregar_evento)
        self.boton_agregar.grid(row=0, column=0)

        self.boton_eliminar = tk.Button(self.frame_botones, text="Eliminar Evento Seleccionado", command=self.eliminar_evento)
        self.boton_eliminar.grid(row=0, column=1)

        self.boton_salir = tk.Button(self.frame_botones, text="Salir", command=self.root.quit)
        self.boton_salir.grid(row=0, column=2)

    def agregar_evento(self):
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.desc_entry.get()

        if fecha and hora and descripcion:
            self.tree.insert("", "end", values=(fecha, hora, descripcion))
            self.limpiar_campos()
        else:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")

    def eliminar_evento(self):
        try:
            selected_item = self.tree.selection()[0]
            self.tree.delete(selected_item)
        except IndexError:
            messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar.")

    def limpiar_campos(self):
        self.fecha_entry.set_date('')
        self.hora_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaPersonal(root)
    root.mainloop()