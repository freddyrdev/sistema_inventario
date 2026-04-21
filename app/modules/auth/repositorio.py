from app.database.conexion import obtener_conexion

class Repositorio:
    def __init__(self):
        self._conexion = obtener_conexion()
    
    def buscar_usuario(self, usuario):
        cursor = self._conexion.cursor()
        
        cursor.execute(
            "SELECT * FROM usuario WHERE usuario = ? OR email = ?;",
            (usuario["nombre"], usuario["email"])
        )

        return cursor.fetchone()