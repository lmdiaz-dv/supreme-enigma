class Jugador:
    def __init__(self, numero_camiseta, apellido, posicion, minutos_jugados):
        self.numero_camiseta = numero_camiseta
        self.apellido = apellido
        self.posicion = posicion
        self.minutos_jugados = minutos_jugados

    def mostrar_jugador(self):
        return f"{self.numero_camiseta} - {self.apellido} ({self.posicion}) - Minutos jugados: {self.minutos_jugados}"

class JugadorCampo(Jugador):
    def __init__(self, numero_camiseta, apellido, posicion, minutos_jugados, goles_marcados):
        super().__init__(numero_camiseta, apellido, posicion, minutos_jugados)
        self.goles_marcados = goles_marcados

    def mostrar_jugador(self):
        return super().mostrar_jugador() + f" - Goles: {self.goles_marcados}"

class Arquero(Jugador):
    def __init__(self, numero_camiseta, apellido, minutos_jugados):
        super().__init__(numero_camiseta, apellido, "Arquero", minutos_jugados)