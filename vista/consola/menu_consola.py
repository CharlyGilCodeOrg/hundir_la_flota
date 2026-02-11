from utils.excepciones import SalirDelPrograma

class Menu:

    def __init__(self, interfaz):
        """
        Inicializa un menú con opciones para que el usuario interactúe
        """
        self._interfaz = interfaz


    def ejecutar_menu_principal(self):
        """
        Ejecuta el menú principal mostrando las opciones hasta que el usuario inicie el juego o decida salir.
        
        :return: El valor devuelto por el menú de dificultad cuando el usuario selecciona jugar.
        :rtype: str
        :raises SalirDelPrograma: Si el usuario selecciona la opción de salir.
        """
        while True:
            opcion = self._menu_principal()

            match opcion:
                case "1":
                    return self.ejecutar_menu_dificultad()
                case "2":
                    self._interfaz.mostrar_instrucciones()
                case "3":
                    raise SalirDelPrograma()
                case _:
                    print("Opción no válida")

    
    def ejecutar_menu_dificultad(self):
        """
        Ejecuta el menú de dificultad.
        
        :return: El número correspondiente a la opción.
        :rtype: int
        """
        while True:
            opcion = self._menu_dificultad()

            match opcion:
                case "1":
                    return 1
                case "2":
                    return 2
                case "3":
                    return 3
                case _:
                    print("Opción no válida")


    def _menu_principal(self):
        """
        Muestra las opciones del menú principal y solicita una opción al usuario.
        
        :return: Opción introducida por el usuario.
        :rtype: str
        """
        print("")
        print("HUNDIR LA FLOTA")
        print("")
        print("1. Jugar")
        print("2. Instrucciones")
        print("3. Salir")
        print("")
        return input("Seleccione opción: ")
    

    def _menu_dificultad(self):
        """
        Muestra las dificultades.
        
        :return: Opción introducida por el usuario.
        :rtype: str
        """
        self._interfaz.borrar_consola()
        print("")
        print("Dificultad")
        print("")
        print("1. Fácil")
        print("2. Media")
        print("3. Difícil")
        print("")
        return input("Seleccione opción: ")