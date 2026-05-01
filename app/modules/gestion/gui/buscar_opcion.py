from app.modules.gestion.services.buscar import FormBuscar
from app.modules.gestion.gui.buscar_datos import MenuBuscarDatos
from app.utils.helpers.gui.menu import MenuBase

class MenuBuscar(MenuBase):
    def __init__(self):
        super().__init__()
        self.etiqueta = "BUSCAR_PRODUCTOS"
        self._form = FormBuscar()

    def _mostrar_gui(self):
        print(
            "\n   BUSCAR PRODUCTO\n"
            "\n[1] Nombre"
            "\n[2] Categoria"
            "\n[3] ID"
            "\n[4] Salir"
        )

        opcion = input("> ")

        if not opcion.isdigit():
            self._msg.mensaje("La opcion ingresada es invalida.", "error")
            return None
        return opcion
    
    def _proceso_cambiar_menu(self, proceso_de_busqueda):
        producto = proceso_de_busqueda()

        if producto:
            nuevo_menu = MenuBuscarDatos(dict(producto))
            self.cambiar_menu(nuevo_menu)

    def _procesar_eleccion(self, opcion):
        match opcion:
            case "1": self._proceso_cambiar_menu(self._form.buscar_nombre)
            case "2": self._proceso_cambiar_menu(self._form.buscar_categoria)
            case "3": self._proceso_cambiar_menu(self._form.buscar_id)
            case "4": self.salir()
            case _: self._msg.mensaje("La opcion ingresada es invalida.", "error")