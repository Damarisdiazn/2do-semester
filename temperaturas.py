# Programación Orientada a Objetos (POO)

class RegistroClima:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperatura_diaria(self, temperatura):
        """Método para ingresar la temperatura diaria."""
        self.temperaturas.append(temperatura)

    def calcular_promedio_semanal(self):
        """Método para calcular el promedio semanal de temperaturas."""
        if len(self.temperaturas) == 0:
            return 0  # Si no hay temperaturas ingresadas, el promedio es 0 por convención.
        promedio = sum(self.temperaturas) / len(self.temperaturas)
        return promedio


def main():
    print("Ingrese las temperaturas diarias para calcular el promedio semanal.")
    registro = RegistroClima()
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        registro.ingresar_temperatura_diaria(temp)

    promedio_semanal = registro.calcular_promedio_semanal()
    print(f"El promedio semanal de temperaturas es: {promedio_semanal:.2f}")


if __name__ == "__main__":
    main()
