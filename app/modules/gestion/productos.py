from app.utils.helpers.gui.menu import MenuBase
from app.modules.gestion.repositorio import Repositorio

class MenuProductos(MenuBase):
    def __init__(self):
        super().__init__()
        self._repo = Repositorio()
        
    def _mostrar_gui(self):
        productos = self._repo.obtener_productos()

        print("\n="*60)
        print(f"{"LISTADO DE PRODUCTOS":^60}")
        print("="*60)
        print(f"{'ID':<5} | {'PRODUCTO':<25} | {'PRECIO':<10} | {'STOCK'}")
        print("-"*60)

        if not productos: print(f"{"NO HAY NINGUN PRODUCTO DISPONIBLE":^60}")

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