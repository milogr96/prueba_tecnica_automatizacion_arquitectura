from logger_config import logger

def notificar_cliente(id_pedido, mensaje):
    """En producción sería email/Slack. Aquí solo log."""
    logger.info(f"NOTIFICACIÓN para pedido {id_pedido}: {mensaje}")
    print(f"[Notificación] Pedido {id_pedido}: {mensaje}")