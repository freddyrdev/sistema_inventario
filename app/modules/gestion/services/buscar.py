from app.modules.gestion.repositorio import Repositorio
from app.utils.helpers.decorators.deco_formulario import formulario
from app.utils.helpers.decorators.deco_validacion import validacion
from app.utils.mensajes import Mensaje

class FormBuscar:
    def __init__(self):
        self._msg = Mensaje()
        self._repo = Repositorio()

    @formulario
    def buscar_nombre(self):
        while True:
            return self._pedir_dato("Ingresa el nombre del producto", consulta=self._repo.buscar_producto, campo="nombre", existe=True, retorno="consulta")

    @formulario
    def buscar_categoria(self):
        while True:
            return self._pedir_dato("Ingresa la categoria del producto", consulta=self._repo.buscar_producto, campo="categoria", existe=True, retorno="consulta")

    @formulario
    def buscar_id(self):
        while True:
            return self._pedir_dato("Ingresa el ID del producto", consulta=self._repo.buscar_producto, campo="id", tipo=int, existe=True, retorno="consulta")

    @validacion
    def _pedir_dato(self, etiqueta, **reglas):
        return self._msg.pregunta(etiqueta)