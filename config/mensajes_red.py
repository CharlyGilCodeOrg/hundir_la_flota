from enum import Enum
import json

class TipoMensaje(Enum):
    # Cliente -> Servidor
    BUSCAR_PARTIDA = "buscar_partida"
    CANCELAR_BUSQUEDA = "cancelar_busqueda"
    REALIZAR_DISPARO = "realizar_disparo"
    ABANDONAR = "abandonar"
    
    # Servidor -> Cliente
    ESPERANDO_OPONENTE = "esperando_oponente"
    PARTIDA_INICIADA = "partida_iniciada"
    TU_TURNO = "tu_turno"
    RESULTADO_DISPARO = "resultado_disparo"
    VICTORIA = "victoria"
    DERROTA = "derrota"
    OPONENTE_ABANDONO = "oponente_abandono"
    ERROR = "error"

class Mensaje:
    @staticmethod
    def crear(tipo, datos=None):
        return json.dumps({
            "tipo": tipo.value if isinstance(tipo, TipoMensaje) else tipo,
            "datos": datos or {}
        })
    
    @staticmethod
    def parsear(mensaje_str):
        try:
            return json.loads(mensaje_str)
        except json.JSONDecodeError:
            return None