from app.database.init_db import iniciar_db
from app.utils.helpers.gui.menu import Navegacion
from app.core.navegacion import MENUS

# Procesos que recorrera el usuario

def main():
    app = MENUS["AUTENTICACION"]()

    iniciar_db()

    while True:
        try:
            app.iniciar()
            break
        except Navegacion as salto:
            clase_menu = MENUS.get(salto.destino)
            if clase_menu:
                app = clase_menu()
            else:
                print(f"ERROR: El destino { salto.destino } no existe.")
                break

if __name__ == "__main__":
    main()