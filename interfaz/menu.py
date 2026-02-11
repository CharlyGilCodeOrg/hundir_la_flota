from utils.excepciones import SalirDelPrograma

class Menu:

    def __init__(self, interfaz):
        """
        Inicializa un menú con opciones para que el usuario interactúe
        """
        self._interfaz = interfaz


    def ejecutar(self):
        """
        Docstring for ejecutar
        
        :param self: Description
        """
        while True:
            opcion = self._mostrar_opciones()

            match opcion:
                case "1":
                    return "JUGAR"
                case "2":
                    raise SalirDelPrograma()
                case _:
                    print("Opción no válida")


    def _mostrar_opciones(self):
        """
        Docstring for _mostrar_opciones
        
        :param self: Description
        """
        print("")
        print("HUNDIR LA FLOTA")
        print("")
        print("1. Jugar")
        print("2. Salir")
        print("")
        return input("Seleccione opción: ")
