from datetime import datetime

class Poliza:
    def __init__(self, fecha, concepto, cuenta_debe, cuenta_haber, monto, usuario):
        self.fecha = fecha
        self.concepto = concepto
        self.cuenta_debe = cuenta_debe
        self.cuenta_haber = cuenta_haber

        # Validación de la regla de negocio (monto positivo y cuentas distintas)
        monto_val = float(monto)
        if monto_val <= 0:
            raise ValueError("El monto debe ser mayor a cero.")
        if cuenta_debe == cuenta_haber:
            raise ValueError("La cuenta de cargo y abono no pueden ser iguales.")

        self.monto = monto_val
        self.usuario = usuario