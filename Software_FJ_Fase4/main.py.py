# ==========================================
# SOFTWARE FJ - FASE 4
# Sistema Integral de Gestion de Clientes,
# Servicios y Reservas
# ==========================================

# Importacion de excepciones personalizadas
from excepciones import (
    ErrorSistema,
    ErrorCliente,
    ErrorServicio,
    ErrorReserva,
    ErrorValidacion
)

# Importacion de las clases del sistema
from modelos import (
    Cliente,
    ReservaSala,
    AlquilerEquipo,
    Asesoria,
    Reserva
)

# Importacion de herramientas para registros
import logging
import os


# ==========================================
# CONFIGURACION DEL REGISTRO DE EVENTOS
# ==========================================

# Crear la carpeta logs si no existe
os.makedirs("logs", exist_ok=True)

# Configurar el archivo de registro
logging.basicConfig(
    filename="logs/software_fj.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

# Crear el registrador del sistema
logger = logging.getLogger("SoftwareFJ")


# ==========================================
# FUNCION PRINCIPAL DEL PROGRAMA
# ==========================================

def main():

    print("====================================")
    print("       SISTEMA SOFTWARE FJ")
    print("====================================")

    print("Sistema iniciado correctamente.")
    print("Preparando gestion de clientes,")
    print("servicios y reservas.")

    # Registrar inicio del sistema
    logger.info("Sistema Software FJ iniciado correctamente.")

    print("====================================")
    print("Sistema preparado para funcionar.")
    print("====================================")


# ==========================================
# EJECUCION DEL PROGRAMA
# ==========================================

if __name__ == "__main__":

    try:
        main()

    except ErrorSistema as error:
        logger.error("Error del sistema: %s", error)
        print("Se presento un error:", error)

    except Exception as error:
        logger.exception("Error inesperado: %s", error)
        print("Se presento un error inesperado.")

    finally:
        print("Finalizacion del proceso de inicio.")
        logger.info("Finalizo el proceso de inicio.")