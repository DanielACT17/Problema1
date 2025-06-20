from personas import Persona

class Usuario(Persona):
    def __init__(self, rut, nombre, apellido, correo, telefono, contrasena):
        super().__init__(rut, nombre, apellido) 
        self.correo = correo
        self.telefono = telefono
        self.contrasena = contrasena

    def generar_usuario(self):
        usuario_n = f"{self.nombre} {self.apellido}"
        print(f"El usuario es: {usuario_n}")

     
    


    