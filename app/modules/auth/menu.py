import os

from app.utils.mensajes import Mensaje
from app.utils.helpers.gui.menu import MenuBase
from app.modules.auth.servicio import Servicio


class Auth(MenuBase):
    # Inyeccion de dependencias
    def __init__(self):
        super().__init__()
        self._servicio = Servicio()
    
    def _mostrar_gui(self):
        print(
            "\n      AUTENTICACION\n"
            "\n[1] Iniciar sesion"
            "\n[2] Registro"
            "\n[3] Salir"
        )

        opcion = input("> ")

        if not opcion.isdigit():
            self._msg.mensaje("La opcion ingresada es invalida.", "error")
            return None
        return opcion
        
    def _eleccion(self, eleccion):
        match eleccion:
            case "1": self._servicio.iniciar_sesion()
            case "2": self._servicio.registro()
            case "3": self.salir()
            case _: self._msg.mensaje("No se ha elegido ninguna opcion.", "advertencia")
