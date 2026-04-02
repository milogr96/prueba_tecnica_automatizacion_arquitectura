# Prueba Técnica – Automatización e-Ship

**Stack:** Python 3.10 + SQLite  

## Requisitos previos
- Python 3.10 o superior instalado.
- No requiere librerías externas.

## Ejecución
1. Clonar el repositorio.
2. Ubicarse en la carpeta `src/`.
3. Ejecutar: `python main.py`
4. El programa leerá automáticamente el archivo `data/solicitudes.json` y procesará cada solicitud.

## Salida esperada
- Se verán logs en consola y se escribirá un archivo `logs/procesamiento.log`.
- La base de datos `data/procesados.db` se actualizará con el estado de cada solicitud.

## Supuestos
- Se asume que el ID del pedido tiene formato alfanumérico de 8 caracteres.
- La ventana de deduplicación es de 2 horas.
- La aprobación del supervisor se simula con una entrada por consola (s/n).

## Enlaces a otros entregables
- [Análisis Fase A](./fase_a_analisis.md)
- [Diagrama de arquitectura](./diagrama.mmd) 
