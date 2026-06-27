import bcrypt

class Usuario:
    def __init__(self, id_usuario, username, password, rol):
        self.id = id_usuario
        self.username = username
        self.password_hash = password # Debe estar hasheado con bcrypt
        self.rol = rol

    def verificar_password(self, password_ingresada):
        # Compara la contraseña plana con el hash almacenado usando bcrypt.checkpw
        return bcrypt.checkpw(password_ingresada.encode('utf-8'), self.password_hash)