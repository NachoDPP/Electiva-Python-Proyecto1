from abc import abstractmethod, ABC
from src.controllers.controller import Controller

from src.sys_io.console import Console
from src.routers.router import Router


class View(ABC):
    """Clase base para la implementación de vistas en la aplicación"""

    def __init__(self, router: Router, controller: Controller):
        if (not router):
            raise Exception('Not router were found.')
        self._controller = controller
        self._console = Console()
        self._router = router

    @abstractmethod
    def render():
        """Método para renderizar la vista"""
        pass
