import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

class Database:
    def __init__(self):
        self.host = os.getenv('DB_HOST')
        self.user = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASSWORD')
        self.database = os.getenv('DB_NAME')
        self.port = os.getenv('DB_PORT')
        self.connection = None
        self.cursor = None
    
    def connect(self):
        """Establecer conexión con la base de datos"""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port
            )
            self.cursor = self.connection.cursor(dictionary=True)
            print("✅ Conexión exitosa a la base de datos")
            return True
        except Error as e:
            print(f"❌ Error al conectar: {e}")
            return False
    
    def disconnect(self):
        """Cerrar la conexión"""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            print("🔒 Conexión cerrada")
    
    def execute_query(self, query, params=None):
        """Ejecutar una consulta SQL"""
        try:
            self.cursor.execute(query, params or ())
            self.connection.commit()
            return True
        except Error as e:
            print(f"❌ Error en consulta: {e}")
            return False
    
    def fetch_all(self, query, params=None):
        """Obtener todos los registros"""
        try:
            self.cursor.execute(query, params or ())
            return self.cursor.fetchall()
        except Error as e:
            print(f"❌ Error al obtener datos: {e}")
            return []
    
    def fetch_one(self, query, params=None):
        """Obtener un solo registro"""
        try:
            self.cursor.execute(query, params or ())
            return self.cursor.fetchone()
        except Error as e:
            print(f"❌ Error al obtener dato: {e}")
            return None