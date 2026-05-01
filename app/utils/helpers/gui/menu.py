from abc import ABC, abstractmethod
import os

from app.utils.mensajes import Mensaje

class MenuBase(ABC):
    """
    Para utilizar la clase abstracta 'MenuBase' se nesesita
    heredar los atributos nesesario como `self.etiqueta: str`
    y despues utilizar los siguientes metodos.

    Metodo `_mostrar_gui()` este metodo privado se utilizara
    especificamente para mostrar el menu de opciones que se
    requieren.

    Metodo `_procesar_eleccion()` este metodo privado se 
    utilizara para procesar las elecciones escogidas por 
    el usuario.

    Metodo `iniciar()` este metodo se utilizara para poder
    iniciar el menu establecido en la clase.

    Metodo `salir()` este metodo se utilizara cuando quieras
    terminar el proceso de ejecucion del menu.

    Metodo `cambiar_menu(Clase)` este metodo se utiliza para cambiar
    de menu si es nesesario.
    """
    def __init__(self):
        self._msg = Mensaje()
        self._ejecutando = True

    def iniciar(self):
        """
        Para usar el metodo `iniciar()` se debe tener el
        atributo `self.etiqueta: str` en el contructor

        ```python
        class Menu(MenuBase):
            def __init__(self):
                super().__init__()
                self.etiqueta = "MENU PRINCIPAL"
        ```
        """
        self._ejecutando = True
        
        while self._ejecutando:
            os.system("cls" if os.name == "nt" else "clear")
            try:
                self._mostrar_gui() # Mostrar el menu

                opcion = input("> ")

                if not opcion.isdigit():
                    self._msg.mensaje("La opcion ingresada es invalida.", "advertencia")
                    continue

                self._procesar_eleccion(opcion)
            except Navegacion as salto:
                if hasattr(self, "etiqueta") and salto.destino == self.etiqueta:
                    self._ejecutando = True
                    continue

                raise salto
            except StopIteration:
                self.salir()

    @abstractmethod
    def _mostrar_gui(self):
        pass

    @abstractmethod
    def _procesar_eleccion(self, opcion):
        pass

    def cambiar_menu(self, menu_clase):
        """
        En un metodo al final hay que retornar `True` para poder
        accionar otro menu por ejemplo:
        ```python
        def metodo(self):
            ...
            return True
        ```

        Y al final en la clase donde se contiene el menu se debe
        utilizar la siguiente condicion:
        ```python
        if self.metodo():
            self.cambiar_menu(SiguienteMenu)
        ```
        """
        if isinstance(menu_clase, type):
            menu = menu_clase()
        else:
            menu = menu_clase

        menu.iniciar()

    def salir(self):
        self._ejecutando = False

# Excepcion especial para navegacion
class Navegacion(Exception):
    def __init__(self, destino):
        """
        Para navegar de forma eficiente con esta opcion se tendra
        que tener obligatoriamente en el constructor un atributo
        llamado `self.etiqueta` que hereda de `MenuBase`

        y para usarlo simplemente se nesesita lanzar un error:
        ```python
        raise Navegacion("DESTINO")
        ```
        """
        self.destino = destino
        