from red.globales import enviar, jugador_partida
from controlador.controlador_pvp import ControladorPVP
from modelo.partida.estado_partida import EstadoPartida
from modelo.resultado import ResultadoDisparo
from config.mensajes import TRADUCCION


class SesionPVP:

    def __init__(self, writer1, writer2):
        self.writer1 = writer1
        self.writer2 = writer2

        self._controlador = ControladorPVP()

        jugador_partida[writer1] = self
        jugador_partida[writer2] = self

        self._writers = {
            1: writer1,
            2: writer2
        }

        self._jugadores = {
            writer1: 1,
            writer2: 2
        }


    async def iniciar(self):

        await enviar(self.writer1, {
            "tipo": "inicio",
            "jugador": 1,
            "estado": self._controlador.estado().value
        })

        await enviar(self.writer2, {
            "tipo": "inicio",
            "jugador": 2,
            "estado": self._controlador.estado().value
        })

        await self._enviar_barcos(1)
        await self._enviar_barcos(2)


    async def recibir_mensaje(self, writer, mensaje):

        jugador = self._jugadores[writer]
        estado = self._controlador.estado()

        if estado == EstadoPartida.COLOCACION:
            await self._procesar_colocacion(jugador, mensaje)

        elif estado == EstadoPartida.JUGANDO:
            await self._procesar_juego(jugador, mensaje)


    async def _procesar_colocacion(self, jugador, mensaje):

        if mensaje.get("tipo") != "seleccionar_barco":
            return

        writer = self._writers[jugador]

        try:
            colocado = self._controlador.colocar_barco(
                jugador,
                mensaje["indice"],
                mensaje["x"],
                mensaje["y"],
                mensaje["horizontal"]
            )

            if not colocado:
                await enviar(writer, {
                    "tipo": "error",
                    "mensaje": "Posición inválida"
                })
                return

            await enviar(writer, {
                "tipo": "confirmacion",
                "mensaje": "Barco colocado correctamente"
            })

            await self._enviar_estado(jugador)

            pendientes = self._controlador.obtener_barcos_pendientes(jugador)

            if pendientes:
                await self._enviar_barcos(jugador)
            else:
                await enviar(writer, {
                    "tipo": "espera",
                    "mensaje": "Esperando al otro jugador..."
                })

            if self._controlador.estado() == EstadoPartida.JUGANDO:
                await self._iniciar_turnos()

        except Exception as e:
            await enviar(writer, {
                "tipo": "error",
                "mensaje": str(e)
            })


    async def _procesar_juego(self, jugador, mensaje):

        if mensaje.get("tipo") != "disparo":
            return

        writer = self._writers[jugador]

        try:
            resultado = self._controlador.disparar(
                jugador,
                mensaje["x"],
                mensaje["y"]
            )

            resultado_str = TRADUCCION[resultado]

            await enviar(writer, {
                "tipo": "resultado",
                "resultado": resultado_str,
                "x": mensaje["x"],
                "y": mensaje["y"]
            })

            rival = 2 if jugador == 1 else 1
            writer_rival = self._writers[rival]

            await enviar(writer_rival, {
                "tipo": "recibido",
                "resultado": resultado_str,
                "x": mensaje["x"],
                "y": mensaje["y"]
            })

            await self._enviar_estado(jugador)
            await self._enviar_estado(rival)

            if self._controlador.hay_victoria():
                await self._finalizar_partida()
            else:
                await self._actualizar_turnos()

        except Exception as e:
            await enviar(writer, {
                "tipo": "error",
                "mensaje": str(e)
            })


    async def _iniciar_turnos(self):
        turno = self._controlador.turno_actual()
        await self._actualizar_turnos()


    async def _actualizar_turnos(self):
        turno = self._controlador.turno_actual()

        for jugador, writer in self._writers.items():
            await enviar(writer, {
                "tipo": "turno",
                "tu_turno": jugador == turno
            })


    async def _finalizar_partida(self):

        ganador = self._controlador.jugador_ganador()

        for jugador, writer in self._writers.items():
            await enviar(writer, {
                "tipo": "fin",
                "victoria": jugador == ganador
            })


    async def _enviar_estado(self, jugador):

        writer = self._writers[jugador]

        estado = self._controlador.obtener_estado_tableros(jugador)

        await enviar(writer, {
            "tipo": "estado_tableros",
            "propio": estado["propio"],
            "rival": estado["rival"]
        })


    async def _enviar_barcos(self, jugador):

        writer = self._writers[jugador]

        lista = self._controlador.obtener_barcos_pendientes(jugador)

        await enviar(writer, {
            "tipo": "lista_barcos",
            "barcos": lista
        })