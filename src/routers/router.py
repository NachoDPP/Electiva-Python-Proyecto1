from abc import abstractmethod, ABC


class Router(ABC):
    """Clase base para la implementación de manejadores de Rutas"""

    def __init__(self):
        self.routes: dict = {}
        self._data = None
        self._error = None
        self._message = None
        self._currentController = None

    def register(self, controller):
        """Registra los controladores con sus rutas respectivas"""
        self.routes[controller.route] = controller

    @abstractmethod
    def navigate(self, route: str, message: str = "", data=None):
        """Método principal para navegar entre controladores a través de un ruta"""
        pass

    @abstractmethod
    def execute(self):
        """Método principal de ejecución del Router"""
        pass
