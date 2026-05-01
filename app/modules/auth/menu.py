from app.utils.helpers.gui.menu import MenuBase, Navegacion
from app.modules.auth.servicio import Servicio

class Auth(MenuBase):
    # Inyeccion de dependencias
    def __init__(self):
        super().__init__()
        self.etiqueta = "AUTENTICACION"
        self._servicio = Servicio()
    
    def _mostrar_gui(self):
        print(
            "\n      AUTENTICACION\n"
            "\n[1] Iniciar sesion"
            "\n[2] Registro"
            "\n[3] Salir"
        )
        
    def _procesar_eleccion(self, opcion):
        match opcion:
            case "1": 
                if self._servicio.iniciar_sesion():
                    raise Navegacion("PRINCIPAL")

            case "2": 
                if self._servicio.registro():
                    raise Navegacion("PRINCIPAL")

            case "3": self.salir()
            case _: self._msg.mensaje("La opcion ingresada es invalida.", "error")
