class Interfaz:
    def __init__(self, textos, utils):
        """
        Inicializa una interfaz con textos para el usuario
        y validaciones de entrada
        
        :param textos: Objeto de la clase textos que contiene los mensajes para el usuario
        :type textos: Texto
        :param utils: Objeto de la clase Utils para validar inputs
        :type utils: Utils
        """
        self.textos = textos
        self.utils = utils


    def lanzar_mensaje(self, key):
        """
        Lanza un mensaje al usuario

        :param key: Clave para los textos del objeto Textos.
        :type key: str
        :return: None
        """
        print(self.textos.obtener_texto[key])
    

    def error_no_entero(self, valor, key):
        """
        Imprime el texto de error correspondiente 
        si el usuario no ha introducido un entero
        
        :param valor: Valor introducido por el usuario.
        :type valor: str
        :param key: Clave para los textos del objeto Textos.
        :type key: str
        :return: None
        """
        if not self.utils.es_numero_entero(valor):
            print(self.lanzar_mensaje(key))


    def pedir_coordenada(self, key):
        """
        Pide una coordenada por teclado y devuelve su valor
        
        :param key: Clave para los textos del objeto Textos.
        :type key: str
        :return: Valor introducido por el usuario.
        :rtype: str
        """
        value = input(self.lanzar_mensaje(key))
        return value
