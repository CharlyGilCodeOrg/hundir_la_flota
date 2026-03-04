class ControladorCliente:

    def __init__(self, red, vista, modelo) -> None:
        self._red = red
        self._vista = vista
        self._modelo = modelo


    async def iniciar(self) -> None:
        await self._red.conectar()

        while True:
            datos = await self._red.recibir()

            self._modelo.actualizar(datos)

            self._renderizar()

            if self._modelo.estado_partida == "FINALIZADA":
                break

            if self._modelo.turno:
                await self._gestionar_turno()


    def _renderizar(self) -> None:
        self._vista.mostrar_mensaje("Tu tablero:")
        self._vista.mostrar_tablero(self._modelo.tablero_propio)

        self._vista.mostrar_mensaje("Tablero rival:")
        self._vista.mostrar_tablero(self._modelo.tablero_rival)


    async def _gestionar_turno(self) -> None:
        self._vista.mostrar_mensaje("Es tu turno")

        x, y = self._vista.pedir_coordenadas()

        await self._red.enviar({
            "accion": "disparo",
            "x": x,
            "y": y
        })
