class TextosJuego:
    def __init__(self, textos):
        """
        Inicializa los textos utilizados por la interfaz del juego.

        :param textos: Diccionario con los mensajes que se mostrarán al usuario,
                       organizados por contexto de uso (entrada, disparos,
                       errores y fin de partida).
        :type textos: dict[str, str]

        El diccionario debe incluir, al menos, las siguientes claves:
        - TEXTO_POSICION_X
        - TEXTO_POSICION_Y
        - TEXTO_TOCADO
        - TEXTO_AGUA
        - TEXTO_REPETIDO
        - TEXTO_BALAS_RESTANTES
        - TEXTO_VICTORIA
        - TEXTO_DERROTA
        - ERROR_LIMITE_TABLERO
        - ERROR_NUMERO_ENTERO
        - SALTO_DE_LINEA
        """
        self.textos = textos

    def obtener_texto(self, clave):
        """
        Devuelve un texto concreto en función de la clave
        
        :param clave: Clave del texto dentro del objeto
        :type clave: str
        :return: Texto específico.
        :rtype: str
        """
        return self.textos[clave]