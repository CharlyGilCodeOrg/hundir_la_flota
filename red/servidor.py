from partida import Partida
import asyncio
import json

cola_espera = []
partidas_activas = []

async def enviar(writer, data):
    writer.write((json.dumps(data) + "\n").encode())
    await writer.drain()

class Servidor:

    def __init__(self, host="127.0.0.1", port=8888):
        self.host = host
        self.port = port

        # Más adelante añadir:
        # self.cola_espera = []
        # self.partidas = {}

    async def iniciar(self):
        server = await asyncio.start_server(
            self._manejar_cliente,
            self.host,
            self.port
        )

        print(f"Servidor escuchando en {self.host}:{self.port}")

        async with server:
            await server.serve_forever()

    async def _manejar_cliente(self, reader, writer):
        addr = writer.get_extra_info("peername")
        print(f"Cliente conectado desde {addr}")
        
        cola_espera.append(writer)
        
        await enviar(writer, {
            "tipo": "espera",
            "mensaje": "Esperando rival..."
        })
        
        if len(cola_espera) >= 2:
            j1 = cola_espera.pop(0)
            j2 = cola_espera.pop(0)

            partida = Partida(j1, j2)
            partidas_activas.append(partida)


        try:
            while True:
                data = await reader.readline()

                if not data:
                    # Cliente cerró conexión
                    break

                mensaje = data.decode().strip()

                try:
                    mensaje_json = json.loads(mensaje)
                    print(f"Mensaje recibido de {addr}: {mensaje_json}")

                    # Respuesta simple de prueba
                    respuesta = {
                        "type": "ACK",
                        "message": "Mensaje recibido correctamente"
                    }

                    await self._enviar(writer, respuesta)

                except json.JSONDecodeError:
                    print("Mensaje no es JSON válido")

        except ConnectionResetError:
            print(f"Conexión perdida con {addr}")

        finally:
            print(f"Cliente desconectado: {addr}")
            writer.close()
            await writer.wait_closed()

    async def _enviar(self, writer, mensaje):
        data = json.dumps(mensaje) + "\n"
        writer.write(data.encode())
        await writer.drain()


if __name__ == "__main__":
    servidor = Servidor()
    asyncio.run(servidor.iniciar())
