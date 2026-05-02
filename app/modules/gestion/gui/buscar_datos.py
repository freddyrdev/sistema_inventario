from colorama import Fore, Style

from app.utils.helpers.gui.menu import MenuBase
from app.modules.gestion.services.agregar import FormAgregar
from app.modules.gestion.services.editar import FormEditar
from app.utils.helpers.gui.menu import Navegacion

class MenuBuscarDatos(MenuBase):
    def __init__(self, producto):
        super().__init__()
        self.etiqueta = "BUSCAR_PRODUCTOS"
        self._form_producto = FormAgregar()
        self._form_editar = FormEditar()
        self._producto = producto
        self._titulo = {
            "principal": f"{'LISTADO DE PRODUCTOS':^60}",
            "id": f"{'ID':<5}",
            "producto": f"{'PRODUCTO':<25}",
            "precio": f"{'PRECIO':<10}",
            "stock": "STOCK"
        }
        

    def _mostrar_gui(self):
        stock = self._producto.get("stock", 0) or 0
        precio = self._producto.get("precio", 0.0) or 0.0
        id_prod = self._producto.get("id", 0) or 0
        nombre = self._formatear_nombre(self._producto["nombre"], 25)

        stock_msg = f"{ stock } un." if stock > 0 else "AGOTADO"

        print("")
        print("="*60)
        print(f"{Fore.YELLOW + Style.BRIGHT}{ self._titulo["principal"] }{Style.RESET_ALL}")
        print("="*60)
        print(
            f"{Fore.CYAN + Style.BRIGHT}{ self._titulo["id"] }{Style.RESET_ALL} | "
            f"{Fore.CYAN + Style.BRIGHT}{ self._titulo["producto"] }{Style.RESET_ALL} |  " 
            f"{Fore.CYAN + Style.BRIGHT}{ self._titulo["precio"] }{Style.RESET_ALL} |  " 
            f"{Fore.CYAN + Style.BRIGHT}{ self._titulo["stock"] }{Style.RESET_ALL}"
        )
        print("-"*60)
        print(f"{id_prod:<5} | {nombre} | ${precio:>9.2f}  | {stock_msg}")
        print("-"*60)
        print("\n[1] Editar producto   [2] Eliminar producto   [3] Volver")

    def _procesar_eleccion(self, opcion):
        match opcion:
            case "1": self._form_editar.editar_producto(self._producto)
            case "3": raise Navegacion("GESTION")
            case _: self._msg.mensaje("La opcion ingresada es invalida.", "error")

    def _formatear_nombre(self, nombre, ancho):
        if len(nombre) > ancho:
            return nombre[:ancho-3] + "..."
        return nombre.ljust(ancho)