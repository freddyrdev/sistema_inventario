from abc import ABC, abstractmethod
import os

from app.utils.mensajes import Mensaje

class MenuBase(ABC):
    """
    Para utilizar la clase abstracta MenuBase se nesesita heredar
    e inicializar los atributos en el contructor despues de este
    proceso se debera crear los metodos _mostrar_gui() y
    _procesar_coleccion() pasando el argunmento de opcion
    """
    def __init__(self):
        self._msg = Mensaje()
        self._ejecutando = True

    def iniciar(self):
        while self._ejecutando:
            os.system("cls" if os.name == "nt" else "clear")
            opcion = self._mostrar_gui()

            if not opcion:
                self._msg.mensaje("Presione 'Enter' para continuar.", "advertencia")
                continue

            self._procesar_coleccion(opcion)

    @abstractmethod
    def _mostrar_gui(self):
        pass

    @abstractmethod
    def _procesar_coleccion(self, opcion):
        pass

    def salir(self):
        self._ejecutando = False