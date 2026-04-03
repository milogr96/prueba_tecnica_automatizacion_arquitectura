import re
from datetime import datetime

def validar_id_pedido(id_pedido):
    
    """Valida el formato: OP + 6 dígitos (aammdd) + guión + 8 dígitos.
    Además verifica que los 6 dígitos correspondan a una fecha real.
    Ejemplo válido: OP260402-12345678 (26=2026, 04=abril, 02=día)"""
    
    if not id_pedido or not isinstance(id_pedido, str):
        return False

    # 1. Validar formato con expresión regular
    patron = r'^OP(\d{6})-(\d{8})$'
    match = re.match(patron, id_pedido)
    if not match:
        return False

    # 2. Extraer la parte de la fecha (aammdd)
    fecha_str = match.group(1)  #260402
    
    # 3. Validar que sea una fecha real
    try:
        # %y%m%d interpreta año en formato corto (26 -> 2026)
        datetime.strptime(fecha_str, "%y%m%d")
        return True
    except ValueError:
        # Fecha inválida (ej:  99/99/99, 31/02/99)
        return False
    
    
    
    