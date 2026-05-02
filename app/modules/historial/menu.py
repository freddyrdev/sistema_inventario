from colorama import Fore, Style

from app.utils.helpers.gui.menu import MenuBase, Navegacion
from app.modules.historial.repositorio import Repositorio

class Historial(MenuBase):
    def __init__(self):
        super().__init__()
        self.etiqueta = "HISTORIAL"
        self._repo = Repositorio()
        self._width = {
            "id": 4,
            "p_id": 6,
            "nombre": 20,
            "total": 10,
            "rem": 10,
            "motivo": 15,
            "fecha": 19,
        }
        self._ancho_total = sum(self._width.values()) + (len(self._width) * 3)

    def _mostrar_gui(self):
        historial = self._repo.obtener_historial()

        print("\n" + "=" * self._ancho_total)
        print(f"{Fore.YELLOW + Style.BRIGHT}{'HISTORIAL DE MOVIMIENTOS':^{self._ancho_total}}{Style.RESET_ALL}")
        print("=" * self._ancho_total)

        encabezado = (
            f"{'ID':<{self._width['id']}}{Style.RESET_ALL} | "
            f"{'P.ID':<{self._width['p_id']}}{Style.RESET_ALL} | "
            f"{'PRODUCTO':<{self._width['nombre']}}{Style.RESET_ALL} | "
            f"{'C.TOT':<{self._width['total']}}{Style.RESET_ALL} | "
            f"{'C.REM':<{self._width['rem']}}{Style.RESET_ALL} | "
            f"{'MOTIVO':<{self._width['motivo']}}{Style.RESET_ALL} | "
            f"{'FECHA':<{self._width['fecha']}}{Style.RESET_ALL}"
        )
        print(f"{Fore.CYAN + Style.BRIGHT}{encabezado}")
        print("-" * self._ancho_total)

        if not historial: 
            print(f"{Fore.RED + Style.BRIGHT}{'NO HAY NINGUN REGISTRO DISPONIBLE':^{self._ancho_total}}{Style.RESET_ALL}")
        else:
            for h in historial:
                # Formateamos cada celda para asegurar que no rompa la línea
                id_f = str(h["id"])[:self._width['id']].ljust(self._width['id'])
                p_id_f = str(h["producto_id"])[:self._width['p_id']].ljust(self._width['p_id'])
                nombre_f = self._formatear_texto(h["producto_nombre"], self._width['nombre'])
                total_f = str(h["cantidad_total"]).ljust(self._width['total'])
                remov_f = str(h["cantidad_removida"]).ljust(self._width['rem'])
                motivo_f = self._formatear_texto(h["motivo"], self._width['motivo'])
                fecha_f = str(h["fecha"])[:self._width['fecha']].ljust(self._width['fecha'])

                print(f"{id_f} | {p_id_f} | {nombre_f} | {total_f} | {remov_f} | {motivo_f} | {fecha_f}")

        print("-" * self._ancho_total)
        print(f"\n[1] Volver")

    def _procesar_eleccion(self, opcion):
        match opcion:
            case "1": raise Navegacion("PRINCIPAL")
            case _: self._msg.mensaje("La opcion ingresada es invalida.", "error")

    def _formatear_texto(self, nombre, ancho):
        if len(nombre) > ancho:
            return nombre[:ancho-3] + "..."
        return nombre.ljust(ancho)