from vehiculo import Vehiculo

class Carro(Vehiculo):
    def __init__(self, placa, color, dueno, puertas):
        super().__init__(placa, color, dueno)
        self.puertas = puertas

    def describir(self):
        return f"CARRO | {super().describir()} | {self.puertas} puertas"

    def calcular_tarifa(self, horas):
        monto = 10 * horas
        return monto if monto <= 60 else 60