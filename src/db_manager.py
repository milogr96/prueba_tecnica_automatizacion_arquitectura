import sqlite3
import hashlib
import os
from datetime import datetime, timedelta

# Obtener la raíz del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)  # Asegurar que la carpeta data existe
DB_PATH = os.path.join(DATA_DIR, "procesados.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS solicitudes
                 (id_pedido TEXT, timestamp TEXT, estado TEXT, damage_type TEXT ,hash_id TEXT)''')
    conn.commit()
    conn.close()

def registrar_solicitud(id_pedido, estado):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    timestamp = datetime.now().isoformat()
    hash_id = hashlib.md5(id_pedido.encode()).hexdigest()
    c.execute("INSERT INTO solicitudes (id_pedido, timestamp, estado,hash_id) VALUES (?,?,?,?)",
              (id_pedido, timestamp,damage_type ,estado, hash_id))
    conn.commit()
    conn.close()

def solicitud_duplicada(id_pedido, ventana_horas=2):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    hace = (datetime.now() - timedelta(hours=ventana_horas)).isoformat()
    c.execute("SELECT COUNT(*) FROM solicitudes WHERE id_pedido = ? AND timestamp > ?",
              (id_pedido, hace))
    count = c.fetchone()[0]
    conn.close()
    return count > 0

def actualizar_estado(id_pedido, nuevo_estado):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("UPDATE solicitudes SET estado = ? WHERE id_pedido = ?",
              (nuevo_estado, id_pedido))
    conn.commit()
    conn.close()