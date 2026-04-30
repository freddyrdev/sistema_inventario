from app.modules.gestion.repositorio import Repositorio
from app.utils.mensajes import Mensaje
from app.utils.helpers.decorators.deco_formulario import formulario
from app.utils.helpers.decorators.deco_validacion import validacion

class FormAgregar():
    def __init__(self):
        self._msg = Mensaje()
        self._repo = Repositorio()

    @formulario
    def crear_producto(self):
        while True:
            self._repo.crear_producto({
                "nombre": self._pedir_dato("Nombre del producto", unico=self._repo.buscar_producto, campo="nombre"),
                "categoria": self._pedir_dato("Categoria del producto"),
                "precio": self._pedir_dato("Precio del producto", tipo=float),
                "stock": self._pedir_dato("Stock del producto", default=0, tipo=int)
            })

            self._msg.mensaje("El producto se a creado con exito.", "exito")
            return True
    
    @validacion
    def _pedir_dato(self, etiqueta, **reglas):
        return self._msg.pregunta(etiqueta)