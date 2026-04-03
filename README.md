# Prueba Técnica – Automatización e-Ship
  
**Stack:** Python 3.10 + SQLite  

## Requisitos
- Python 3.10 o superior

## Ejecución
1. Clonar el repositorio.
2. Ubicarse en la carpeta raíz.
3. Ejecutar: `python src/main.py`

## Estructura del proyecto
- `src/` – Código fuente del prototipo (Python + SQLite)
- `data/` – Archivos JSON de entrada (`solicitudes.json`, `pedidos.json`)
- `logs/` – Archivos de log generados durante la ejecución
- `Propuesta Libre/` – Carpeta con la arquitectura alternativa (WhatsApp Business + portal web)
  - `Propuesta Libre.pdf` y README.md – Descripción detallada de la propuesta
  - `Diagrama Propuesta libre.mmd` – Diagrama de flujo de la arquitectura propuesta

## Supuestos del prototipo
- Formato de ID: `OPaammdd-12345678` (fecha válida, ej. `OP260402-12345678`)
- Ventana de deduplicación: **2 horas**
- Aprobación manual simulada por consola (para montos > $200 USD)

## Entregables incluidos
- ✅ **Fase A** – Análisis, preguntas al stakeholder, riesgos y decisiones de diseño.
- ✅ **Fase B** – Diagrama de arquitectura (`Diagrama FaseB.mmd`).
- ✅ **Fase C** – Prototipo funcional en Python + SQLite (código en `src/`).
- ✅ **Fase D** – Propuesta de IA (detección de sentimiento y validación de imagen).
- ✅ **Propuesta Libre** – Mejora de arquitectura usando WhatsApp Business y portal web, con manejo de saturación y emojis para sentimiento. (Ver carpeta `Propuesta Libre/`)

## ¿Cómo probar el prototipo?
1. Asegúrate de tener Python 3.10+ instalado.
2. Clona este repositorio.
3. En la raíz, ejecuta:  
   `python src/main.py`
4. Observa los logs en consola y en la carpeta `logs/`.  
   Para montos > $200, el sistema te pedirá que simules la aprobación del supervisor escribiendo `s` (sí) o `n` (no).

## Notas adicionales
- La base de datos SQLite (`data/procesados.db`) se crea automáticamente al ejecutar.
- Los archivos `solicitudes.json` y `pedidos.json` contienen datos de ejemplo; puedes modificarlos para probar otros casos.
- La propuesta libre es una mejora conceptual que no está implementada en el prototipo, pero está completamente documentada.

---

**¡Gracias por la revisión!**
