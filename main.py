import tkinter as tk
from tkinter import messagebox, simpledialog

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

class Equipo:
    def __init__(self):
        self.jugadores = []

    def agregar(self, jugador):
        self.jugadores.append(jugador)

    def mostrar_equipo(self):
        return "\n".join(j.mostrar_jugador() for j in self.jugadores)


miEquipo = Equipo()

def agregar_jugador():
    posiciones = ["arquero", "defensor", "mediocampista", "delantero"]
    posiciones_de_campo = ["defensor", "mediocampista", "delantero"]
    try:
        numero = int(simpledialog.askstring("Info", "Número de camiseta"))
        apellido = simpledialog.askstring("Info", "Apellido")
        posicion = simpledialog.askstring("Info", "Tipo (arquero / defensor / mediocampista / delantero )")
        while posicion not in posiciones:
            posicion = simpledialog.askstring("Tipo incorrecto",
                                              "Tipo (arquero / defensor / mediocampista / delantero )")
        minutos_jugados = int(simpledialog.askstring("Info", "Minutos jugados"))

        if posicion == "arquero":
            jugador = Arquero(numero, apellido, minutos_jugados)

        elif posicion in posiciones_de_campo:
            goles = int(simpledialog.askstring("Info", "Goles"))
            jugador = JugadorCampo(numero, apellido, posicion, minutos_jugados, goles)

        else:
            messagebox.showerror("Error", "Tipo inválido")
            return

        miEquipo.agregar(jugador)
        messagebox.showinfo("Éxito", "Jugador agregado correctamente")

    except:
        messagebox.showerror("Error", "Datos inválidos")


def mostrar_jugadores():
    datos = miEquipo.mostrar_equipo()
    if datos:
        messagebox.showinfo("Jugadores", datos)
    else:
        messagebox.showinfo("Jugadores", "No hay jugadores cargados")

ventana = tk.Tk()
ventana.title("Gestión Equipo de Fútbol")
ventana.geometry("400x300")

menu = tk.Menu(ventana)
ventana.config(menu=menu)

menu_jugadores = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Opciones", menu=menu_jugadores)

menu_jugadores.add_command(label="Agregar jugador", command=agregar_jugador)
menu_jugadores.add_command(label="Mostrar jugadores", command=mostrar_jugadores)
menu_jugadores.add_separator()
menu_jugadores.add_command(label="Salir", command=ventana.quit)

ventana.mainloop()