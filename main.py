"""
Punto de entrada del juego Hundir la Flota.
"""

from dominio.tablero import Tablero
from dominio.juego import Juego
from dominio.barco import Barco
from interfaz.interfaz_consola import InterfazConsola
from utils.utils import Util
from utils.excepciones import SalirDelJuego
from config.textos import TEXTOS


def main():
    """
    Ejecuta el juego Hundir la Flota.
    """
    validador = Util()
    interfaz = InterfazConsola(TEXTOS, validador)

    # Constantes
    CARACTER_VACIO = "~"
    CARACTER_TOCADO = "X"
    CARACTER_AGUA = "O"
    DISPAROS_MAXIMOS = 50

    # Barcos
    portaaviones = Barco(4, 1, "P")
    destructores = Barco(3, 2, "D")
    submarinos = Barco(2, 3, "S")

    barcos = [portaaviones, destructores, submarinos]

    tablero_usuario = Tablero(10, 10, barcos, CARACTER_VACIO)
    tablero_interno = Tablero(10, 10, barcos, CARACTER_VACIO)
    juego = Juego(
        tablero_usuario,
        tablero_interno,
        DISPAROS_MAXIMOS,
        CARACTER_VACIO,
        CARACTER_TOCADO,
        CARACTER_AGUA
    )

    try:
        while juego.quedan_disparos() and not juego.hay_victoria():
            
            interfaz.opcion_fin_programa()
            x, y = interfaz.pedir_disparo(
                tablero_interno.ancho,
                tablero_interno.alto
            )

            resultado = juego.disparar(x, y)

            interfaz.borrar_consola()
            interfaz.mostrar_resultado(resultado)
            interfaz.mostrar_tablero(tablero_usuario)
            interfaz.mostrar_balas(DISPAROS_MAXIMOS - juego.disparos_realizados)

    except SalirDelJuego:
        interfaz.fin_programa()
        return

    interfaz.mostrar_mensaje_final(juego.hay_victoria())


if __name__ == "__main__":
    main()