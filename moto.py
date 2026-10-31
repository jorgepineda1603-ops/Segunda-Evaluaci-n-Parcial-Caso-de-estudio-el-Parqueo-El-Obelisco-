from vehiculo import Vehiculo

class Moto(Vehiculo):
    def __init__(self, placa, color, dueno, cilindrada):
        super().__init__(placa, color, dueno)
        self.cilindrada = cilindrada

    def describir(self):
        return f"MOTO | {super().describir()} | {self.cilindrada} cc"

    def calcular_tarifa(self, horas):
        return 5 * horas