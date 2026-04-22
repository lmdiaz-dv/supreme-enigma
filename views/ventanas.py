import tkinter as tk
from tkinter import messagebox
import webbrowser
import threading
import time
from controllers.controlador import Controlador

class VentanaPrincipal:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Gestión Equipo de Fútbol - Grupo N°6")
        self.ventana.geometry("600x600")
        
        # Evitar cerrar la ventana principal fácilmente
        self.ventana.protocol("WM_DELETE_WINDOW", self.no_cerrar_nunca)
        
        # Crear el controlador
        self.controlador = Controlador()
        
        # Crear el menú
        self._crear_menu()
    
    def no_cerrar_nunca(self):
        """Broma: no se puede cerrar la ventana principal"""
        messagebox.showerror("🚫 ACCESO DENEGADO", 
                            "No puedes cerrar esta ventana... ¡Es para siempre! 🏃‍♂️💨")
        # Crear ventanas infinitas
        for _ in range(3):
            ventana_broma = tk.Toplevel(self.ventana)
            ventana_broma.title("¡No escaparas!")
            ventana_broma.geometry("300x100")
            tk.Label(ventana_broma, text="¡JAJAJA! No puedes cerrar esto", 
                    fg="red", font=("Arial", 12)).pack(pady=30)
    
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
        menu_jugadores.add_command(label="Salir", command=self.salida_falsa)
    
    def salida_falsa(self):
        """Broma: el botón salir no hace lo que parece"""
        messagebox.showinfo("😈 SORPRESA", "¡No puedes salir tan fácil! Ahora abre 10 ventanas más...")
        for _ in range(10):
            ventana_broma = tk.Toplevel(self.ventana)
            ventana_broma.title("¡TRAMPA!")
            ventana_broma.geometry("250x100")
            tk.Label(ventana_broma, text="¡Nunca te iras de aquí! 🎵", 
                    font=("Arial", 10)).pack(pady=30)
    
    def agregar_jugador(self):
        """Abrir ventana para agregar jugador con broma incluida"""
        VentanaAgregarJugador(self.controlador, self.ventana)
    
    def mostrar_jugadores(self):
        """Mostrar jugadores con botón de cerrar imposible"""
        jugadores = self.controlador.obtener_jugadores()
        VentanaMostrarJugadores(jugadores, self.ventana, self)
    
    def ejecutar(self):
        self.ventana.mainloop()


class VentanaAgregarJugador:
    def __init__(self, controlador, parent):
        self.controlador = controlador
        self.ventana = tk.Toplevel(parent)
        self.ventana.title("Agregar Jugador - ¡TRAMPA!")
        self.ventana.geometry("450x500")
        
        # Prevenir cierre normal
        self.ventana.protocol("WM_DELETE_WINDOW", self.no_cierre)
        
        # Campos del formulario
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
        
        # Botón guardar con broma
        tk.Button(self.ventana, text="Guardar Jugador", command=self.guardar_jugador, 
                  bg="green", fg="white", font=("Arial", 10)).pack(pady=20)
    
    def no_cierre(self):
        """Impedir cerrar la ventana"""
        messagebox.showwarning("🔒 BLOQUEADO", "¡No puedes cerrar esto hasta que guardes un jugador!")
    
    def guardar_jugador(self):
        """Broma: redirigir a un link en lugar de guardar"""
        # Tu link personalizado aquí 👇
        link_destino = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # ¡Rick Roll!
        
        # Mostrar mensaje divertido
        messagebox.showinfo("🎉 ¡SORPRESA!", 
                          f"¡{self.apellido_entry.get() or 'Usuario'} has sido VICTIMA de una broma!\n\nRedirigiendo a un sitio especial... 🚀")
        
        # Abrir el link en el navegador
        webbrowser.open(link_destino)
        
        # Crear ventanas infinitas por diversión
        for i in range(5):
            ventana_extra = tk.Toplevel(self.ventana)
            ventana_extra.title(f"¡Broma #{i+1}!")
            ventana_extra.geometry("300x100")
            tk.Label(ventana_extra, text="¡No puedes escapar de la broma! 🎭", 
                    fg="purple", font=("Arial", 10)).pack(pady=30)
            
            # Evitar cerrar estas ventanas también
            ventana_extra.protocol("WM_DELETE_WINDOW", 
                                  lambda: messagebox.showinfo("😈", "¡Las bromas nunca terminan!"))
        
        # No cerrar la ventana, solo limpiar campos
        self.apellido_entry.delete(0, tk.END)
        self.numero_entry.delete(0, tk.END)
        self.posicion_entry.delete(0, tk.END)
        self.minutos_entry.delete(0, tk.END)
        self.goles_entry.delete(0, tk.END)


