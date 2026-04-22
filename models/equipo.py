class Equipo:
    def __init__(self):
        self.jugadores = []

    def agregar(self, jugador):
        self.jugadores.append(jugador)

    def mostrar_equipo(self):
        return "\n".join(j.mostrar_jugador() for j in self.jugadores)