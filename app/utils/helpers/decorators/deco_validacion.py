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
    | Kwargs | Valores permitidos | Dependencia | Valor por defecto |
    | :--- | :---: | :---: | :---: |
    | obligatorio | `bool` | `default` tiene valor sera `False` | `True` |
    | email | `bool` | Ninguna | `False` |
    | default | `Any` | Ninguna | `None` |
    | tipo | `type` | Ninguna | `str` |
    | consulta | `function` | `campo` | `None` |
    | campo | `str` | `consulta` | `None` |
    | unico | `bool` | `consulta` | `False` |
    | existe | `bool` | `consulta` | `False` |
    | retorno | `texto`/`consulta` | `consulta` | `texto` |
    | longitud_max | `int` | `Ninguna` | `indefinido` |
    | valor_max | `int`/`float` | `tipo int o float` | `indefinido` |
    """
    @wraps(func)
    def envoltorio(self, etiqueta, **reglas):
        if getattr(self, "_salir_flujo", False):
            return None
        
        while True:
            valor = func(self, etiqueta, **reglas)

            # El valor que se escribe en el formulario
            valor_texto = str(valor).strip() if valor is not None else ""
            respuesta_db = None

            # Mapa de reglas
            obligatorio = reglas.get("obligatorio", True)
            email = reglas.get("email", False)
            default = reglas.get("default", None)
            tipo = reglas.get("tipo", str)
            consulta = reglas.get("consulta", None)
            campo = reglas.get("campo", None)
            unico = reglas.get("unico", False)
            existe = reglas.get("existe", False)
            retorno = reglas.get("retorno", "texto")
            longitud_max = reglas.get("longitud_max", None)
            valor_max = reglas.get("valor_max", None)

            # DEPENDENCIA: Si default tiene valor obligatorio sera False
            if default != None: obligatorio = False

            # REGLA: Salir con un comando
            if COMANDO and valor_texto.lower() == str(COMANDO).lower():
                raise StopIteration

            # REGLA: Obligatorio
            if obligatorio and not valor_texto:
                self._msg.mensaje(f"{ etiqueta } es requerido.", "error")
                continue

            # REGLA: Longitud maxima
            if longitud_max and (len(valor_texto) > longitud_max ):
                self._msg.mensaje(f"{ etiqueta } rebasa la longitud maxima.")
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

            # REGLA: Tipos de datos
            if tipo:
                try:
                    valor_texto = tipo(valor_texto)
                except ValueError:
                    self._msg.mensaje("El tipo de dato ingresado es invalido.", "error")
                    continue

            # REGLA: Valor maximo
            if valor_max and (isinstance(tipo, (int, float))):
                self._msg.mensaje("El tipo de dato es invalido.", "error")
                continue

            if valor_max and (valor_texto > valor_max):
                self._msg.mensaje("El numero ingresado es invalido.", "error")
                continue

                
            # CONFIGURACION: Validacion de los campos unicos
            if (consulta or unico or existe) and not campo:
                raise TypeError("The 'campo' argument is required to use 'unico' option")
            
            criterio = { campo: valor_texto } if campo else {}

            # REGLA: Hacer consultas SQL en un campo en especifico
            if consulta: respuesta_db = consulta(**criterio)

            # REGLA: Verificar si un dato existe
            if existe and (respuesta_db is None):
                self._msg.mensaje(f"'{valor_texto}' no existe en el sistema.", "error")
                continue

            # REGLA: Verificar si un dato es unico en la base de datos
            if unico and (respuesta_db is not None):
                self._msg.mensaje(f"'{valor_texto}' ya existe en el sistema.", "error")
                continue

            if consulta and (retorno.lower() == "consulta"): 
                return respuesta_db
            return valor_texto
    return envoltorio