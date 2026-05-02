from app.modules.gestion.repositorio import Repositorio as Gestion
from app.modules.movimientos.repositorio import Repositorio
from app.utils.helpers.decorators.deco_formulario import formulario
from app.utils.helpers.decorators.deco_validacion import validacion
from app.utils.helpers.gui.menu import Navegacion
from app.utils.mensajes import Mensaje

class FormMovimientos:
    def __init__(self):
        self._msg = Mensaje()
        self._repo_gestion = Gestion()
        self._repo = Repositorio()

    @formulario
    def movimientos(self):
        while True:
            producto = self._pedir_dato("nombre del producto", consulta=self._repo_gestion.buscar_producto, campo="nombre", existe=True, retorno="consulta")

            cantidad = self._pedir_dato("Cantidad", tipo=int)
            cantidad_total = cantidad + producto["stock"]

            self._repo.crear_registro({
                "producto_id": producto["id"],
                "producto_nombre": producto["nombre"],
                "cantidad_total": cantidad_total,
                "cantidad_removida": 0,
                "motivo": self._pedir_dato("Motivo", default="No hay ningun motivo")
            })

            self._repo_gestion.editar_producto({
                "nombre": producto["nombre"],
                "categoria": producto["categoria"],
                "precio": producto["stock"],
                "stock": cantidad_total
            }, id=producto["id"])

            self._msg.mensaje("El Stock de a actualizado correctamente.", "exito")
            raise Navegacion("MOVIMIENTOS")

    @validacion
    def _pedir_dato(self, etiqueta, **reglas):
        return self._msg.pregunta(etiqueta)