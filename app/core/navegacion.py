from app.modules.auth.menu import Auth
from app.modules.menu import MenuPrincipal as Principal
from app.modules.gestion.menu import Gestion
from app.modules.gestion.gui.buscar_datos import MenuBuscarDatos as BuscarDato
from app.modules.gestion.gui.buscar_opcion import MenuBuscar as Buscar 
from app.modules.gestion.gui.productos import MenuProductos as Productos
from app.modules.movimientos.menu import Movimientos
from app.modules.historial.menu import Historial

#####################################
#       SISTEMA DE NAVEGACION       #
#####################################

# Aqui se tendra que agregar todos los sistema de navegacion
# del sistema si se quiere utilizar la excepcion Navegacion()

MENUS = {
    "AUTENTICACION": Auth,
    "PRINCIPAL": Principal,
    "GESTION": Gestion,
    "BUSCAR_PRODUCTOS": Buscar,
    "BUSCAR_DATO": BuscarDato,
    "VER_PRODUCTOS": Productos,
    "MOVIMIENTOS": Movimientos,
    "HISTORIAL": Historial
}