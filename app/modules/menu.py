import sys

from app.utils.helpers.gui.menu import MenuBase, Navegacion
from app.modules.gestion.menu import Gestion


class MenuPrincipal(MenuBase):
    def __init__(self):
        super().__init__()
        self.etiqueta = "PRINCIPAL"
        self._gestion = Gestion()
    
    def _mostrar_gui(self):
        print(
            "\n     MENU PRINCIPAL\n"
            "\n[1] Gestionar productos"
            # "\n[2] Movimientos de inventario"
            # "\n[3] Ver historial de movimientos"
            "\n[4] Salir"
        )

    def _procesar_eleccion(self, opcion):
        match opcion:
            case "1": raise Navegacion("GESTION")
            case "4": sys.exit()
            case _: self._msg.mensaje("La opcion ingresada es invalida.", "error")