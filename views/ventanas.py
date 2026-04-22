import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from controllers.controlador import Controlador

class VentanaPrincipal:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Gestión Equipo de Fútbol - Grupo N°6")
        self.ventana.geometry("600x600")
        self.ventana.configure(bg="#F5F5F7") 
        
        self.controlador = Controlador()
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
        VentanaAgregarJugador(self.controlador, self.ventana)
    
    def mostrar_jugadores(self):
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
        self.ventana.geometry("450x600")
        
        self.ventana.configure(bg="#F5F5F7")
        self.ventana.resizable(False, False)
        
        estilo = ttk.Style()
        estilo.theme_use('clam')
        estilo.configure("TLabel", background="#F5F5F7", font=("Segoe UI", 10))
        estilo.configure("TRadiobutton", background="#F5F5F7", font=("Segoe UI", 10))
        estilo.configure("TButton", font=("Segoe UI", 10, "bold"), padding=5)
        
        titulo = tk.Label(self.ventana, text="Ficha del Jugador", font=("Segoe UI", 16, "bold"), bg="#F5F5F7", fg="#1D1D1F")
        titulo.pack(pady=(20, 15))
        
        form_frame = tk.Frame(self.ventana, bg="#F5F5F7")
        form_frame.pack(fill=tk.BOTH, expand=True, padx=40)

        ttk.Label(form_frame, text="Apellido:").pack(anchor="w", pady=(5, 0))
        self.apellido_entry = ttk.Entry(form_frame, width=40, font=("Segoe UI", 10))
        self.apellido_entry.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(form_frame, text="Número de Camiseta:").pack(anchor="w", pady=(5, 0))
        self.numero_entry = ttk.Entry(form_frame, width=40, font=("Segoe UI", 10))
        self.numero_entry.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(form_frame, text="Posición:").pack(anchor="w", pady=(5, 0))
        self.posicion_var = tk.StringVar()
        self.posicion_combo = ttk.Combobox(form_frame, textvariable=self.posicion_var, state="readonly", font=("Segoe UI", 10))
        self.posicion_combo['values'] = ("Defensor", "Central", "Delantero")
        self.posicion_combo.pack(fill=tk.X, pady=(0, 10))
        
        row_frame = tk.Frame(form_frame, bg="#F5F5F7")
        row_frame.pack(fill=tk.X, pady=(5, 10))
        
        col1 = tk.Frame(row_frame, bg="#F5F5F7")
        col1.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        ttk.Label(col1, text="Minutos Jugados:").pack(anchor="w")
        self.minutos_entry = ttk.Entry(col1, font=("Segoe UI", 10))
        self.minutos_entry.pack(fill=tk.X)
        
        col2 = tk.Frame(row_frame, bg="#F5F5F7")
        col2.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=(5, 0))
        ttk.Label(col2, text="Goles Marcados:").pack(anchor="w")
        self.goles_entry = ttk.Entry(col2, font=("Segoe UI", 10))
        self.goles_entry.pack(fill=tk.X)
        
        ttk.Label(form_frame, text="Rol en el equipo:").pack(anchor="w", pady=(10, 5))
        self.tipo_var = tk.StringVar(value="campo")
        
        radio_frame = tk.Frame(form_frame, bg="#F5F5F7")
        radio_frame.pack(fill=tk.X, pady=(0, 15))
        ttk.Radiobutton(radio_frame, text="Jugador de Campo", variable=self.tipo_var, value="campo", command=self.actualizar_estado_campos).pack(side=tk.LEFT, padx=(0, 20))
        ttk.Radiobutton(radio_frame, text="Arquero", variable=self.tipo_var, value="arquero", command=self.actualizar_estado_campos).pack(side=tk.LEFT)
        
        tk.Button(self.ventana, text="Guardar Registro", command=self.guardar_jugador, 
                  bg="#007AFF", fg="white", font=("Segoe UI", 11, "bold"), 
                  relief="flat", cursor="hand2", pady=8, padx=20).pack(pady=20)

    def actualizar_estado_campos(self):
        if self.tipo_var.get() == "arquero":
            self.posicion_combo.set("")
            self.posicion_combo.config(state="disabled")
            
            self.goles_entry.config(state="normal")
            self.goles_entry.delete(0, tk.END)
            self.goles_entry.insert(0, "0")
            self.goles_entry.config(state="disabled")
        else:
            self.posicion_combo.config(state="readonly")
            self.goles_entry.config(state="normal")
            self.goles_entry.delete(0, tk.END)

    def guardar_jugador(self):
        apellido = self.apellido_entry.get().strip()
        numero_camiseta = self.numero_entry.get().strip()
        minutos_jugados = self.minutos_entry.get().strip()
        tipo_jugador = self.tipo_var.get()
        
        if tipo_jugador == "arquero":
            posicion = "Arquero"
            goles_marcados = "0"
        else:
            posicion = self.posicion_combo.get()
            goles_marcados = self.goles_entry.get().strip()

        if not all([apellido, numero_camiseta, minutos_jugados]) or (tipo_jugador == "campo" and (not posicion or not goles_marcados)):
            messagebox.showerror("Error", "Por favor complete todos los campos correspondientes.")
            return

        try:
            numero_camiseta = int(numero_camiseta)
            minutos_jugados = int(minutos_jugados)
            goles_marcados = int(goles_marcados)
            
            if numero_camiseta <= 0 or minutos_jugados < 0 or goles_marcados < 0:
                messagebox.showerror("Error", "Los números no pueden ser negativos.")
                return
        except ValueError:
            messagebox.showerror("Error", "Número, minutos y goles deben ser números enteros válidos.")
            return

        self.controlador.guardar_jugador(apellido, numero_camiseta, posicion, minutos_jugados, goles_marcados, tipo_jugador)
        self.ventana.destroy()


class VentanaMostrarJugadores:
    def __init__(self, jugadores, parent):
        self.ventana = tk.Toplevel(parent)
        self.ventana.title("Lista de Jugadores")
        self.ventana.geometry("600x400")
        self.ventana.configure(bg="#F5F5F7")
        
        frame = tk.Frame(self.ventana, bg="#F5F5F7")
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        lista_texto = tk.Text(frame, height=20, width=70, yscrollcommand=scrollbar.set, font=("Segoe UI", 10))
        lista_texto.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=lista_texto.yview)
        
        for jugador in jugadores:
            lista_texto.insert(tk.END, f"ID: {jugador.get('id', 'N/A')}\n")
            lista_texto.insert(tk.END, f"Apellido: {jugador.get('apellido', 'N/A')}\n")
            lista_texto.insert(tk.END, f"N° Camiseta: {jugador.get('numero_camiseta', 'N/A')}\n")
            lista_texto.insert(tk.END, f"Posición: {jugador.get('posicion', 'N/A')}\n")
            lista_texto.insert(tk.END, f"Minutos: {jugador.get('minutos_jugados', 'N/A')}\n")
            lista_texto.insert(tk.END, f"Goles: {jugador.get('goles_marcados', 'N/A')}\n")
            lista_texto.insert(tk.END, f"Tipo: {jugador.get('tipo_jugador', 'N/A')}\n")
            lista_texto.insert(tk.END, "-" * 50 + "\n")
        
        lista_texto.config(state=tk.DISABLED)
        
        tk.Button(self.ventana, text="Cerrar", command=self.ventana.destroy,
                  bg="#FF3B30", fg="white", font=("Segoe UI", 10, "bold"), relief="flat", cursor="hand2", padx=10).pack(pady=10)