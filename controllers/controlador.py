from tkinter import messagebox, simpledialog
from models.jugador import JugadorCampo, Arquero
from models.equipo import Equipo

class ControladorEquipo:
    def __init__(self):
        self.miEquipo = Equipo()
    
    def agregar_jugador(self):
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

            self.miEquipo.agregar(jugador)
            messagebox.showinfo("Éxito", "Jugador agregado correctamente")

        except:
            messagebox.showerror("Error", "Datos inválidos")
    
    def mostrar_jugadores(self):
        datos = self.miEquipo.mostrar_equipo()
        if datos:
            messagebox.showinfo("Jugadores", datos)
        else:
            messagebox.showinfo("Jugadores", "No hay jugadores cargados")