from db_manager import solicitud_duplicada

def es_duplicado(id_pedido, ventana_horas=2):
    return solicitud_duplicada(id_pedido, ventana_horas)