import bcrypt
from app.models.usuario import Usuario

def test_password_correcta():
    password = bcrypt.hashpw("admin123".encode(), bcrypt.gensalt())
    usuario = Usuario(1, "admin", password, "Administrador")

    assert usuario.verificar_password("admin123") == True

def test_password_incorrecta():
    password = bcrypt.hashpw("admin123".encode(), bcrypt.gensalt())
    usuario = Usuario(1, "admin", password, "Administrador")

    assert usuario.verificar_password("123456") == False

def test_usuario_vacio():
    password = bcrypt.hashpw("admin123".encode(), bcrypt.gensalt())
    usuario = Usuario(1, "", password, "Administrador")

    assert usuario.username == ""
