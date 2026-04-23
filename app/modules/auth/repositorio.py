from app.database.conexion import obtener_conexion

class Repositorio:
    def __init__(self):
        self._conexion = obtener_conexion()
    
    def buscar_usuario(self, usuario):
        cursor = self._conexion.cursor()
        
        cursor.execute(
            "SELECT * FROM usuario WHERE usuario = ? OR email = ?;",
            (usuario["usuario"], usuario["email"])
        )

        return cursor.fetchone()
    
    def crear_usuario(self, usuario):
        cursor = self._conexion.cursor()
        
        cursor.execute(
            """
            INSERT INTO usuario (nombre_completo, usuario, email, empresa, rol, contrasenia)
            VALUES (?, ?, ?, ?, ?, ?);
            """, (
                usuario["nombre_completo"], 
                usuario["usuario"], 
                usuario["email"], 
                usuario["empresa"], 
                usuario["rol"],
                usuario["contrasenia"])
        )

        self._conexion.commit()