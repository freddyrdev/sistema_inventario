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
        """
        Estos son los siguientes kwargs permitidos en la consulta SQL
        | Kwargs | Tipo de dato | Valores permitidos |
        | :--- | :---: | :---: |
        | nombre | `str` | `None` |
        | id | `int` | `None` |
        | categoria | `str` | `None` |
        """
        cursor = self._conexion.cursor()
        
        cursor.execute(
            "SELECT * FROM productos WHERE nombre = ? OR id = ? OR categoria = ?;", (
                producto.get("nombre", None), 
                producto.get("id", None),
                producto.get("categoria", None)
        ))

        return cursor.fetchone()
    
    def editar_producto(self, producto, **busqueda):
        cursor = self._conexion.cursor()

        cursor.execute("""
            UPDATE productos SET nombre = ?, categoria = ?, precio = ?, stock = ?
            WHERE nombre = ? OR id = ? OR categoria = ?""", (
                producto.get("nombre"),
                producto.get("categoria"),
                producto.get("precio"),
                producto.get("stock"),

                busqueda.get("nombre", None),
                busqueda.get("id", None),
                busqueda.get("categoria", None)
        ))

        self._conexion.commit()