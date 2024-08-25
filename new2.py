
import os

class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        """Carga los productos desde el archivo al iniciar el programa."""
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, 'r') as file:
                    for linea in file:
                        nombre, cantidad = linea.strip().split(',')
                        self.productos[nombre] = int(cantidad)
            except FileNotFoundError:
                print("El archivo no se encontró. Se creará uno nuevo.")
            except Exception as e:
                print(f"Error al cargar el inventario: {e}")

    def guardar_inventario(self):
        """Guarda los productos en el archivo."""
        try:
            with open(self.archivo, 'w') as file:
                for nombre, cantidad in self.productos.items():
                    file.write(f"{nombre},{cantidad}\n")
            print("Inventario guardado exitosamente.")
        except PermissionError:
            print("Error: No se tienen permisos para escribir en el archivo.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def agregar_producto(self, nombre, cantidad):
        """Agrega un producto al inventario y lo guarda en el archivo."""
        if nombre in self.productos:
            self.productos[nombre] += cantidad
        else:
            self.productos[nombre] = cantidad
        self.guardar_inventario()

    def eliminar_producto(self, nombre):
        """Elimina un producto del inventario y actualiza el archivo."""
        if nombre in self.productos:
            del self.productos[nombre]
            self.guardar_inventario()
        else:
            print("El producto no existe en el inventario.")

    def actualizar_producto(self, nombre, cantidad):
        """Actualiza la cantidad de un producto en el inventario."""
        if nombre in self.productos:
            self.productos[nombre] = cantidad
            self.guardar_inventario()
        else:
            print("El producto no existe en el inventario.")

def main():
    inventario = Inventario()

    while True:
        print("\nOpciones:")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            inventario.agregar_producto(nombre, cantidad)
        elif opcion == '2':
            nombre = input("Nombre del producto a eliminar: ")
            inventario.eliminar_producto(nombre)
        elif opcion == '3':
            nombre = input("Nombre del producto a actualizar: ")
            cantidad = int(input("Nueva cantidad: "))
            inventario.actualizar_producto(nombre, cantidad)
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
