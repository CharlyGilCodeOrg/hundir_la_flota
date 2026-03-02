from red.globales import enviar
import asyncio
import json


class ClientePVP:

    def __init__(self, host="127.0.0.1", port=8888):
        self.host = host
        self.port = port
        self.reader = None
        self.writer = None

        self.jugador_num = None
        self.estado = None
        self.mi_turno = False
        self.colocando = False
        self.activo = True


    async def conectar(self):
        print("Conectando al servidor...")
        self.reader, self.writer = await asyncio.open_connection(
            self.host,
            self.port
        )
        print("Conectado correctamente.")


    async def escuchar_servidor(self):
        try:
            while self.activo:
                data = await self.reader.readline()
                if not data:
                    print("Servidor cerró la conexión.")
                    break

                mensaje = json.loads(data.decode().strip())
                await self.procesar_mensaje(mensaje)

        except Exception as e:
            print("Error escuchando servidor:", e)


    async def procesar_mensaje(self, mensaje):
        tipo = mensaje.get("tipo")

        if tipo == "espera":
            print(mensaje["mensaje"])

        elif tipo == "inicio":
            self.jugador_num = mensaje["jugador"]
            self.estado = mensaje["estado"]

            print(f"Eres jugador {self.jugador_num}")
            print("Fase de colocación iniciada.")
            print("Escribe 'salir' en cualquier momento para abandonar la partida.")
            self.colocando = True
            asyncio.create_task(self.fase_colocacion())

        elif tipo == "confirmacion":
            print(mensaje["mensaje"])

        elif tipo == "error":
            print("Error:", mensaje["mensaje"])

        elif tipo == "turno":
            self.mi_turno = mensaje["tu_turno"]

            if self.mi_turno:
                print("Es tu turno.")
                asyncio.create_task(self.fase_turno())
            else:
                print("Turno del rival.")

        elif tipo == "resultado":
            print(f"Disparo en ({mensaje['x']},{mensaje['y']}): {mensaje['resultado']}")

        elif tipo == "recibido":
            print(f"Te dispararon en ({mensaje['x']},{mensaje['y']}): {mensaje['resultado']}")

        elif tipo == "fin":
            if mensaje.get("victoria"):
                print("Has ganado.")
            else:
                print("Has perdido.")

            if "motivo" in mensaje:
                print("Motivo:", mensaje["motivo"])

            print("Partida finalizada.")
            self.activo = False
            self.writer.close()
            await self.writer.wait_closed()


    async def input_async(self, mensaje):
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, input, mensaje)


    async def leer_entero(self, mensaje):
        while True:
            valor = await self.input_async(mensaje)

            if valor.lower() == "salir":
                await self.salir_partida()
                return None

            try:
                return int(valor)
            except ValueError:
                print("Debes introducir un número válido.")


    async def fase_colocacion(self):
        while self.colocando and self.activo:
            caracter = await self.input_async("Carácter del barco: ")

            if caracter.lower() == "salir":
                await self.salir_partida()
                return

            x = await self.leer_entero("X: ")
            if x is None:
                return

            y = await self.leer_entero("Y: ")
            if y is None:
                return

            while True:
                orientacion = await self.input_async("Horizontal (s/n): ")

                if orientacion.lower() == "salir":
                    await self.salir_partida()
                    return

                if orientacion.lower() in ("s", "n"):
                    horizontal = orientacion.lower() == "s"
                    break

                print("Debes introducir 's' o 'n'.")

            tamanyo = await self.leer_entero("Tamaño: ")
            if tamanyo is None:
                return

            nombre = await self.input_async("Nombre barco: ")

            if nombre.lower() == "salir":
                await self.salir_partida()
                return

            await enviar(self.writer, {
                "tipo": "colocar",
                "caracter": caracter,
                "x": x,
                "y": y,
                "horizontal": horizontal,
                "tamanyo": tamanyo,
                "barco_nombre": nombre
            })


    async def fase_turno(self):
        if not self.mi_turno or not self.activo:
            return

        x = await self.leer_entero("Coordenada X del disparo: ")
        if x is None:
            return

        y = await self.leer_entero("Coordenada Y del disparo: ")
        if y is None:
            return

        await enviar(self.writer, {
            "tipo": "disparo",
            "x": x,
            "y": y
        })


    async def salir_partida(self):
        print("Saliendo de la partida...")
        self.activo = False

        await enviar(self.writer, {
            "tipo": "salir"
        })

        self.writer.close()
        await self.writer.wait_closed()


    async def ejecutar(self):
        await self.conectar()
        await self.escuchar_servidor()


if __name__ == "__main__":
    cliente = ClientePVP()
    asyncio.run(cliente.ejecutar())
