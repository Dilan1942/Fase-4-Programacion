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
    ErrorReserva
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

    logger.info("Sistema Software FJ iniciado correctamente.")

    # ======================================
    # PRUEBA 1: CREACION DE CLIENTE
    # ======================================

    print("\n--- PRUEBA DE CLIENTE ---")

    try:
        cliente = Cliente(
            "123",
            "Carlos Perez",
            "carlos@gmail.com"
        )

        print(cliente.mostrar_informacion())
        logger.info("Cliente creado correctamente.")

    except ErrorCliente as error:
        print("Error de cliente:", error)
        logger.warning("Error de cliente: %s", error)

    # ======================================
    # PRUEBA 2: EXCEPCION DE CLIENTE
    # ======================================

    print("\n--- PRUEBA DE EXCEPCION ---")

    try:
        cliente_invalido = Cliente(
            "124",
            "",
            "correo@gmail.com"
        )

    except ErrorCliente as error:
        print("Error controlado:", error)
        logger.warning("Excepcion de cliente: %s", error)

    # ======================================
    # PRUEBA 3: CREACION DE SERVICIO
    # ======================================

    print("\n--- PRUEBA DE SERVICIO ---")

    try:
        servicio = ReservaSala("Sala principal", 50000)

        print("Servicio:", servicio.describir())
        print("Precio por hora:", servicio.precio)

        logger.info("Servicio creado correctamente.")

    except ErrorServicio as error:
        print("Error de servicio:", error)
        logger.warning("Error de servicio: %s", error)

    # ======================================
    # PRUEBA 4: EXCEPCION DE SERVICIO
    # ======================================

    print("\n--- PRUEBA DE EXCEPCION DE SERVICIO ---")

    try:
        servicio_invalido = ReservaSala("Sala", 0)

    except ErrorServicio as error:
        print("Error controlado:", error)
        logger.warning("Excepcion de servicio: %s", error)

    # ======================================
    # PRUEBA 5: CREACION DE RESERVA
    # ======================================

    print("\n--- PRUEBA DE RESERVA ---")

    try:
        reserva = Reserva(cliente, servicio, 2)

        print(reserva.confirmar())

        costo = reserva.procesar()

        print("Costo total de la reserva:", costo)

        logger.info("Reserva procesada correctamente.")

    except ErrorReserva as error:
        print("Error de reserva:", error)
        logger.warning("Error de reserva: %s", error)

    # ======================================
    # PRUEBA 6: EXCEPCION DE RESERVA
    # ======================================

    print("\n--- PRUEBA DE EXCEPCION DE RESERVA ---")

    try:
        reserva_invalida = Reserva(cliente, servicio, 0)

    except ErrorReserva as error:
        print("Error controlado:", error)
        logger.warning("Error de reserva: %s", error)

    # ======================================
    # FINALIZACION DEL SISTEMA
    # ======================================

    print("\n====================================")
    print("Todas las pruebas finalizaron.")
    print("Sistema preparado para funcionar.")
    print("====================================")

    logger.info("Finalizaron las pruebas del sistema.")


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
        print("\nFinalizacion del proceso de inicio.")
        logger.info("Finalizo el proceso de inicio.")