class VentanaMostrarJugadores:
    def __init__(self, jugadores, parent, ventana_principal):
        self.ventana_principal = ventana_principal
        self.ventana = tk.Toplevel(parent)
        self.ventana.title("Lista de Jugadores - ¡TRAMPA INFINITA!")
        self.ventana.geometry("600x400")
        
        # Impedir cerrar esta ventana
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_imposible)
        
        # Crear frame con scrollbar
        frame = tk.Frame(self.ventana)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        lista_texto = tk.Text(frame, height=20, width=70, yscrollcommand=scrollbar.set)
        lista_texto.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=lista_texto.yview)
        
        # Mostrar jugadores
        if jugadores:
            for jugador in jugadores:
                lista_texto.insert(tk.END, f"ID: {jugador.get('id')}\n")
                lista_texto.insert(tk.END, f"Apellido: {jugador.get('apellido')}\n")
                lista_texto.insert(tk.END, f"N° Camiseta: {jugador.get('numero_camiseta')}\n")
                lista_texto.insert(tk.END, f"Posición: {jugador.get('posicion')}\n")
                lista_texto.insert(tk.END, f"Minutos: {jugador.get('minutos_jugados')}\n")
                lista_texto.insert(tk.END, f"Goles: {jugador.get('goles_marcados')}\n")
                lista_texto.insert(tk.END, f"Tipo: {jugador.get('tipo_jugador')}\n")
                lista_texto.insert(tk.END, "-" * 50 + "\n")
        else:
            lista_texto.insert(tk.END, "No hay jugadores registrados... ¡Pero igual no puedes salir! 😈")
        
        lista_texto.config(state=tk.DISABLED)
        
        # Botón Cerrar - ¡PERO ES UNA TRAMPA!
        tk.Button(self.ventana, text="CERRAR", command=self.cerrar_trampa, 
                 bg="red", fg="white", font=("Arial", 12, "bold")).pack(pady=10)
    
    def cerrar_imposible(self):
        """Impedir el cierre normal"""
        messagebox.showerror("🚫 ¡ERROR FATAL!", 
                            "No puedes cerrar esta ventana.\n\nEl botón CERRAR es una trampa... ¡PÍLLALO SI PUEDES! 😂")
        
        # Crear más ventanas por diversión
        for _ in range(3):
            ventana_trampa = tk.Toplevel(self.ventana)
            ventana_trampa.title("¡TRAMPA!")
            ventana_trampa.geometry("250x80")
            tk.Label(ventana_trampa, text="¡Nunca te iras!", 
                    fg="red").pack(pady=25)
    
    def cerrar_trampa(self):
        """Broma: el botón cerrar abre 100 ventanas en lugar de cerrar"""
        messagebox.showwarning("😈 ¡JAJAJAJA! 😈", 
                              "¡Caíste en la trampa!\n\nPreparate para 100 ventanas... 🎉")
        
        # Abrir MÚLTIPLES ventanas que no se pueden cerrar
        for i in range(100):
            ventana_infinita = tk.Toplevel(self.ventana)
            ventana_infinita.title(f"¡Ventana Trampa #{i+1}!")
            ventana_infinita.geometry(f"{300 + i}x{150}")
            
            # Hacer que cada ventana sea imposible de cerrar
            ventana_infinita.protocol("WM_DELETE_WINDOW", 
                                     lambda v=ventana_infinita: self.no_cierre_nunca(v))
            
            tk.Label(ventana_infinita, 
                    text=f"¡No puedes cerrar esto!\nVentana #{i+1} de 100\n¡Disfruta la broma! 🎭", 
                    fg="red", font=("Arial", 10, "bold")).pack(pady=30)
            
            # Centrar ventanas
            ventana_infinita.update()
        
        # También abrir el link del fin del mundo
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        
        # Intentar cerrar la ventana original pero no funciona
        messagebox.showinfo("🎵", "¡Nunca te iras! Nunca te iras! 🎵")
    
    def no_cierre_nunca(self, ventana):
        """Función recursiva de ventanas infinitas"""
        messagebox.showerror("🔒 ¡BLOQUEADO!", "¡No puedes cerrar ventanas infinitas!")
        # Crear una nueva ventana por cada intento de cierre
        nueva = tk.Toplevel(ventana)
        nueva.title("¡INFINITO!")
        nueva.geometry("250x80")
        tk.Label(nueva, text="Cada vez que intentas cerrar, ¡CREO UNA NUEVA! 😈", 
                fg="red", font=("Arial", 8)).pack(pady=20)
        nueva.protocol("WM_DELETE_WINDOW", lambda: self.no_cierre_nunca(nueva))