from colorama import Fore, Style

from app.utils.helpers.gui.menu import MenuBase
from app.modules.gestion.repositorio import Repositorio

class MenuProductos(MenuBase):
    def __init__(self):
        super().__init__()
        self._repo = Repositorio()

        self._titulo = {
            "principal": f"{'LISTADO DE PRODUCTOS':^60}",
            "id": f"{'ID':<5}",
            "producto": f"{'PRODUCTO':<25}",
            "precio": f"{'PRECIO':<10}",
            "stock": "STOCK"
        }
        
    def _mostrar_gui(self):
        productos = self._repo.obtener_productos()

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

        if not productos: 
            print(f"{Fore.RED + Style.BRIGHT}{'NO HAY NINGUN PRODUCTO DISPONIBLE':^60}{Style.RESET_ALL}")

        for p in productos:
            nombre_f = self._formatear_nombre(p["nombre"], 25)

            stock_msg = f"{ p["stock"] } un." if p["stock"] > 0 else "AGOTADO"
            print(f"{ p["id"]:<5 } | { nombre_f } | ${ p["precio"]:>9.2f } | { stock_msg }")

        print("-"*60)
        print("\n[1] Ver detalle   [2] Añadir nuevo   [3] Volver")

        opcion = input("> ")

        if not opcion.isdigit():
            self._msg.mensaje("La opcion ingresada es invalida.", "error")
            return None
        return opcion
    
    def _procesar_eleccion(self, opcion):
        match opcion:
            case "3": self.salir()
    

    def _formatear_nombre(self, nombre, ancho):
        if len(nombre) > ancho:
            return nombre[:ancho-3] + "..."
        return nombre.ljust(ancho)