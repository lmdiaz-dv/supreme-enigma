# Sistema de Gestión de Equipo de Fútbol - TP06

**Laboratorio de Lenguajes | UNSAdA | Grupo N°6**

Un software computacional orientado a objetos desarrollado en Python utilizando arquitectura MVC (Modelo-Vista-Controlador). El sistema cuenta con una interfaz gráfica moderna (Tkinter/ttk) y persistencia de datos en una base de datos MySQL remota (Hostinger), diseñado para administrar las estadísticas de un plantel de fútbol aplicando conceptos avanzados de herencia (POO).

---

## Requisitos Previos

- Python 3.6 o superior.
- Conexión a Internet (Requerida para interactuar con la base de datos remota).
- Tkinter (Normalmente incluido por defecto en las instalaciones de Python).
- Git (Para clonar el repositorio).

---

## Guía de Instalación y Ejecución
Un software computacional orientado a objetos desarrollado en Python utilizando arquitectura MVC (Modelo-Vista-Controlador). El sistema cuenta con una interfaz gráfica moderna (Tkinter/ttk) y persistencia de datos en MySQL, diseñado para administrar las estadísticas de un plantel de fútbol aplicando conceptos avanzados de herencia (POO).

---

## Requisitos Previos

- Python 3.6 o superior.
- Conexión a Internet (Requerida para interactuar con la base de datos remota).
- Tkinter (Normalmente incluido por defecto en las instalaciones de Python).
- Git (Para clonar el repositorio).

---

## Guía de Instalación y Ejecución

**1. Clonación del repositorio**
```bash
git clone [https://github.com/lmdiaz-dv/supreme-enigma.git](https://github.com/lmdiaz-dv/supreme-enigma.git)
cd supreme-enigma

2. Instalación de dependencias -> El proyecto utiliza librerías externas para la conexión a la base de datos y el manejo de variables de entorno. Instálalas ejecutando:

    ----> pip install -r requirements.txt 

3. Configuración de la Base de Datos (.env) -> Crea un archivo llamado .env en la raíz del proyecto (al mismo nivel que main.py) y configura las credenciales de acceso al servidor. Ejemplo:

    DB_HOST=ip_o_dominio_de_hostinger
    DB_USER=usuario_asignado_en_hostinger
    DB_PASSWORD=tu_contraseña_fuerte
    DB_NAME=nombre_de_la_base_de_datos
    DB_PORT=3306

4. Ejecución del programa -> Una vez configurado el entorno, inicia la interfaz gráfica ejecutando:

    ----> python main.py 


supreme-enigma/
├── controllers/          
│   └── controlador.py
├── database/             
│   └── database.py
├── models/               
│   ├── equipo.py
│   └── jugador.py
├── views/                
│   └── ventanas.py
├── .env                 
├── main.py               
├── requirements.txt      
└── README.md      