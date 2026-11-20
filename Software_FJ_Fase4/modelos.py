# ==========================================
# SOFTWARE FJ - FASE 4
# Modelos del sistema
# ==========================================

from abc import ABC, abstractmethod
from excepciones import (
    ErrorCliente,
    ErrorServicio,
    ErrorReserva,
    ErrorValidacion
)


# Clase abstracta general
class Entidad(ABC):

    def __init__(self, identificacion):
        self._identificacion = identificacion

    @abstractmethod
    def mostrar_informacion(self):
        pass


# Clase Cliente
class Cliente(Entidad):

    def __init__(self, identificacion, nombre, correo):
        super().__init__(identificacion)

        if not nombre.strip():
            raise ErrorCliente("El nombre no puede estar vacio.")

        if "@" not in correo:
            raise ErrorCliente("El correo no es valido.")

        self.__nombre = nombre
        self.__correo = correo

    def mostrar_informacion(self):
        return f"Cliente: {self.__nombre} | Correo: {self.__correo}"


# Clase abstracta Servicio
class Servicio(ABC):

    def __init__(self, nombre, precio):
        if precio <= 0:
            raise ErrorServicio("El precio debe ser mayor que cero.")

        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def calcular_costo(self, duracion):
        pass

    @abstractmethod
    def describir(self):
        pass


# Servicio de reserva de salas
class ReservaSala(Servicio):

    def calcular_costo(self, duracion):
        return self.precio * duracion

    def describir(self):
        return "Reserva de sala."


# Servicio de alquiler de equipos
class AlquilerEquipo(Servicio):

    def calcular_costo(self, duracion):
        return self.precio * duracion

    def describir(self):
        return "Alquiler de equipos."


# Servicio de asesorias
class Asesoria(Servicio):

    def calcular_costo(self, duracion):
        return self.precio * duracion

    def describir(self):
        return "Asesoria especializada."
# ==========================================
# Clase Reserva
# ==========================================

class Reserva:

    def __init__(self, cliente, servicio, duracion):

        if not isinstance(cliente, Cliente):
            raise ErrorReserva("El cliente no es valido.")

        if not isinstance(servicio, Servicio):
            raise ErrorReserva("El servicio no es valido.")

        if not isinstance(duracion, (int, float)) or duracion <= 0:
            raise ErrorReserva("La duracion debe ser mayor que cero.")

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):
        if self.estado != "Pendiente":
            raise ErrorReserva("La reserva no se puede confirmar.")

        self.estado = "Confirmada"
        return "Reserva confirmada correctamente."

    def cancelar(self):
        if self.estado == "Cancelada":
            raise ErrorReserva("La reserva ya esta cancelada.")

        self.estado = "Cancelada"
        return "Reserva cancelada correctamente."

    def procesar(self):
        if self.estado != "Confirmada":
            raise ErrorReserva("La reserva debe estar confirmada.")

        costo = self.servicio.calcular_costo(self.duracion)

        return costo