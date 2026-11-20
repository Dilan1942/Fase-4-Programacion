
# ==========================================
# SOFTWARE FJ - FASE 4
# Modelos del sistema
# ==========================================

from abc import ABC, abstractmethod
import math

from excepciones import (
    ErrorCliente,
    ErrorServicio,
    ErrorReserva,
    ErrorValidacion
)


# ==========================================
# FUNCIONES DE VALIDACION
# ==========================================

def validar_numero(valor, nombre, minimo=None):
    """Valida que un valor sea numerico y finito."""

    if isinstance(valor, bool) or not isinstance(valor, (int, float)):
        raise ErrorValidacion(
            f"{nombre} debe ser un numero."
        )

    if not math.isfinite(valor):
        raise ErrorValidacion(
            f"{nombre} debe ser un numero finito."
        )

    if minimo is not None and valor <= minimo:
        raise ErrorValidacion(
            f"{nombre} debe ser mayor que {minimo}."
        )


# ==========================================
# CLASE ABSTRACTA ENTIDAD
# ==========================================

class Entidad(ABC):

    def __init__(self, identificacion):

        if not isinstance(identificacion, str) or not identificacion.strip():
            raise ErrorValidacion(
                "La identificacion no puede estar vacia."
            )

        self._identificacion = identificacion.strip()

    @abstractmethod
    def mostrar_informacion(self):
        pass


# ==========================================
# CLASE CLIENTE
# ==========================================

class Cliente(Entidad):

    def __init__(self, identificacion, nombre, correo):
        super().__init__(identificacion)

        if not isinstance(nombre, str) or not nombre.strip():
            raise ErrorCliente(
                "El nombre no puede estar vacio."
            )

        if not isinstance(correo, str) or "@" not in correo:
            raise ErrorCliente(
                "El correo no es valido."
            )

        partes_correo = correo.strip().split("@")

        if (
            len(partes_correo) != 2
            or not partes_correo[0]
            or "." not in partes_correo[1]
            or partes_correo[1].startswith(".")
            or partes_correo[1].endswith(".")
        ):
            raise ErrorCliente(
                "El formato del correo no es valido."
            )

        self.__nombre = nombre.strip()
        self.__correo = correo.strip()

    def mostrar_informacion(self):
        return (
            f"Cliente: {self.__nombre} | "
            f"Correo: {self.__correo}"
        )


# ==========================================
# CLASE ABSTRACTA SERVICIO
# ==========================================

class Servicio(ABC):

    def __init__(self, nombre, precio):

        if not isinstance(nombre, str) or not nombre.strip():
            raise ErrorServicio(
                "El nombre del servicio no puede estar vacio."
            )

        try:
            validar_numero(precio, "El precio", 0)

        except ErrorValidacion as error:
            raise ErrorServicio(
                "No se pudo registrar el precio del servicio."
            ) from error

        self.nombre = nombre.strip()
        self.precio = precio

    def validar_parametros(self, duracion, descuento=0, impuesto=0):
        """Valida los parametros utilizados para calcular costos."""

        validar_numero(duracion, "La duracion", 0)
        validar_numero(descuento, "El descuento", -1)
        validar_numero(impuesto, "El impuesto", -1)

        if descuento > 100:
            raise ErrorServicio(
                "El descuento no puede superar el 100%."
            )

        if impuesto > 100:
            raise ErrorServicio(
                "El impuesto no puede superar el 100%."
            )

    def _calcular_costo_base(self, duracion, descuento=0, impuesto=0):
        """
        Calcula el costo con parametros opcionales.

        Ejemplos:
        calcular_costo(2)
        calcular_costo(2, descuento=10)
        calcular_costo(2, descuento=10, impuesto=19)
        """

        self.validar_parametros(
            duracion,
            descuento,
            impuesto
        )

        costo = self.precio * duracion

        costo_con_descuento = costo - (
            costo * descuento / 100
        )

        costo_final = costo_con_descuento + (
            costo_con_descuento * impuesto / 100
        )

        return round(costo_final, 2)

    @abstractmethod
    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        pass

    @abstractmethod
    def describir(self):
        pass


# ==========================================
# SERVICIO DE RESERVA DE SALAS
# ==========================================

class ReservaSala(Servicio):

    def validar_parametros(self, duracion, descuento=0, impuesto=0):
        super().validar_parametros(
            duracion,
            descuento,
            impuesto
        )

    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        return self._calcular_costo_base(
            duracion,
            descuento,
            impuesto
        )

    def describir(self):
        return "Reserva de sala."


# ==========================================
# SERVICIO DE ALQUILER DE EQUIPOS
# ==========================================

class AlquilerEquipo(Servicio):

    def validar_parametros(self, duracion, descuento=0, impuesto=0):
        super().validar_parametros(
            duracion,
            descuento,
            impuesto
        )

    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        return self._calcular_costo_base(
            duracion,
            descuento,
            impuesto
        )

    def describir(self):
        return "Alquiler de equipos."


# ==========================================
# SERVICIO DE ASESORIAS
# ==========================================

class Asesoria(Servicio):

    def validar_parametros(self, duracion, descuento=0, impuesto=0):
        super().validar_parametros(
            duracion,
            descuento,
            impuesto
        )

    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        return self._calcular_costo_base(
            duracion,
            descuento,
            impuesto
        )

    def describir(self):
        return "Asesoria especializada."


# ==========================================
# CLASE RESERVA
# ==========================================

class Reserva:

    def __init__(self, cliente, servicio, duracion):

        if not isinstance(cliente, Cliente):
            raise ErrorReserva(
                "El cliente no es valido."
            )

        if not isinstance(servicio, Servicio):
            raise ErrorReserva(
                "El servicio no es valido."
            )

        try:
            validar_numero(duracion, "La duracion", 0)

        except ErrorValidacion as error:
            raise ErrorReserva(
                "No se pudo crear la reserva por una duracion incorrecta."
            ) from error

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):

        if self.estado != "Pendiente":
            raise ErrorReserva(
                "La reserva no se puede confirmar."
            )

        self.estado = "Confirmada"

        return "Reserva confirmada correctamente."

    def cancelar(self):

        if self.estado == "Cancelada":
            raise ErrorReserva(
                "La reserva ya esta cancelada."
            )

        if self.estado == "Procesada":
            raise ErrorReserva(
                "No se puede cancelar una reserva procesada."
            )

        self.estado = "Cancelada"

        return "Reserva cancelada correctamente."

    def procesar(self):

        if self.estado != "Confirmada":
            raise ErrorReserva(
                "La reserva debe estar confirmada."
            )

        try:
            costo = self.servicio.calcular_costo(
                self.duracion
            )

        except ErrorServicio as error:
            raise ErrorReserva(
                "Ocurrio un error al calcular el costo de la reserva."
            ) from error

        self.estado = "Procesada"

        return costo
