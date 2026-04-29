from app.utils.helpers.gui.menu import MenuBase
from app.modules.gestion.productos import MenuProductos

class Gestion(MenuBase):
    def __init__(self):
        super().__init__()
        self._ver_productos = MenuProductos()

    def _mostrar_gui(self):
        print(
            "\n     GESTION DE PRODUCTOS\n"
            "\n[1] Ver productos"
            "\n[2] Agregar producto"
            "\n[3] Buscar producto"
            "\n[4] Editar producto"
            "\n[5] Eliminar producto"
            "\n[6] Salir"
        )

        opcion = input("> ")

        if not opcion.isdigit():
            self._msg.mensaje("La opcion ingresada es invalida.", "error")
            return None
        return opcion
    
    def _procesar_eleccion(self, opcion):
        match opcion:
            case "1": self._ver_productos.iniciar()
            case "6": self.salir()