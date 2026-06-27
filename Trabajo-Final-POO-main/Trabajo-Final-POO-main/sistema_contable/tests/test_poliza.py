import pytest
from app.models.poliza import Poliza

def test_crear_poliza_valida():
    # Caso válido 1
    poliza = Poliza("2026-06-18 10:00", "Pago de servicios", "1110 - Bancos", "1105 - Caja General", 150.00, "contador")
    assert poliza.monto == 150.00

def test_monto_positivo():
    # Caso válido 2
    poliza = Poliza("2026-06-18 11:00", "Venta", "1105 - Caja General", "4135 - Ingresos por Ventas", 500.00, "contador")
    assert poliza.monto > 0

def test_poliza_monto_invalido():
    # Caso inválido (falla esperada)
    with pytest.raises(ValueError):
        Poliza("2026-06-18 12:00", "Error", "1110 - Bancos", "1105 - Caja General", -50.00, "contador")