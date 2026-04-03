import json
import time
import os
from logger_config import logger

def cargar_pedidos():
    """Carga el diccionario de pedidos desde data/pedidos.json"""
    ruta = os.path.join(os.path.dirname(__file__), "..", "data", "pedidos.json")
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error(f"No se encontró el archivo {ruta}. Se usará un diccionario vacío.")
        return {}
    except json.JSONDecodeError:
        logger.error(f"Error al decodificar {ruta}. Verifica el formato JSON.")
        return {}

def obtener_monto_pedido(id_pedido):
    """Simula consulta a base de datos externa leyendo desde pedidos.json.
    Incluye demora artificial para probar reintentos."""
    
    time.sleep(5)  # Simula latencia de red
    pedidos = cargar_pedidos()
    if id_pedido in pedidos:
        return pedidos[id_pedido]
    else:
        raise ValueError(f"ID {id_pedido} no existe en la base de datos de pedidos")

def obtener_monto_con_reintentos(id_pedido, reintentos=3):
    
    """Intenta obtener el monto con reintentos (backoff exponencial).
    Si después de reintentos falla, lanza la excepción."""
    
    for intento in range(reintentos):
        try:
            monto = obtener_monto_pedido(id_pedido)
            logger.info(f"Pedido {id_pedido} encontrado con monto ${monto}")
            return monto
        except Exception as e:
            logger.error(f"Intento {intento+1} falló para {id_pedido}: {e}")
            if intento < reintentos - 1:
                espera = 2 ** intento  # 1, 2, 4 segundos
                logger.info(f"Reintentando en {espera} segundos...")
                time.sleep(espera)
            else:
                raise  # Re-lanzar la excepción después de todos los reintentos

def solicitar_aprobacion_supervisor(id_pedido, monto):
    
    """Simula la aprobación del supervisor.
    En un entorno real sería Slack/Teams. Aquí usamos input por consola.
    Retorna True si aprueba, False si rechaza."""
    
    logger.info(f"Se requiere aprobación para pedido {id_pedido} con monto ${monto}")
    respuesta = input(f"¿Aprueba la devolución del pedido {id_pedido} (s/n)? ").strip().lower()
    return respuesta == 's'