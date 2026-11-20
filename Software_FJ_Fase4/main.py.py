# ==========================================
# SOFTWARE FJ - FASE 4
# Sistema de clientes, servicios y reservas
# ==========================================

# Importar las excepciones
from excepciones import (
    ErrorSistema,
    ErrorCliente,
    ErrorServicio,
    ErrorReserva
)

# Importar las clases del sistema
from modelos import (
    Cliente,
    ReservaSala,
    AlquilerEquipo,
    Asesoria,
    Reserva
)

# Importar herramientas para guardar registros
import logging
import os


# ==========================================
# CONFIGURAR ARCHIVO DE LOGS
# ==========================================

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/software_fj.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
    force=True
)

logger = logging.getLogger("SoftwareFJ")


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

def main():

    print("====================================")
    print("       SISTEMA SOFTWARE FJ")
    print("====================================")

    logger.info("Inicio del sistema Software FJ.")

    # Crear listas para almacenar los datos
    clientes = []
    servicios = []
    reservas = []

    # ======================================
    # OPERACION 1: CREAR CLIENTE
    # ======================================

    print("\n--- OPERACION 1: CREAR CLIENTE ---")

    cliente = None

    try:
        cliente = Cliente(
            "123",
            "Carlos Perez",
            "carlos@gmail.com"
        )

        clientes.append(cliente)

    except ErrorCliente as error:
        print("Error:", error)
        logger.warning("Error al crear cliente: %s", error)

    else:
        print(cliente.mostrar_informacion())
        print("Cliente creado correctamente.")
        logger.info("Cliente creado correctamente.")

    # ======================================
    # OPERACION 2: CLIENTE INVALIDO
    # ======================================

    print("\n--- OPERACION 2: CLIENTE INVALIDO ---")

    try:
        Cliente("124", "", "correo@gmail.com")

    except ErrorCliente as error:
        print("Error controlado:", error)
        logger.warning("Cliente invalido: %s", error)

    else:
        print("Cliente registrado.")

    # ======================================
    # OPERACION 3: CORREO INVALIDO
    # ======================================

    print("\n--- OPERACION 3: CORREO INVALIDO ---")

    try:
        Cliente("125", "Laura Gomez", "correo")

    except ErrorCliente as error:
        print("Error controlado:", error)
        logger.warning("Correo invalido: %s", error)

    else:
        print("Correo aceptado.")

    # ======================================
    # OPERACION 4: CREAR RESERVA DE SALA
    # ======================================

    print("\n--- OPERACION 4: SERVICIO DE SALA ---")

    sala = None

    try:
        sala = ReservaSala("Sala principal", 50000)
        servicios.append(sala)

    except ErrorServicio as error:
        print("Error:", error)
        logger.warning("Error en servicio de sala: %s", error)

    else:
        print(sala.describir())
        print("Precio por hora:", sala.precio)
        logger.info("Servicio de sala creado.")

    # ======================================
    # OPERACION 5: PRECIO INVALIDO
    # ======================================

    print("\n--- OPERACION 5: PRECIO INVALIDO ---")

    try:
        ReservaSala("Sala secundaria", 0)

    except ErrorServicio as error:
        print("Error controlado:", error)
        logger.warning("Precio invalido: %s", error)

    else:
        print("Servicio creado.")

    # ======================================
    # OPERACION 6: ALQUILER DE EQUIPOS
    # ======================================

    print("\n--- OPERACION 6: ALQUILER DE EQUIPOS ---")

    equipo = None

    try:
        equipo = AlquilerEquipo("Computadores", 30000)
        servicios.append(equipo)

    except ErrorServicio as error:
        print("Error:", error)
        logger.warning("Error en alquiler: %s", error)

    else:
        print(equipo.describir())
        print("Precio por hora:", equipo.precio)
        logger.info("Alquiler de equipos creado.")

    # ======================================
    # OPERACION 7: CREAR ASESORIA
    # ======================================

    print("\n--- OPERACION 7: ASESORIA ---")

    asesoria = None

    try:
        asesoria = Asesoria(
            "Asesoria especializada",
            80000
        )

        servicios.append(asesoria)

    except ErrorServicio as error:
        print("Error:", error)
        logger.warning("Error en asesoria: %s", error)

    else:
        print(asesoria.describir())
        print("Precio por hora:", asesoria.precio)
        logger.info("Asesoria creada.")

    # ======================================
    # OPERACION 8: COSTO NORMAL
    # ======================================

    print("\n--- OPERACION 8: COSTO NORMAL ---")

    if sala is not None:

        try:
            costo = sala.calcular_costo(2)

        except ErrorServicio as error:
            print("Error:", error)
            logger.warning("Error al calcular costo: %s", error)

        else:
            print("Costo de dos horas:", costo)
            logger.info("Costo normal calculado.")

    # ======================================
    # OPERACION 9: COSTO CON DESCUENTO
    # ======================================

    print("\n--- OPERACION 9: COSTO CON DESCUENTO ---")

    if sala is not None:

        try:
            costo = sala.calcular_costo(2, descuento=10)

        except ErrorServicio as error:
            print("Error:", error)
            logger.warning("Error en descuento: %s", error)

        else:
            print("Costo con descuento:", costo)
            logger.info("Descuento aplicado.")

    # ======================================
    # OPERACION 10: COSTO CON IMPUESTO
    # ======================================

    print("\n--- OPERACION 10: COSTO CON IMPUESTO ---")

    if sala is not None:

        try:
            costo = sala.calcular_costo(
                2,
                descuento=10,
                impuesto=19
            )

        except ErrorServicio as error:
            print("Error:", error)
            logger.warning("Error en impuesto: %s", error)

        else:
            print("Costo final:", costo)
            logger.info("Impuesto aplicado.")

    # ======================================
    # OPERACION 11: DESCUENTO INVALIDO
    # ======================================

    print("\n--- OPERACION 11: DESCUENTO INVALIDO ---")

    if sala is not None:

        try:
            sala.calcular_costo(2, descuento=150)

        except ErrorSistema as error:
            print("Error controlado:", error)
            logger.warning("Descuento invalido: %s", error)

        else:
            print("Calculo realizado.")

    # ======================================
    # OPERACION 12: CREAR RESERVA
    # ======================================

    print("\n--- OPERACION 12: CREAR RESERVA ---")

    reserva = None

    if cliente is not None and sala is not None:

        try:
            reserva = Reserva(cliente, sala, 2)
            reservas.append(reserva)

        except ErrorReserva as error:
            print("Error:", error)
            logger.warning("Error al crear reserva: %s", error)

        else:
            print("Reserva creada correctamente.")
            logger.info("Reserva creada.")

    else:
        print("No se puede crear la reserva.")
        logger.warning("Falta el cliente o el servicio.")

    # ======================================
    # OPERACION 13: CONFIRMAR Y PROCESAR
    # ======================================

    print("\n--- OPERACION 13: CONFIRMAR RESERVA ---")

    if reserva is not None:

        try:
            print(reserva.confirmar())
            costo = reserva.procesar()
            print("Costo total:", costo)
            print("Estado:", reserva.estado)

        except ErrorReserva as error:
            print("Error:", error)
            logger.warning("Error al procesar reserva: %s", error)

        else:
            print("Reserva procesada correctamente.")
            logger.info("Reserva procesada.")

    else:
        print("No existe una reserva para procesar.")

    # ======================================
    # OPERACION 14: RESERVA INVALIDA
    # ======================================

    print("\n--- OPERACION 14: RESERVA INVALIDA ---")

    if cliente is not None and sala is not None:

        try:
            Reserva(cliente, sala, 0)

        except ErrorReserva as error:
            print("Error controlado:", error)
            logger.warning("Reserva invalida: %s", error)

            # Mostrar la causa original del error
            if error.__cause__ is not None:
                print("Causa original:", error.__cause__)

        else:
            print("Reserva creada.")

    # ======================================
    # OPERACION 15: CANCELAR RESERVA
    # ======================================

    print("\n--- OPERACION 15: CANCELAR RESERVA ---")

    if cliente is not None and equipo is not None:

        try:
            reserva2 = Reserva(cliente, equipo, 1)
            reservas.append(reserva2)

            print(reserva2.cancelar())

        except ErrorReserva as error:
            print("Error:", error)
            logger.warning("Error al cancelar: %s", error)

        else:
            print("Reserva cancelada correctamente.")
            logger.info("Reserva cancelada.")

    # ======================================
    # MOSTRAR LISTAS DEL SISTEMA
    # ======================================

    print("\n====================================")
    print("       RESUMEN DEL SISTEMA")
    print("====================================")

    print("Total de clientes:", len(clientes))
    print("Total de servicios:", len(servicios))
    print("Total de reservas:", len(reservas))

    logger.info(
        "Resumen: %s clientes, %s servicios y %s reservas.",
        len(clientes),
        len(servicios),
        len(reservas)
    )

    # Mostrar los clientes registrados
    print("\nCLIENTES REGISTRADOS:")

    for cliente_registrado in clientes:
        print(cliente_registrado.mostrar_informacion())

    # Mostrar los servicios registrados
    print("\nSERVICIOS REGISTRADOS:")

    for servicio in servicios:
        print(servicio.describir())

    # Mostrar las reservas registradas
    print("\nRESERVAS REGISTRADAS:")

    for reserva_registrada in reservas:
        print("Estado:", reserva_registrada.estado)

    # ======================================
    # FINALIZACION
    # ======================================

    print("\n====================================")
    print("Las operaciones finalizaron.")
    print("Sistema Software FJ funcionando.")
    print("====================================")

    logger.info("Finalizaron las operaciones.")


# ==========================================
# EJECUTAR PROGRAMA
# ==========================================

if __name__ == "__main__":

    try:
        main()

    except ErrorSistema as error:
        print("Error general:", error)
        logger.error("Error general: %s", error)

    except Exception as error:
        print("Error inesperado:", error)
        logger.exception("Error inesperado.")

    finally:
        print("\nFinalizacion del programa.")
        logger.info("Programa finalizado.")
