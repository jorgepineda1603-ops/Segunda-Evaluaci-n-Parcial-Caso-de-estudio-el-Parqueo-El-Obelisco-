class Parqueo:
    def __init__(self, nombre, capacidad):
        self.nombre = nombre
        self.capacidad = capacidad
        self.estacionados = []
        self.total_recaudado = 0

    def espacios_libres(self):
        return self.capacidad - len(self.estacionados)

    def buscar(self, placa):
        placa_buscar = placa.upper()
        for v in self.estacionados:
            if v.placa == placa_buscar:
                return v
        return None

    def registrar_entrada(self, vehiculo, hora):
        # ART. 2 — Horario
        if not (6 <= hora <= 22):
            print("ART. 2 · Fuera de horario (6–22 hrs)")
            return False
        # ART. 1 — Capacidad
        if len(self.estacionados) >= self.capacidad:
            print("ART. 1 · Parqueo lleno")
            return False
        # ART. 3 — Placa única
        if self.buscar(vehiculo.placa) is not None:
            print("ART. 3 · Placa ya registrada")
            return False

        vehiculo.hora_entrada = hora
        self.estacionados.append(vehiculo)
        print(f"✅ Entrada registrada: {vehiculo.placa} a las {hora}:00")
        return True

    def registrar_salida(self, placa, hora_salida):
        v = self.buscar(placa)
        if v is None:
            print("Placa no encontrada")
            return 0
        # ART. 2 — Horario
        if not (6 <= hora_salida <= 22):
            print("ART. 2 · Fuera de horario (6–22 hrs)")
            return 0
        # ART. 4 — Hora de salida válida
        if hora_salida < v.hora_entrada:
            print("ART. 4 · Hora de salida anterior a la entrada")
            return 0

        horas = hora_salida - v.hora_entrada
        if horas == 0:
            horas = 1  # cobro mínimo
        monto = v.calcular_tarifa(horas)
        self.total_recaudado += monto
        self.estacionados.remove(v)
        print(f"🚗 Salida: {v.placa} — {horas} hora(s) — A cobrar: Q{monto}")
        return monto

    def listar(self):
        if not self.estacionados:
            print("No hay vehículos estacionados")
            return
        for v in self.estacionados:
            print(f"{v.describir()} — Entrada: {v.hora_entrada}:00")