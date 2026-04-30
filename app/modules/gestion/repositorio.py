from app.database.conexion import obtener_conexion

class Repositorio:
    def __init__(self):
        self._conexion = obtener_conexion()

    def obtener_productos(self):
        cursor = self._conexion.cursor()

        cursor.execute("SELECT * FROM productos")
        return cursor.fetchall()
    
    def crear_producto(self, producto):
        cursor = self._conexion.cursor()

        cursor.execute("""
            INSERT INTO productos (nombre, categoria, precio, stock)
            VALUES (?, ?, ?, ?);
        """, (
            producto["nombre"],
            producto["categoria"],
            producto["precio"],
            producto["stock"]
        ))

        self._conexion.commit()

    def buscar_producto(self, **producto):
        cursor = self._conexion.cursor()
        
        cursor.execute(
            "SELECT * FROM productos WHERE nombre = ? OR id = ?;", (
                producto.get("nombre", None), 
                producto.get("id", None)
        ))

        return cursor.fetchone()