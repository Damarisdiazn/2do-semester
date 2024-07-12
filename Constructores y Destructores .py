class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print(f'Se ha creado una nueva instancia de Persona: {self.nombre}')

    def __del__(self):
        print(f'Se está eliminando la instancia de Persona: {self.nombre}')


class Archivo:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.abrir_archivo()
        print(f'Se ha creado una nueva instancia de Archivo: {self.nombre_archivo}')

    def abrir_archivo(self):
        print(f'Abriendo el archivo: {self.nombre_archivo}')

    def cerrar_archivo(self):
        print(f'Cerrando el archivo: {self.nombre_archivo}')

    def __del__(self):
        self.cerrar_archivo()
        print(f'Se está eliminando la instancia de Archivo: {self.nombre_archivo}')


# Ejemplo de uso de las clases
persona1 = Persona("Juan", 30)
archivo1 = Archivo("documento.txt")

# Simulación de eliminación de instancias
del persona1
del archivo1