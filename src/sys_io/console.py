import os


class Console:
    """Clase base para imprimir por consola"""

    def __init__(self, width=100, option_margin=4):
        self.__width: int = width
        self.__option_margin: int = option_margin

    def clear(self):
        """Clear current console according to the current OS"""
        command = 'clear'  # For Linux OS
        if os.name in ('nt', 'dos'):  # For Windows OS
            command = 'cls'
        os.system(command)

    def break_line(self):
        """Salto de linea"""
        print()

    def print_message(self, message: str = ""):
        """Print a message on the current console"""
        print(message)

    def option_message(self, option: str = "", message: str = ""):
        """ Print a menu option on the current console """
        print(" " * self.__option_margin + option + ". " + message)

    def print_error(self, error, decorator: str = "-"):
        """Imprime el mensaje de error"""
        message = 'Ha ocurrido un error inesperado!'

        print(decorator * self.__width)
        print(" " * ((self.__width - len(message) - 10) // 2), message)
        print(decorator * self.__width)
        print('[ERROR #1]:', error)
        print(decorator * self.__width)
        print()
        print()

    def print_success(self, success="", decorator: str = "-"):
        """Imprime un mensaje de exito"""
        message = 'Operación realizada exitosamente!'

        print(decorator * self.__width)
        print(" " * ((self.__width - len(message) - 10) // 2), message)
        print(decorator * self.__width)
        print(success)
        print(decorator * self.__width)
        print()
        print()

    def print_decorator(self, decorator: str = "#"):
        """Imprime una linea con un decorador"""
        print(decorator * self.__width)

    def header(self, message="", decorator: str = "#"):
        """ Print a header on the current console """
        print(decorator * self.__width)
        print(" " * ((self.__width - len(message) - 10) // 2), message)
        print(decorator * self.__width, "\n")
