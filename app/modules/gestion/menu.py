from app.utils.helpers.gui.menu import MenuBase, Navegacion
from app.modules.gestion.services.agregar import FormAgregar

class Gestion(MenuBase):
    def __init__(self):
        super().__init__()
        self.etiqueta = "GESTION"
        self._agregar_productos = FormAgregar()

    def _mostrar_gui(self):
        print(
            "\n     GESTION DE PRODUCTOS\n"
            "\n[1] Ver productos"
            "\n[2] Agregar producto"
            "\n[3] Buscar producto"
            # "\n[5] Eliminar producto"
            "\n[6] Salir"
        )

    def _procesar_eleccion(self, opcion):
        match opcion:
            case "1": raise Navegacion("VER_PRODUCTOS")
            case "2": self._agregar_productos.crear_producto()
            case "3": raise Navegacion("BUSCAR_PRODUCTOS")
            case "6": raise Navegacion("PRINCIPAL")
            case _: self._msg.mensaje("La opcion ingresada es invalida.", "error")