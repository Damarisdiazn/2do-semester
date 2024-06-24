class Producto:
    def __init__(self, nombre, descripcion, precio, inventario):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.inventario = inventario

    def mostrar_informacion(self):
        return f"{self.nombre}: {self.descripcion}. Precio: ${self.precio}. Disponibles: {self.inventario}"

    def restar_inventario(self, cantidad):
        if cantidad <= self.inventario:
            self.inventario -= cantidad
            return True
        else:
            return False

    def agregar_inventario(self, cantidad):
        self.inventario += cantidad


class Vendedor:
    def __init__(self, nombre):
        self.nombre = nombre

    def consultar_producto(self, producto):
        return f"Información proporcionada por {self.nombre}: {producto.mostrar_informacion()}"


class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre

    def consultar_precio(self, producto):
        return f"{producto.nombre}: Precio actual ${producto.precio}"

    def realizar_compra(self, producto, cantidad):
        if producto.restar_inventario(cantidad):
            return f"Compra realizada: {cantidad} unidades de {producto.nombre}. Total: ${producto.precio * cantidad}"
        else:
            return "Lo sentimos, no hay suficientes unidades disponibles."

# Creamos algunos productos
telefono = Producto("iPhone 12", "Teléfono inteligente de Apple", 1000, 10)
laptop = Producto("MacBook Pro", "Laptop de Apple", 2000, 5)

# Creamos un vendedor y un cliente
vendedor1 = Vendedor("Ana")
cliente1 = Cliente("Juan")

# El cliente consulta el precio de un producto
print(cliente1.consultar_precio(telefono))

# El cliente realiza una compra
print(cliente1.realizar_compra(telefono, 2))

# El vendedor consulta información sobre un producto
print(vendedor1.consultar_producto(laptop))

# Mostramos el inventario después de la compra
print(f"Inventario después de la compra de {telefono.nombre}: {telefono.inventario} unidades")
