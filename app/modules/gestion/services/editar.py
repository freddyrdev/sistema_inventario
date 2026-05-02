from app.modules.gestion.repositorio import Repositorio
from app.utils.helpers.decorators.deco_formulario import formulario
from app.utils.helpers.decorators.deco_validacion import validacion
from app.utils.helpers.gui.menu import Navegacion
from app.utils.mensajes import Mensaje

class FormEditar:
    def __init__(self):
        self._msg = Mensaje()
        self._repo = Repositorio()

    @formulario
    def editar_producto(self, producto):
        while True:
            self._msg.mensaje("Todos los campos son opcionales", "advertencia")
            self._repo.editar_producto({
                "nombre": self._pedir_dato("nombre del producto", consulta=self._repo.buscar_producto, campo="nombre", unico=True, default=producto["nombre"]),
                "categoria": self._pedir_dato("categoria del producto", default=producto["categoria"]),
                "precio": self._pedir_dato("precio del producto", tipo=float, default=producto["precio"]),
                "stock": self._pedir_dato("Stock del producto", tipo=int, default=producto["stock"])
            }, id=producto["id"])

            raise Navegacion("GESTION")

    @validacion
    def _pedir_dato(self, etiqueta, **reglas):
        return self._msg.pregunta(etiqueta)
