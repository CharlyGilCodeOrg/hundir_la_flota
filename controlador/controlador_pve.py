from modelo.tablero import Tablero
from modelo.partida.partida_pve import PartidaPVE
from modelo.barco import Barco
from vista.consola.vista_consola_pve import VistaConsolaPVE
from vista.consola.menu_consola_pve import Menu
from utils.excepciones import VolverAlMenu
from controlador.controlador import Controlador
from config.constantes import CONSTANTES

class ControladorPVE(Controlador):
    def __init__(self, interfaz: VistaConsolaPVE, menu: Menu) -> None:
        """
        Inicializa el controlador PVE.
        """
        self._interfaz = interfaz
        self._menu = menu
        
        
    def crear_partida(self, dificultad: int) -> PartidaPVE:
        """
        Crea e inicializa una nueva partida pve.

        :param dificultad: Índice para la dificultad.
        :type dificultad: int
        :return: Objeto PartidaPVE inicializado.
        :rtype: PartidaPVE
        """
        config_dificultad = CONSTANTES["DIFICULTAD"]["PVE"][dificultad]
        caracteres = CONSTANTES["CARACTERES"]

        barcos = [
            Barco(nombre, longitud, identificador)
            for nombre, longitud, identificador in config_dificultad["barcos"]
        ]

        tablero_usuario = Tablero(
            config_dificultad["ancho"],
            config_dificultad["alto"],
            barcos,
            caracteres["CARACTER_VACIO"],
            caracteres["CARACTER_TOCADO"],
            caracteres["CARACTER_AGUA"]
        )

        tablero_maquina = Tablero(
            config_dificultad["ancho"],
            config_dificultad["alto"],
            barcos,
            caracteres["CARACTER_VACIO"],
            caracteres["CARACTER_TOCADO"],
            caracteres["CARACTER_AGUA"]
        )

        return PartidaPVE(
            tablero_usuario,
            tablero_maquina,
            config_dificultad["disparos"]
        )


    def ejecutar_partida(self, partida_pve: PartidaPVE) -> None:
        """
        Ejecuta el bucle principal de una partida pve.

        :param partida_pve: Instancia de la partida pve en curso.
        :type partida_pve: PartidaPVE
        """
        try:
            ancho, alto = partida_pve.obtener_dimensiones_tablero()
            self._interfaz.borrar_consola()
            self._interfaz.mostrar_tablero(partida_pve.obtener_tablero_rival())
            
            while partida_pve.quedan_disparos() and not partida_pve.hay_victoria():
                self._interfaz.opcion_volver_menu()
                x, y = self._interfaz.pedir_disparo(
                    ancho,
                    alto
                )

                resultado_enum = partida_pve.disparar(x, y)

                self._interfaz.borrar_consola()
                self._interfaz.mostrar_tablero(partida_pve.obtener_tablero_rival())
                self._interfaz.mostrar_resultado(resultado_enum)
                self._interfaz.mostrar_balas(partida_pve.disparos_restantes())

            self._interfaz.mostrar_mensaje_final(partida_pve.hay_victoria())

        except VolverAlMenu:
            self._interfaz.borrar_consola()