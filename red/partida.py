import asyncio
import json

class Partida:

    def __init__(self, jugador1, jugador2):
        self.jugador1 = jugador1
        self.jugador2 = jugador2

        print("Nueva partida creada")

        asyncio.create_task(self.iniciar())

    async def iniciar(self):
        await self.enviar(self.jugador1, {
            "tipo": "inicio",
            "mensaje": "Partida encontrada. Eres jugador 1."
        })

        await self.enviar(self.jugador2, {
            "tipo": "inicio",
            "mensaje": "Partida encontrada. Eres jugador 2."
        })

    async def enviar(self, writer, data):
        writer.write((json.dumps(data) + "\n").encode())
        await writer.drain()
