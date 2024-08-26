class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto  # ID único
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def obtener_id(self):
        return self.id_producto

    def obtener_nombre(self):
        return self.nombre

    def obtener_cantidad(self):
        return self.cantidad

    def obtener_precio(self):
        return self.precio

    def establecer_cantidad(self, cantidad):
        self.cantidad = cantidad

    def establecer_precio(self, precio):
        self.precio = precio
class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario para almacenar productos

    def añadir_producto(self, producto):
        self.productos[producto.obtener_id()] = producto

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].establecer_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].establecer_precio(precio)

    def buscar_producto(self, nombre):
        return [producto for producto in self.productos.values() if producto.obtener_nombre() == nombre]

    def mostrar_productos(self):
        for producto in self.productos.values():
            print(f"ID: {producto.obtener_id()}, Nombre: {producto.obtener_nombre()}, Cantidad: {producto.obtener_cantidad()}, Precio: {producto.obtener_precio()}")
import json

def guardar_inventario(inventario, archivo):
    with open(archivo, 'w') as f:
        json.dump({id: vars(producto) for id, producto in inventario.productos.items()}, f)

def cargar_inventario(archivo):
    inventario = Inventario()
    try:
        with open(archivo, 'r') as f:
            productos = json.load(f)
            for id, datos in productos.items():
                producto = Producto(id, datos['nombre'], datos['cantidad'], datos['precio'])
                inventario.añadir_producto(producto)
    except FileNotFoundError:
        print("Archivo no encontrado. Se creará un nuevo inventario.")
    return inventario
def menu():
    inventario = cargar_inventario('inventario.json')
    while True:
        print("\nMenu:")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == '2':
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == '3':
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío para no cambiar): ")
            precio = input("Nuevo precio (dejar vacío para no cambiar): ")
            inventario.actualizar_producto(id_producto, int(cantidad) if cantidad else None, float(precio) if precio else None)

        elif opcion == '4':
            nombre = input("Nombre del producto a buscar: ")
            productos_encontrados = inventario.buscar_producto(nombre)
            for producto in productos_encontrados:
                print(f"ID: {producto.obtener_id()}, Nombre: {producto.obtener_nombre()}, Cantidad: {producto.obtener_cantidad()}, Precio: {producto.obtener_precio()}")

        elif opcion == '5':
            inventario.mostrar_productos()

        elif opcion == '6':
            guardar_inventario(inventario, 'inventario.json')

        elif opcion == '7':
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()