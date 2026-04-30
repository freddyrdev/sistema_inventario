from functools import wraps
import os

from colorama import Fore

from app.core.config import COMANDO

def formulario(func):
    """
    El decorador formulario sirve para marcar a un
    modulo como un formulario al que el usuario
    ingresara los datos nesesarios para completarlo

    **USO DEL DECORADOR:**
    Se debe de crear un atributo privado con el nombre
    `_salir_flujo = True` y al final del metodo se
    retornara un `_salir_flujo = False`

    **EJEMPLO:**
    ```python
    def __init__(self):
        self._salir_flujo = True

    @formulario
    def metodo(self):
        # Logica del formulario
        
        if self._salir_flujo: 
            return False
    ```
    """
    @wraps(func)
    def envoltorio(self, *args, **kwargs):
        os.system("cls" if os.name == "nt" else "clear")
        self._msg.mensaje(f"Ingresa el comando { Fore.CYAN }'{ COMANDO }'{ Fore.RESET } para salir del formulario", "advertencia")

        self._salir_flujo = False
        resultado = func(self, *args, **kwargs)

        if self._salir_flujo:
            self._msg.mensaje("El formulario se a cancelado", "advertencia")
            return None
        
        return resultado
    return envoltorio