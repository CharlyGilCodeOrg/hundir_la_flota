"""
Punto de entrada del juego Hundir la Flota.
"""

from dominio.tablero import Tablero
from dominio.juego import Juego
from dominio.barco import Barco
from interfaz.interfaz_consola import InterfazConsola
from interfaz.menu import Menu
from utils.utils import Util
from utils.excepciones import SalirDelPrograma, VolverAlMenu
from config.textos import TEXTOS

def main():

    validador = Util()
    interfaz = InterfazConsola(TEXTOS, validador)
    menu = Menu(interfaz)

    try:
        while True:

            menu.ejecutar()

            CARACTER_VACIO = "~"
            CARACTER_TOCADO = "X"
            CARACTER_AGUA = "O"
            DISPAROS_MAXIMOS = 50

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

                    interfaz.opcion_volver_menu()

                    x, y = interfaz.pedir_disparo(
                        tablero_interno.ancho,
                        tablero_interno.alto
                    )

                    resultado = juego.disparar(x, y)

                    interfaz.borrar_consola()
                    interfaz.mostrar_resultado(resultado)
                    interfaz.mostrar_tablero(tablero_usuario)
                    interfaz.mostrar_balas(juego.disparos_restantes())

                interfaz.mostrar_mensaje_final(juego.hay_victoria())

            except VolverAlMenu:
                interfaz.borrar_consola()
                continue  # vuelve al menú

    except SalirDelPrograma:
        interfaz.fin_programa()

if __name__ == "__main__":
    main()