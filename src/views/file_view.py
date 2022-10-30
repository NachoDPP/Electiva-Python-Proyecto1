from src.exceptions.domain_expection import DomainException
from src.sys_io.int_input import NumberInput
from src.views.view import View


class FileView(View):
    """Vista principal del menú de administrador de archivos"""

    def render(self):
        option = 0

        self._console.header('ADMINISTRADOR DE ARCHIVOS', '#')
        self._console.option_message('1', 'Cargar archivo')
        self._console.option_message('0', 'Regresar')
        self._console.break_line()
        self._console.print_decorator()

        while True:
            option = NumberInput("Opcion: ")
            if option == 1:
                self._console.break_line()
                self._controller.load_file()
            elif option == 0:
                self._router.navigate('/')
            else:
                raise DomainException('Opción inválida.')
