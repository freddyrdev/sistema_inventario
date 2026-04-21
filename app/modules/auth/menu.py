import os

from app.utils.mensajes import Mensaje
from app.modules.auth.servicio import Servicio

class Auth:
    # Inyeccion de dependencias
    def __init__(self):
        self._msg = Mensaje()
        self._servicio = Servicio()
    
    # Inicio del menu
    def iniciar(self):
        while True:
            os.system("cls")

            menu_respuesta = self._menu()
            if not menu_respuesta: continue

            eleccion_respuesta = self._eleccion(menu_respuesta)
            if not eleccion_respuesta: break

    def _menu(self):
        print(
            "\n      AUTENTICACION\n"
            "\n[1] Iniciar sesion"
            "\n[2] Registro"
            "\n[3] Salir"
        )

        opcion = input("> ")

        if not opcion.isdigit():
            self._msg.mensaje("La opcion ingresada es invalida.", "error")
            return False
        
        return opcion
        
    def _eleccion(self, eleccion):
        match eleccion:
            case "1": self._servicio.iniciar_sesion()
            case "2": self._servicio.registro()
            case "3": return False
            case _: self._msg.mensaje("No se ha elegido ninguna opcion.", "advertencia")
