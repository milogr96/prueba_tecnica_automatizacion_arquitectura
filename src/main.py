import json
import os
import sys

# Como ejecutaremos desde la raíz del proyecto con "python src/main.py", necesitamos ajustar el path.
sys.path.insert(0, os.path.dirname(__file__))

from db_manager import init_db, registrar_solicitud, actualizar_estado, solicitud_duplicada
from validador import validar_id_pedido
from deduplicador import es_duplicado
from aprobador import obtener_monto_con_reintentos, solicitar_aprobacion_supervisor
from notificador import notificar_cliente
from logger_config import logger

# Inicializar BD
init_db()

def procesar_solicitud(solicitud):
    id_pedido = solicitud.get("id_pedido")
    if not validar_id_pedido(id_pedido):
        logger.warning(f"ID inválido: {id_pedido}")
        notificar_cliente(id_pedido, "El ID del pedido no tiene el formato correcto. Por favor verifique.")
        return

    if solicitud_duplicada(id_pedido, ventana_horas=2):
        logger.info(f"Solicitud duplicada para {id_pedido} dentro de las últimas 2 horas. Se ignora.")
        notificar_cliente(id_pedido, "Su solicitud ya está siendo procesada. No es necesario reenviarla.")
        return

    registrar_solicitud(id_pedido, "recibida")
    logger.info(f"Procesando nueva solicitud para pedido {id_pedido}")

    try:
        monto = obtener_monto_con_reintentos(id_pedido)
    except Exception as e:
        logger.error(f"No se pudo obtener el monto para {id_pedido}: {e}")
        notificar_cliente(id_pedido, "Hubo un error interno. Por favor intente más tarde.")
        actualizar_estado(id_pedido, "error_interno")
        return

    if monto <= 200: #Aprobacion Automatica
        logger.info(f"Pedido {id_pedido} (${monto}) <= $200. Aprobación automática.")
        notificar_cliente(id_pedido, "Su devolución ha sido aprobada automáticamente. Se generará un código de retorno.")
        actualizar_estado(id_pedido, "aprobado_auto")
    else:
        logger.info(f"Pedido {id_pedido} (${monto}) > $200. Se requiere aprobación manual.")
        actualizar_estado(id_pedido, "pendiente_aprobacion")
        aprobado = solicitar_aprobacion_supervisor(id_pedido, monto)
        if aprobado:
            notificar_cliente(id_pedido, "Su devolución ha sido aprobada por el supervisor.")
            actualizar_estado(id_pedido, "aprobado_supervisor")
        else:
            notificar_cliente(id_pedido, "El supervisor ha rechazado su solicitud.")
            actualizar_estado(id_pedido, "rechazado")

    logger.info(f"Procesamiento completado para {id_pedido}")

def main():
    # Ruta al archivo solicitudes.json en la raíz/data/
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    solicitudes_path = os.path.join(BASE_DIR, "data", "solicitudes.json")
    
    if not os.path.exists(solicitudes_path):
        logger.error(f"No se encontró el archivo {solicitudes_path}")
        return
    
    with open(solicitudes_path, "r") as f:
        solicitudes = json.load(f)
    
    for solicitud in solicitudes:
        procesar_solicitud(solicitud)
        print("-" * 40)

if __name__ == "__main__":
    main()