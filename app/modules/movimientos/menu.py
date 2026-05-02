from app.modules.movimientos.servicio import FormMovimientos
from app.utils.helpers.gui.menu import MenuBase, Navegacion

class Movimientos(MenuBase):
    def __init__(self):
        super().__init__()
        self.etiqueta = "MOVIMIENTOS"
        self._servicio = FormMovimientos()

    def _mostrar_gui(self):
        print(
            "\n    MOVIMIENTOS\n"
            "\n[1] Registrar entrada"
            "\n[2] Registrar salida"
            "\n[3] Salir"
        )

    def _procesar_eleccion(self, opcion):
        match opcion:
            case "1": self._servicio.entrada()
            case "2": self._servicio.salida()
            case "3": raise Navegacion("PRINCIPAL")