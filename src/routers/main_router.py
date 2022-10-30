from src.routers.router import Router
from src.exceptions.domain_expection import DomainException
from src.sys_io.console import Console
from src.exceptions.navigation_exception import NavigationException


class MainRouter(Router):
    """MainRouter es una implementación concreta de la clase Router utilizando excepciones de navegación"""

    def __init__(self):
        super().__init__()
        self.__console = Console()

    def navigate(self, route: str, message: str = None, data=None):
        # Verificamos que la ruta a navegar exista
        if (route not in self.routes):
            raise Exception('Ruta inválida')

        # Asignamos la data a manejar
        self._currentController = self.routes[route]
        self._message = message
        self._error = None
        self._data = data

        # Iniciamos la excepción de navegación
        raise NavigationException()

    def execute(self):
        while True:
            # Limpiamos consola
            self.__console.clear()

            # Si hay error lo imprimimos
            if self._error:
                self.__console.print_error(self._error)

            # Si hay mensaje lo imprimimos
            if self._message:
                self.__console.print_success(self._message)

            # Manejador de excepciones
            try:
                # Ejecutamos el controlador actual
                self._currentController.execute(self._data)
                break
            except NavigationException:
                # En caso de que ocurra un excepción de navegación ciclamos nuevamente
                pass
            except DomainException as e:
                # En caso de errores de la aplicación los mostramos por consola
                self._error = e
