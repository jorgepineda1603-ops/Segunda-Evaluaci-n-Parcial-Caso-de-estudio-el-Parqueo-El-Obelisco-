from vehiculo import Vehiculo

class Pickup(Vehiculo):
    def __init__(self, placa, color, dueno, carga_ton):
        super().__init__(placa, color, dueno)
        self.carga_ton = carga_ton

    def describir(self):
        return f"PICKUP | {super().describir()} | {self.carga_ton} toneladas"

    def calcular_tarifa(self, horas):
        return 15 * horas + 10