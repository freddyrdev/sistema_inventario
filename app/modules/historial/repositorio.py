from app.database.conexion import obtener_conexion

class Repositorio():
    def __init__(self):
        self._conexion = obtener_conexion()

    def obtener_historial(self):
        cursor = self._conexion.cursor()
        cursor.execute("SELECT * FROM movimientos")

        return cursor.fetchall()