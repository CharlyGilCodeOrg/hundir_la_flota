import asyncio
from red.globales import enviar, jugador_partida
from modelo.tablero import Tablero
from modelo.barco import Barco
from modelo.resultado import ResultadoDisparo
from config.constantes import CONSTANTES
from config.mensajes import TRADUCCION

class Partida:

    ESPERANDO_COLOCACION = "esperando_colocacion"
    JUGANDO = "jugando"
    FINALIZADA = "finalizada"
    ANCHO_TABLEROS = CONSTANTES["DIFICULTAD"]["PVP"]["ancho"]
    ALTO_TABLEROS = CONSTANTES["DIFICULTAD"]["PVP"]["alto"]
    DICT_DE_BARCOS = CONSTANTES["DIFICULTAD"]["PVP"]["barcos"]
    CARACTER_VACIO = CONSTANTES["CARACTERES"]["CARACTER_VACIO"]
    CARACTER_TOCADO = CONSTANTES["CARACTERES"]["CARACTER_TOCADO"]
    CARACTER_AGUA = CONSTANTES["CARACTERES"]["CARACTER_AGUA"]

    def __init__(self, jugador1, jugador2):
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.turno = self.jugador1
        
        barcos_j1 = self.crear_barcos()
        barcos_j2 = self.crear_barcos()
        
        self.tableros = {
            self.jugador1: Tablero(self.ANCHO_TABLEROS, self.ALTO_TABLEROS, barcos_j1, self.CARACTER_VACIO, self.CARACTER_TOCADO, self.CARACTER_AGUA),
            self.jugador2: Tablero(self.ANCHO_TABLEROS, self.ALTO_TABLEROS, barcos_j2, self.CARACTER_VACIO, self.CARACTER_TOCADO, self.CARACTER_AGUA)
        }

        # Copia superficial de la lista, NO los objetos
        self.barcos_pendientes = {
            self.jugador1: barcos_j1.copy(),
            self.jugador2: barcos_j2.copy()
        }

        self.estado = self.ESPERANDO_COLOCACION

        self.jugadores_listos = set()

        print("Nueva partida creada")

        jugador_partida[jugador1] = self
        jugador_partida[jugador2] = self

        asyncio.create_task(self.iniciar())
    
    
    def crear_barcos(self):
        return [
            Barco(nombre, tamanyo, caracter)
            for nombre, tamanyo, caracter in self.DICT_DE_BARCOS
        ]
    
        
    async def iniciar(self):
        await enviar(self.jugador1, {
            "tipo": "inicio",
            "jugador": 1,
            "estado": self.estado
        })

        await enviar(self.jugador2, {
            "tipo": "inicio",
            "jugador": 2,
            "estado": self.estado
        })
        
        await self.enviar_lista_barcos(self.jugador1)
        await self.enviar_lista_barcos(self.jugador2)



    async def recibir_mensaje(self, writer, mensaje):
        if self.estado == self.ESPERANDO_COLOCACION:
            await self.procesar_colocacion(writer, mensaje)

        elif self.estado == self.JUGANDO:
            await self.procesar_juego(writer, mensaje)


    async def procesar_colocacion(self, writer, mensaje):
        if mensaje.get("tipo") != "seleccionar_barco":
            return

        indice = mensaje.get("indice")
        x = mensaje.get("x")
        y = mensaje.get("y")
        horizontal = mensaje.get("horizontal")

        pendientes = self.barcos_pendientes[writer]

        if not indice or indice < 1 or indice > len(pendientes):
            await enviar(writer, {
                "tipo": "error",
                "mensaje": "Selección inválida"
            })
            return

        barco_info = pendientes[indice - 1]
        tablero = self.tableros[writer]

        try:
            barco = pendientes[indice - 1]
            barco.set_horizontal(horizontal)
            
            colocado = tablero.colocar_barco_manual(barco, x, y)

            if not colocado:
                await enviar(writer, {
                    "tipo": "error",
                    "mensaje": "Posición inválida"
                })
                return

        except Exception as e:
            await enviar(writer, {
                "tipo": "error",
                "mensaje": str(e)
            })
            return

        pendientes.remove(barco_info)

        await enviar(writer, {
            "tipo": "confirmacion",
            "mensaje": f"{barco_info.nombre} colocado correctamente"
        })
        
        await self.enviar_estado_tableros(writer)

        if pendientes:
            await self.enviar_lista_barcos(writer)
        else:
            self.jugadores_listos.add(writer)

            await enviar(writer, {
                "tipo": "espera",
                "mensaje": "Esperando al otro jugador..."
            })

            if len(self.jugadores_listos) == 2:
                self.estado = self.JUGANDO
                await self.comenzar_juego()


    async def procesar_juego(self, writer, mensaje):
        if mensaje.get("tipo") != "disparo":
            return

        if writer != self.turno:
            await enviar(writer, {
                "tipo": "error",
                "mensaje": "No es tu turno"
            })
            return

        x = mensaje.get("x")
        y = mensaje.get("y")

        defensor = self.oponente(writer)
        tablero_defensor = self.tableros[defensor]

        try:
            resultado_enum = self.disparar(x, y, tablero_defensor)
            resultado = self.adaptar_resultado_a_string(resultado_enum)

            await enviar(writer, {
                "tipo": "resultado",
                "resultado": resultado,
                "x": x,
                "y": y
            })

            await enviar(defensor, {
                "tipo": "recibido",
                "resultado": resultado,
                "x": x,
                "y": y
            })
            await self.enviar_estado_tableros(writer)
            await self.enviar_estado_tableros(defensor)

            if tablero_defensor.todos_hundidos():
                self.estado = self.FINALIZADA

                await enviar(writer, {
                    "tipo": "fin",
                    "victoria": True
                })

                await enviar(defensor, {
                    "tipo": "fin",
                    "victoria": False
                })

                print("Partida finalizada")
                return

            else:
                self.turno = defensor
                await enviar(self.turno, {
                    "tipo": "turno",
                    "tu_turno": True
                })

                await enviar(self.oponente(self.turno), {
                    "tipo": "turno",
                    "tu_turno": False
                })
                
        except ValueError as e:
            await enviar(writer, {
                "tipo": "error",
                "mensaje": str(e)
            })
            return


    async def comenzar_juego(self):
        self.turno = self.jugador1

        await enviar(self.jugador1, {
            "tipo": "turno",
            "tu_turno": True
        })

        await enviar(self.jugador2, {
            "tipo": "turno",
            "tu_turno": False
        })

        print("Turno inicial asignado")


    async def enviar_a_ambos(self, data):
        await enviar(self.jugador1, data)
        await enviar(self.jugador2, data)
        
        
    def oponente(self, writer):
        return self.jugador2 if writer == self.jugador1 else self.jugador1


    async def jugador_desconectado(self, writer):
        if self.estado == self.FINALIZADA:
            return

        oponente = self.oponente(writer)

        self.estado = self.FINALIZADA

        try:
            await enviar(oponente, {
                "tipo": "fin",
                "victoria": True,
                "motivo": "El rival se desconectó"
            })
        except:
            pass

        print("Partida finalizada por desconexión")


    async def enviar_lista_barcos(self, writer):
        pendientes = self.barcos_pendientes[writer]

        lista = []
        for i, barco in enumerate(pendientes, start=1):
            lista.append({
                "indice": i,
                "nombre": barco.nombre,
                "tamanyo": barco.tamanyo
            })

        await enviar(writer, {
            "tipo": "lista_barcos",
            "barcos": lista
        })


    async def enviar_estado_tableros(self, writer):
        propio = self.tableros[writer]
        rival = self.tableros[self.oponente(writer)]

        await enviar(writer, {
            "tipo": "estado_tableros",
            "propio": propio.ver_tablero(),
            "rival": rival.ver_tablero_rival()
        })


    def adaptar_resultado_a_string(self, resultado: ResultadoDisparo) -> str:
        """
        Convierte el enum a str.

        Args:
            resultado (ResultadoDisparo): Objeto de la clase ResultadoDisparo que representa un resultado.

        Returns:
            str: Cadena resultado.
        """
        return TRADUCCION[resultado]
    
    
    def disparar(self, x: int, y: int, tablero_defensor: Tablero) -> ResultadoDisparo:
        """
        Realiza un disparo sobre los tableros.

        :param x: Coordenada X.
        :type x: int
        :param y: Coordenada Y.
        :type y: int
        :return: Resultado del disparo.
        :param tablero_defensor: Tablero de la persona atacada.
        :type tablero_defensor: Tablero
        :rtype: ResultadoDisparo
        """
        [resultado, caracter] = tablero_defensor.recibir_disparo(x, y)

        return resultado