from app.core.config import EXITO, ADVERTENCIA, ERROR, PREGUNTA

class Mensaje:
    def __init__(self):
        self._tipos = {
            "exito": EXITO,
            "advertencia": ADVERTENCIA,
            "error": ERROR,
            "pregunta": PREGUNTA
        }

    def mensaje(self, msg, tipo):
        input(f"{ self._tipos[tipo] } { msg }\n")

    def pregunta(self, msg):
        return input(f"{ self._tipos["pregunta"] } { msg }: ")