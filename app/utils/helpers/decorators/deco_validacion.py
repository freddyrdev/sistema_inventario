from functools import wraps
import re

from app.core.config import COMANDO

def validacion(func):
    """
    Para usar el decorador es nesesario utilizar un metodo que se
    encargue de preguntar o ejecutar un mensaje al usuario esto
    servira para validaciones ingresadas por teclado y al momento
    de recibir el mensaje de pregunta se utilizara este formato:

    Creacion del metodo para la implementacion del decorador:
    ```python
    @validacion
    def _pedir_dato(self, etiqueta, **reglas):
        return self._msg.pregunta("Mensaje")
    ```
    
    Un ejemplo de como utilizar el sistema de validaciones
    ```python
        self._pedir_dato("Numero a ingresar", default=0, tipo=int)
    ```

    Los Kwargs permitidos son:
    | Kwargs | Valores permitidos |
    | :--- | :---: |
    | obligatorio | `bool` |
    | email | `bool` |
    | default | `Any` |
    | tipo | `type` |
    """
    @wraps(func)
    def envoltorio(self, etiqueta, **reglas):
        if getattr(self, "_salir_flujo", False):
            return None
        
        while True:
            valor = func(self, etiqueta, **reglas)

            # El valor que se escribe en el formulario
            valor_texto = str(valor).strip() if valor is not None else ""

            # Mapa de reglas
            obligatorio = reglas.get("obligatorio", True)
            email = reglas.get("email", False)
            default = reglas.get("default", None)
            tipo = reglas.get("tipo", str)

            if default != None: obligatorio = False

            # REGLA: Salir con un comando
            if COMANDO and valor_texto.lower() == str(COMANDO).lower():
                self._salir_flujo = True
                return None

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
            if not (valor_texto) and (default != None):
                valor_texto = default

            if tipo:
                try:
                    valor_texto = tipo(valor_texto)
                except ValueError:
                    self._msg.mensaje("El tipo de dato ingresado es invalido.", "error")
                    continue

            return valor_texto
    return envoltorio