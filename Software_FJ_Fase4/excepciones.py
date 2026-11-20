# ==========================================
# SOFTWARE FJ - FASE 4
# Excepciones personalizadas
# ==========================================

# Excepcion general del sistema
class ErrorSistema(Exception):
    pass


# Error relacionado con clientes
class ErrorCliente(ErrorSistema):
    pass


# Error relacionado con servicios
class ErrorServicio(ErrorSistema):
    pass


# Error relacionado con reservas
class ErrorReserva(ErrorSistema):
    pass


# Error de validacion de datos
class ErrorValidacion(ErrorSistema):
    pass
