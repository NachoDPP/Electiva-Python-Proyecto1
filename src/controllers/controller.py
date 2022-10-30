from abc import abstractmethod, ABC

from src.routers.router import Router


class Controller(ABC):
    """Controller es una clase base para las implementaciones de un controlador"""

    def __init__(self, router: Router, route: str):
        if (not router):
            raise Exception('No se encontró la referencia al router')

        if (not route):
            raise Exception('No se encontró la ruta asignada')

        self._router: Router = router
        self.route: str = route

    @abstractmethod
    def execute(self, data=None):
        """Método principal del controlador"""
        pass
