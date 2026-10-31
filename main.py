from parqueo import Parqueo
from cliente import Cliente
from moto import Moto
from carro import Carro
from pickup import Pickup

def pedir_entero(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto.isdigit():
            return int(texto)
        print("⚠️ Por favor ingresa un número válido")

def main():
    parqueo = Parqueo("El Obelisco", 6)

    while True:
        print("\n" + "="*35)
        print("Parqueo El Obelisco")
        print("1. Registrar entrada")
        print("2. Registrar salida")
        print("3. Ver vehículos estacionados")
        print("4. Buscar vehículo por placa")
        print("5. Ver resumen del día")
        print("6. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            tipo = input("Tipo (M/C/P): ").strip().upper()
            placa = input("Placa: ").strip()
            color = input("Color: ").strip()
            nombre = input("Nombre del dueño: ").strip()
            telefono = input("Teléfono del dueño: ").strip()
            hora = pedir_entero("Hora de entrada: ")

            dueno = Cliente(nombre, telefono)
            vehiculo = None

            if tipo == "M":
                cilindrada = pedir_entero("Cilindrada: ")
                vehiculo = Moto(placa, color, dueno, cilindrada)
            elif tipo == "C":
                puertas = pedir_entero("Número de puertas: ")
                vehiculo = Carro(placa, color, dueno, puertas)
            elif tipo == "P":
                carga = pedir_entero("Carga en toneladas: ")
                vehiculo = Pickup(placa, color, dueno, carga)
            else:
                print("⚠️ Tipo inválido. Usa M, C o P")
                continue

            parqueo.registrar_entrada(vehiculo, hora)

        elif opcion == "2":
            placa = input("Placa: ").strip()
            hora = pedir_entero("Hora de salida: ")
            parqueo.registrar_salida(placa, hora)

        elif opcion == "3":
            print("\n--- Vehículos Estacionados ---")
            parqueo.listar()

        elif opcion == "4":
            placa = input("Placa a buscar: ").strip()
            v = parqueo.buscar(placa)
            if v:
                print(v.describir())
            else:
                print("No se encontró ningún vehículo con esa placa")

        elif opcion == "5":
            print("\n--- Resumen del Día ---")
            print(f"Espacios libres: {parqueo.espacios_libres()} de {parqueo.capacidad}")
            print(f"Total recaudado: Q{parqueo.total_recaudado}")

        elif opcion == "6":
            print("👋 Saliendo del sistema...")
            break

        else:
            print("⚠️ Opción no válida")

if __name__ == "__main__":
    main()