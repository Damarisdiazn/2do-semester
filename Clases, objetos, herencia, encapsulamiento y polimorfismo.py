# Definición de la clase base "Vehiculo"
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def encender(self):
        print("El vehículo está encendido")


# Definición de la clase derivada "Coche" que hereda de Vehiculo
class Coche(Vehiculo):
    def __init__(self, marca, modelo, color):
        super().__init__(marca, modelo)
        self.color = color

    def encender(self):
        print("El coche está encendido")

    def acelerar(self):
        print("El coche está acelerando")


# Creación de instancias y demostración de herencia, encapsulación y polimorfismo
if __name__ == "__main__":
    # Crear instancia de la clase derivada "Coche"
    mi_coche = Coche("Toyota", "Corolla", "Rojo")

    # Acceder a atributos de la clase base
    print(f"Marca: {mi_coche.marca}")
    print(f"Modelo: {mi_coche.modelo}")

    # Acceder a atributos de la clase derivada
    print(f"Color: {mi_coche.color}")

    # Llamar al método de la clase base
    mi_coche.encender()

    # Llamar al método de la clase derivada
    mi_coche.acelerar()