from personas import Persona 
from usuarios import Usuario
from database import BaseDatos

def menu():
    print("\n--- Menu Biblioteca ---")
    print("1. Registrar Usuario")
    print("2. Buscar un Libro")
    print("3. Rentar Libro")
    print("4. Devolver Libro")
    print("5. Salir")

def main():
    bd = BaseDatos()
    bd.conectar()
    
    while True:
        menu()
        opcion = input("Seleccione una opcion:")
    

if __name__ == "__main__":
    main()
