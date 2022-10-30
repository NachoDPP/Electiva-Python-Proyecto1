from src.routers.router import Router
from src.sys_io.str_input import StringInput
from src.repositories.competitors_repository import CompetitorsRepository
from src.controllers.controller import Controller


from src.controllers.controller import Controller
from src.views.file_view import FileView


class FileController(Controller):
    """Controlador para el manejo de peticiones del menu de administrador de archivos"""

    def __init__(self, router: Router):
        super().__init__(router, '/file')
        self.__view = FileView(router, self)
        self.__competitors_repository = CompetitorsRepository.get_repository()

    def execute(self, data=None):
        self.__view.render()

    def load_file(self):
        """Permite cargar un archivo en función del nombre y extensión dada"""
        file_name = StringInput('Nombre del archivo: ', margin=4)
        self.__competitors_repository.load(file_name)
        self._router.navigate(
            '/file', 'Se ha cargado el archivo exitosamente!')
