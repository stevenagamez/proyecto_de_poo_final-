import sqlite3
import bcrypt
from app.views.login_view import LoginView
from app.controllers.contabilidad_controller import ContabilidadController

def inicializar_bd(cursor):
    """Crea las tablas de usuarios y pólizas si no existen, e inserta un usuario por defecto."""
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT UNIQUE,
            password TEXT,
            rol TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS polizas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT,
            concepto TEXT,
            cuenta_debe TEXT,
            cuenta_haber TEXT,
            monto REAL,
            usuario TEXT
        )
    """)
    # Insertar usuario administrador por defecto con contraseña encriptada ('admin123')
    hashed = bcrypt.hashpw('admin123'.encode('utf-8'), bcrypt.gensalt())
    try:
        cursor.execute("INSERT INTO usuarios (usuario, password, rol) VALUES (?, ?, ?)", 
                       ('admin', hashed, 'Administrador'))
    except sqlite3.IntegrityError:
        pass # Ya existe

def main():
    # Conexión a la base de datos SQLite
    conn = sqlite3.connect("contabilidad_avanzada.db")
    cursor = conn.cursor()
    inicializar_bd(cursor)
    conn.commit()

    # Instanciamos el controlador pasándole la conexión y el cursor
    controller = ContabilidadController(conn, cursor)
    
    # Arrancamos la vista de Login
    login_vista = LoginView(controller)
    login_vista.mainloop()

if __name__ == "__main__":
    main()