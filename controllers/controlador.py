from database.database import Database
from tkinter import messagebox

class Controlador:
    def __init__(self):
        self.db = Database()
        
    def iniciar_conexion(self):
        """Iniciar conexión a BD"""
        return self.db.connect()
    
    def cerrar_conexion(self):
        """Cerrar conexión"""
        self.db.disconnect()
    
    def obtener_equipos(self):
        if self.db.connect():
            equipos = self.db.fetch_all("SELECT * FROM equipos")
            self.db.disconnect()
            return equipos
        return []
    
    def obtener_jugadores(self):
        """Obtener todos los jugadores"""
        if self.db.connect():
            jugadores = self.db.fetch_all("SELECT * FROM jugadores")
            self.db.disconnect()
            return jugadores
        return []
    
    def guardar_jugador(self, apellido, numero_camiseta, posicion, minutos_jugados, goles_marcados, tipo_jugador):
        """Guardar un nuevo jugador en la base de datos"""
        query = """INSERT INTO jugadores 
                   (apellido, numero_camiseta, posicion, minutos_jugados, goles_marcados, tipo_jugador) 
                   VALUES (%s, %s, %s, %s, %s, %s)"""
        params = (apellido, numero_camiseta, posicion, minutos_jugados, goles_marcados, tipo_jugador)
        
        if self.db.connect():
            resultado = self.db.execute_query(query, params)
            self.db.disconnect()
            if resultado:
                messagebox.showinfo("Éxito", f"Jugador {apellido} agregado correctamente")
            else:
                messagebox.showerror("Error", "No se pudo agregar el jugador")
            return resultado
        return False