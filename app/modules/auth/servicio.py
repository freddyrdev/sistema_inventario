from app.modules.auth.repositorio import Repositorio

from app.utils.mensajes import Mensaje
from app.utils.helpers.decorators.deco_validacion import validacion
from app.utils.helpers.decorators.deco_formulario import formulario

class Servicio:
    def __init__(self):
        self._repo = Repositorio()
        self._msg = Mensaje()

    @formulario
    def iniciar_sesion(self):
        while True:
            datos = {
                "usuario": self._pedir_dato("Nombre de usuario"),
                "email": self._pedir_dato("Correo electronico", email=True),
                "contrasenia": self._pedir_dato("Contraseña")
            }

            usuario = self._repo.buscar_usuario(datos)
            
            try:
                if datos["contrasenia"] != usuario["contrasenia"]:
                    self._msg.mensaje("Las credenciaes ingresadas no son validas.", "error")
                    continue

                if datos["usuario"] != usuario["usuario"]:
                    self._msg.mensaje("Las credenciaes ingresadas no son validas.", "error")
                    continue

                if datos["email"] != usuario["email"]:
                    self._msg.mensaje("Las credenciaes ingresadas no son validas.", "error")
                    continue
                
                if usuario:
                    self._msg.mensaje("Inicio de sesion con exito.", "exito")
                    return True
            except TypeError:
                self._msg.mensaje("Las credenciales ingresadas no son validas.", "error")

    @formulario
    def registro(self):
        while True:
            usuario = {
                "nombre_completo": self._pedir_dato("Nombre completo"),
                "usuario": self._pedir_dato("Nombre de usuario"),
                "email": self._pedir_dato("Correo electronico", email=True),
                "empresa": self._pedir_dato("Empresa perteneciente"),
                "rol": self._pedir_dato("Rol que ocupa", obligatorio=False, default="empleado"),
                "contrasenia": self._pedir_dato("Contraseña")
            }

            respuesta = self._repo.buscar_usuario(usuario)
            if respuesta: 
                self._msg.mensaje("El usuario ya existe.", "error")
                continue

            self._repo.crear_usuario(usuario)
            self._msg.mensaje("El usuario se a creado con exito.", "exito")
            return True

    @validacion
    def _pedir_dato(self, etiqueta, **reglas):
        return self._msg.pregunta(etiqueta)