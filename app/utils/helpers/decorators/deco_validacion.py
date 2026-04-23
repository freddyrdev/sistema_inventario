from functools import wraps
import re

from app.utils.mensajes import Mensaje

def validacion(func):
    """
    Para usar el decorador es nesesario utilizar un metodo que se
    encargue de preguntar o ejecutar un mensaje al usuario esto
    servira para validaciones ingresadas por teclado y al momento
    de recibir el mensaje de pregunta se utilizara este formato:

    Asumiendo que ya creamos el metodo:
    self._pedir_dato("Nombre completo", obligatorio=True, email=True)
    """
    @wraps(func)
    def envoltorio(self, etiqueta, **reglas):
        while True:
            valor = func(self, etiqueta, **reglas)
            valor_texto = str(valor).strip() if valor is not None else ""

            # Mapa de reglas
            obligatorio = reglas.get("obligatorio", True)
            email = reglas.get("email", False)
            default = reglas.get("default", None)

            # REGLA: Obligatorio
            if obligatorio and not valor_texto:
                self._msg.mensaje(f"{ etiqueta } es requerido.", "error")
                continue

            # REGLA: Validacion email con expresion regular
            if email and valor_texto:
                exp_irregular = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
                if not re.match( exp_irregular, valor_texto ):
                    self._msg.mensaje("Formato del email no valido.", "error")
                    continue

            # REGLA: Valor por defecto
            if not obligatorio and default is not None:
                valor_texto = default

            return valor_texto
    return envoltorio