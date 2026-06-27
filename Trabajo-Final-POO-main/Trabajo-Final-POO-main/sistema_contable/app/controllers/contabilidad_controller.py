import bcrypt
from app.models.poliza import Poliza

class ContabilidadController:
    def __init__(self, conn, cursor):
        self.conn = conn
        self.cursor = cursor

    def autenticar_usuario(self, username, password):
        self.cursor.execute("SELECT password FROM usuarios WHERE usuario = ?", (username,))
        resultado = self.cursor.fetchone()
        if resultado:
            stored_hash = resultado[0]
            # Usamos la validación de la clase Usuario (POO)
            return bcrypt.checkpw(password.encode('utf-8'), stored_hash)
        return False

    def registrar_poliza(self, fecha, concepto, cuenta_debe, cuenta_haber, monto, usuario):
        # Llama al Modelo para instanciar y validar los datos aplicando POO estricta
        poliza = Poliza(fecha, concepto, cuenta_debe, cuenta_haber, monto, usuario)
        
        # Guardamos en la base de datos
        self.cursor.execute("""
            INSERT INTO polizas (fecha, concepto, cuenta_debe, cuenta_haber, monto, usuario) 
            VALUES (?, ?, ?, ?, ?, ?)
        """, (poliza.fecha, poliza.concepto, poliza.cuenta_debe, poliza.cuenta_haber, poliza.monto, poliza.usuario))
        self.conn.commit()

    def obtener_polizas(self):
        self.cursor.execute("SELECT id, fecha, concepto, cuenta_debe, cuenta_haber, monto, usuario FROM polizas ORDER BY id DESC")
        return self.cursor.fetchall()