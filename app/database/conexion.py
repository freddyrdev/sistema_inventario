import sqlite3
from pathlib import Path

from app.core.config import RUTA

RUTA_DB = Path(RUTA)

def obtener_conexion():
    carpeta = RUTA_DB.parent
    carpeta.mkdir(parents=True, exist_ok=True)

    conexion = sqlite3.connect(RUTA_DB)
    conexion.row_factory = sqlite3.Row

    return conexion