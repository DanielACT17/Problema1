
import sqlite3
import csv

class BaseDatos:
    def __init__(self, nombre_bd="Biblioteca.db"):
        self.nombre_bd = nombre_bd
        self.conexion = None

    def conectar(self):
        self.conexion = sqlite3.connect(self.nombre_bd)
        self.crear_tabla()
    
    def crear_tabla(self):
        cursor = self.conexion.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       rut TEXT NOT NULL,
                       nombre TEXT NOT NULL,
                       apellido INTEGER NOT NULL,
                       correo TEXT NOT NULL,
                       telefono TEXT NOT NULL,
                       contrasena TEXT NOT NULL);  
             ''')
        cursor.execute('''         
            CREATE TABLE IF NOT EXISTS libros (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        codigo TEXT NOT NULL,
                        titulo TEXT NOT NULL,
                        autor TEXT NOT NULL,
                        stock INTEGER NOT NULL);
             ''') 
        cursor.execute  ('''   
            CREATE TABLE IF NOT EXISTS prestamos 
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        codigo TEXT NOT NULL,
                        fecha_prestamo TEXT NOT NULL,
                        fecha_devolucion TEXT NOT NULL,
                        usuario_id INTEGER NOT NULL,
                        libro_id INTEGER NOT NULL,
                        FOREIGN KEY (usuario_id) REFERENCES usuarios (id),
                        FOREIGN KEY (libro_id) REFERENCES libros (id));
             ''')

        self.conexion.commit()