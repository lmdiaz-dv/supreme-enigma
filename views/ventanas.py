import tkinter as tk
from tkinter import messagebox
from controllers.controlador import Controlador

class VentanaPrincipal:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Gestión Equipo de Fútbol - Grupo N°6")
        self.ventana.geometry("600x600")
        
        # Crear el controlador
        self.controlador = Controlador()
        
        # Crear el menú
        self._crear_menu()
    
    def _crear_menu(self):
        menu = tk.Menu(self.ventana)
        self.ventana.config(menu=menu)
        
        menu_jugadores = tk.Menu(menu, tearoff=0)
        menu_vista = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Opciones", menu=menu_jugadores)
        menu.add_cascade(label="Ver jugadores", menu=menu_vista)
        
        menu_jugadores.add_command(label="Agregar jugador", command=self.agregar_jugador)
        menu_vista.add_command(label="Mostrar jugadores", command=self.mostrar_jugadores)
        menu_jugadores.add_separator()
        menu_jugadores.add_command(label="Salir", command=self.ventana.quit)
    
    def agregar_jugador(self):
        """Abrir ventana para agregar jugador"""
        VentanaAgregarJugador(self.controlador, self.ventana)
    
    def mostrar_jugadores(self):
        """Mostrar todos los jugadores"""
        jugadores = self.controlador.obtener_jugadores()
        if jugadores:
            VentanaMostrarJugadores(jugadores, self.ventana)
        else:
            messagebox.showinfo("Info", "No hay jugadores registrados")
    
    def ejecutar(self):
        self.ventana.mainloop()


class VentanaAgregarJugador:
    def __init__(self, controlador, parent):
        self.controlador = controlador
        self.ventana = tk.Toplevel(parent)
        self.ventana.title("Agregar Jugador")
        self.ventana.geometry("450x500")
        
        # Campos del formulario (adaptados a tu BD)
        tk.Label(self.ventana, text="Apellido:", font=("Arial", 10)).pack(pady=5)
        self.apellido_entry = tk.Entry(self.ventana, width=30)
        self.apellido_entry.pack(pady=5)
        
        tk.Label(self.ventana, text="Número de Camiseta:", font=("Arial", 10)).pack(pady=5)
        self.numero_entry = tk.Entry(self.ventana, width=30)
        self.numero_entry.pack(pady=5)
        
        tk.Label(self.ventana, text="Posición:", font=("Arial", 10)).pack(pady=5)
        self.posicion_entry = tk.Entry(self.ventana, width=30)
        self.posicion_entry.pack(pady=5)
        
        tk.Label(self.ventana, text="Minutos Jugados:", font=("Arial", 10)).pack(pady=5)
        self.minutos_entry = tk.Entry(self.ventana, width=30)
        self.minutos_entry.pack(pady=5)
        
        tk.Label(self.ventana, text="Goles Marcados:", font=("Arial", 10)).pack(pady=5)
        self.goles_entry = tk.Entry(self.ventana, width=30)
        self.goles_entry.pack(pady=5)
        
        tk.Label(self.ventana, text="Tipo de Jugador:", font=("Arial", 10)).pack(pady=5)
        self.tipo_var = tk.StringVar(value="campo")
        tk.Radiobutton(self.ventana, text="Arquero", variable=self.tipo_var, value="arquero").pack()
        tk.Radiobutton(self.ventana, text="Campo", variable=self.tipo_var, value="campo").pack()
        
        # Botón guardar
        tk.Button(self.ventana, text="Guardar Jugador", command=self.guardar_jugador, 
                  bg="green", fg="white", font=("Arial", 10)).pack(pady=20)
    
    def guardar_jugador(self):
        """Guardar el jugador en la base de datos"""
        apellido = self.apellido_entry.get()
        numero_camiseta = self.numero_entry.get()
        posicion = self.posicion_entry.get()
        minutos_jugados = self.minutos_entry.get()
        goles_marcados = self.goles_entry.get()
        tipo_jugador = self.tipo_var.get()
        
        # Validar campos
        if not all([apellido, numero_camiseta, posicion, minutos_jugados, goles_marcados]):
            messagebox.showerror("Error", "Por favor complete todos los campos")
            return
        
        # Validar que número, minutos y goles sean números
        try:
            numero_camiseta = int(numero_camiseta)
            minutos_jugados = int(minutos_jugados)
            goles_marcados = int(goles_marcados)
        except ValueError:
            messagebox.showerror("Error", "Número, minutos y goles deben ser valores numéricos")
            return
        
        # Guardar en la base de datos
        self.controlador.guardar_jugador(apellido, numero_camiseta, posicion, 
                                         minutos_jugados, goles_marcados, tipo_jugador)
        self.ventana.destroy()


class VentanaMostrarJugadores:
    def __init__(self, jugadores, parent):
        self.ventana = tk.Toplevel(parent)
        self.ventana.title("Lista de Jugadores")
        self.ventana.geometry("600x400")
        
        # Crear frame con scrollbar
        frame = tk.Frame(self.ventana)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        lista_texto = tk.Text(frame, height=20, width=70, yscrollcommand=scrollbar.set)
        lista_texto.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=lista_texto.yview)
        
        # Mostrar jugadores
        for jugador in jugadores:
            lista_texto.insert(tk.END, f"ID: {jugador.get('id')}\n")
            lista_texto.insert(tk.END, f"Apellido: {jugador.get('apellido')}\n")
            lista_texto.insert(tk.END, f"N° Camiseta: {jugador.get('numero_camiseta')}\n")
            lista_texto.insert(tk.END, f"Posición: {jugador.get('posicion')}\n")
            lista_texto.insert(tk.END, f"Minutos: {jugador.get('minutos_jugados')}\n")
            lista_texto.insert(tk.END, f"Goles: {jugador.get('goles_marcados')}\n")
            lista_texto.insert(tk.END, f"Tipo: {jugador.get('tipo_jugador')}\n")
            lista_texto.insert(tk.END, "-" * 50 + "\n")
        
        lista_texto.config(state=tk.DISABLED)
        
        tk.Button(self.ventana, text="Cerrar", command=self.ventana.destroy).pack(pady=10)