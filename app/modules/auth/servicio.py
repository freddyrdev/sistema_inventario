from app.modules.auth.repositorio import Repositorio
from app.utils.mensajes import Mensaje

class Servicio:
    def __init__(self):
        self._repo = Repositorio()
        self._msg = Mensaje()

    def iniciar_sesion(self):
        while True:
            nombre = self._msg.pregunta("Nombre de usuario")
            email = self._msg.pregunta("Correo electronico")
            contrasenia = self._msg.pregunta("Contraseña de usuario")

            usuario = self._repo.buscar_usuario({
                "nombre": nombre,
                "email": email,
                "contrasenia": contrasenia
            })

            if usuario: 
                self._msg.mensaje("Inicio de sesion con exito.", "exito")
                return
            
            self._msg.mensaje("Las credenciales ingresadas no son validas.", "error")

    def registro(self):
        while True:
            nombre_completo = self._msg.pregunta("Nombre completo")
            if not nombre_completo: 
                self._msg.mensaje("Nombre completo requerido", "error")
                continue

            usuario = self._msg.pregunta("Nombre de usuario")
            if not usuario: 
                self._msg.mensaje("Nombre de usuario requerido", "error")
                continue

            email = self._msg.pregunta("Correo electronico")
            if not email:
                self._msg.mensaje("Correo electronico requerido", "error")
                continue

            empresa = self._msg.pregunta("Empresa perteneciente")
            if not empresa:
                self._msg.mensaje("La empresa es requerida", "error")
                continue

            rol = self._msg.pregunta("Rol o perfil en la empresa")
            if not rol: rol = "empleado"

            ({
                "nombre_completo": nombre_completo,
                "usuario": usuario,
                "email": email,
                "empresa": empresa,
                "rol": rol
            })