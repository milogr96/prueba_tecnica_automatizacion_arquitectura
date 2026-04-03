import logging
import os

#la ruta absoluta al directorio raíz del proyecto (dos niveles arriba de src)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGS_DIR = os.path.join(BASE_DIR, "logs")
os.makedirs(LOGS_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(os.path.join(LOGS_DIR, "procesamiento.log")),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)