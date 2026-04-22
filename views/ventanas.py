import tkinter as tk
from controllers.controlador import ControladorEquipo

class VentanaPrincipal:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Gestión Equipo de Fútbol - Grupo N°6")
        self.ventana.geometry("600x600")
        
        # Crear el controlador
        self.controlador = ControladorEquipo()
        
        # Crear el menú
        self._crear_menu()
    
    def _crear_menu(self):
        menu = tk.Menu(self.ventana)
        self.ventana.config(menu=menu)
        
        menu_jugadores = tk.Menu(menu, tearoff=0)
        menu_vista = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Opciones", menu=menu_jugadores)
        menu.add_cascade(label="Ver jugadores", menu=menu_vista)
        
        menu_jugadores.add_command(label="Agregar jugador", command=self.controlador.agregar_jugador)
        menu_vista.add_command(label="Mostrar jugadores", command=self.controlador.mostrar_jugadores)
        menu_jugadores.add_separator()
        menu_jugadores.add_command(label="Salir", command=self.ventana.quit)
    
    def ejecutar(self):
        self.ventana.mainloop()