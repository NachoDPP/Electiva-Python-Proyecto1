from src.controllers.controller import Controller


from src.controllers.controller import Controller
from src.views.main_view import MainView


class MainController(Controller):
    """Controlador principal de la aplicación para menu inicial"""

    def __init__(self, router):
        super().__init__(router, '/')
        self.__view = MainView(router, self)

    def execute(self, data=None):
        self.__view.render()
