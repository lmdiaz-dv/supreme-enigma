import mysql.connector

# Configuración con la contraseña correcta
config = {
    'host': 'srv1438.hstgr.io',
    'port': 3306,
    'user': 'u481307435_grupo6',
    'password': 'OUp9v5D8d?1',  # Contraseña correcta sin :
    'database': 'u481307435_futbol'
}

print("Intentando conectar a Hostinger...")
print(f"Host: {config['host']}")
print(f"Usuario: {config['user']}")
print(f"Password: {'*' * len(config['password'])}")
print(f"Base datos: {config['database']}")

try:
    conn = mysql.connector.connect(**config)
    print("\n✅ ¡CONEXIÓN EXITOSA A HOSTINGER!")
    
    cursor = conn.cursor()
    cursor.execute("SELECT VERSION()")
    version = cursor.fetchone()
    print(f"📌 Versión MySQL: {version[0]}")
    
    cursor.execute("SHOW TABLES")
    tablas = cursor.fetchall()
    print(f"📊 Tablas encontradas: {len(tablas)}")
    for tabla in tablas:
        print(f"   - {tabla[0]}")
    
    cursor.close()
    conn.close()
    print("\n🔒 Conexión cerrada correctamente")
    
except mysql.connector.Error as err:
    print(f"\n❌ Error: {err}")
    print("\n💡 Posibles causas:")
    print("1. La contraseña tiene caracteres especiales que necesitan escaparse")
    print("2. El usuario no tiene permisos sobre la base de datos")
    print("3. La base de datos no existe")