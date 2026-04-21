from app.database.init_db import iniciar_db
from app.modules.auth.menu import Auth

# Procesos que recorrera el usuario



if __name__ == "__main__":
    auth = Auth()
    
    iniciar_db()
    auth.iniciar()