from modelo.tablero import Tablero
from modelo.partida.partida_pve import PartidaPVE
from modelo.barco import Barco
from vista.consola.vista_consola_pve import VistaConsolaPVE
from vista.consola.menu_consola_pve import Menu
from utils.excepciones import VolverAlMenu
from controlador.controlador import Controlador
from modelo.resultado import ResultadoDisparo

class ControladorPVE(Controlador):
    def __init__(self, constantes: dict, interfaz: VistaConsolaPVE, menu: Menu, indice_dificultad: int) -> None:
        """
        Inicializa el controlador PVE.
        """
        self._interfaz = interfaz
        self._menu = menu
        self._constantes = constantes
        self._partida_pve = self.crear_partida(indice_dificultad)
        self._ejecutar = self.ejecutar_partida(self._partida_pve)
        
    def crear_partida(self, dificultad: int) -> PartidaPVE:
        """
        Crea e inicializa una nueva partida pve.

        :param dificultad: Índice para la dificultad.
        :type dificultad: int
        :return: Objeto PartidaPVE inicializado.
        :rtype: PartidaPVE
        """
        config_dificultad = self._constantes["DIFICULTAD"]["PVE"][dificultad]
        caracteres = self._constantes["CARACTERES"]
        barcos = self._crear_barcos(config_dificultad["barcos"])

        tablero_maquina = Tablero(
            config_dificultad["ancho"],
            config_dificultad["alto"],
            barcos,
            caracteres["CARACTER_VACIO"],
            caracteres["CARACTER_TOCADO"],
            caracteres["CARACTER_AGUA"]
        )

        return PartidaPVE(
            tablero_maquina,
            config_dificultad["disparos"]
        )


    def ejecutar_partida(self) -> None:
        """
        Ejecuta el bucle principal de una partida pve.
        """
        try:
            ancho, alto = self.obtener_dimensiones_tablero()
            self._interfaz.borrar_consola()
            self._interfaz.mostrar_tablero(self.obtener_tablero_rival())
            
            while self._partida_pve.quedan_disparos() and not self.hay_victoria():
                self._interfaz.opcion_volver_menu()
                x, y = self._interfaz.pedir_disparo(
                    ancho,
                    alto
                )

                resultado_enum = self.disparar(x, y)

                self._interfaz.borrar_consola()
                self._interfaz.mostrar_tablero(self.obtener_tablero_rival())
                self._interfaz.mostrar_resultado(resultado_enum)
                self._interfaz.mostrar_balas(self.disparos_restantes())

            self._interfaz.mostrar_mensaje_final(self.hay_victoria())

        except VolverAlMenu:
            self._interfaz.borrar_consola()
            
            
    def crear_barcos(self, config_barcos: list) -> list:
        return [
            Barco(nombre, tamanyo, caracter)
            for nombre, tamanyo, caracter in config_barcos
        ]

    
    def hay_victoria(self) -> bool:
        return self._partida_pve.hay_victoria()
    
    
    def quedan_disparos(self) -> bool:
        return self._partida_pve.quedan_disparos()
    
    
    def obtener_tablero_rival(self) -> list:
        return self._partida_pve.obtener_tablero_rival()
    
    
    def obtener_dimensiones_tablero(self) -> tuple[int, int]:
        return self._partida_pve.obtener_dimensiones_tablero()
    
    
    def disparar(self, x: int, y: int) -> ResultadoDisparo:
        return self._partida_pve.disparar(x, y)
    
    
    def disparos_restantes(self) -> int:
        return self._partida_pve.disparos_restantes()