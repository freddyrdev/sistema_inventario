from app.utils.helpers.gui.menu import MenuBase
from app.modules.gestion.services.productos import MenuProductos
from app.modules.gestion.services.agregar import FormAgregar

class Gestion(MenuBase):
    def __init__(self):
        super().__init__()
        self._ver_productos = MenuProductos()
        self._agregar_productos = FormAgregar()

    def _mostrar_gui(self):
        print(
            "\n     GESTION DE PRODUCTOS\n"
            "\n[1] Ver productos"
            "\n[2] Agregar producto"
            # "\n[3] Buscar producto"
            # "\n[4] Editar producto"
            # "\n[5] Eliminar producto"
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
            case "2": self._agregar_productos.crear_producto()
            case "6": self.salir()
            case _: self._msg.mensaje("La opcion ingresada es invalida.", "error")