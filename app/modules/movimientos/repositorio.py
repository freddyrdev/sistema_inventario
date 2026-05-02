from app.database.conexion import obtener_conexion

class Repositorio:
    def __init__(self):
        self._conexion = obtener_conexion()

    def crear_registro(self, movimiento):
        cursor = self._conexion.cursor()

        cursor.execute("""
            INSERT INTO movimientos (producto_id, producto_nombre, cantidad_total, cantidad_removida, motivo)
            VALUES (?, ?, ?, ?, ?)
        """, (
            movimiento["producto_id"],
            movimiento["producto_nombre"],
            movimiento["cantidad_total"],
            movimiento["cantidad_removida"],
            movimiento["motivo"],
        ))

        self._conexion.commit()