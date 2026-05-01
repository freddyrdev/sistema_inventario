from functools import wraps
import os

from colorama import Fore

from app.core.config import COMANDO

def formulario(func):
    """
    El decorador formulario sirve para marcar a un
    metodo como un formulario al que el usuario
    ingresara los datos nesesarios para completarlo
    """
    @wraps(func)
    def envoltorio(self, *args, **kwargs):
        os.system("cls" if os.name == "nt" else "clear")
        self._msg.mensaje(f"Ingresa el comando { Fore.CYAN }'{ COMANDO }'{ Fore.RESET } para salir del formulario", "advertencia")

        try:
            return func(self, *args, **kwargs)
        except StopIteration:
            self._msg.mensaje("El formulario se a cancelado", "advertencia")
            return None
    return envoltorio
