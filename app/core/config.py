from colorama import Fore, Style

#############################
#       Base de datos       #
#############################

# La ruta significa en donde se guardara el archivo que
# almacenara todos los datos de la aplicacion es muy
# importante que si no se sabe lo que se esta haciendo
# no se toca esta opcion amenos de que sea algo
# extremandamente estricto

RUTA = "data/inventario.db"

################################
#       Estilos de texto       #
################################

# Colores o personalizacion de textos de exito,
# advertencia y errores al momento de utilizar la
# aplicacion.

# NOTA: Esta configuracion se modificara en todos los
# mensajes de la app.

EXITO = Fore.GREEN + Style.BRIGHT + "EXITO:" + Style.RESET_ALL
ADVERTENCIA = Fore.YELLOW + Style.BRIGHT + "[!]:" + Style.RESET_ALL
ERROR = Fore.RED + Style.BRIGHT + "ERROR:" + Style.RESET_ALL
PREGUNTA = Fore.CYAN + Style.BRIGHT + "[?]:" + Style.RESET_ALL

#########################################
#       Configuracion de mensajes       #
#########################################

# Configuraciones generales de los mensajes de texto
# definira reglas, entre otras cosas.

# Si el usuario digita la palabra que contiene
# el valor de la variable del comando sale del
# formulario.

COMANDO = "salir"