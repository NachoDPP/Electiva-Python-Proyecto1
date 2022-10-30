from src.exceptions.domain_expection import DomainException
from src.sys_io.int_input import NumberInput
from src.views.view import View


class MainView(View):
    """Vista del menú principal de la aplicación"""

    def render(self):
        option = 0

        self._console.header('MAIN MENU', '#')
        self._console.option_message('1', 'Acciones')
        self._console.option_message('2', 'Archivos')
        self._console.option_message('0', 'Salir')
        self._console.break_line()
        self._console.print_decorator()

        while True:
            option = NumberInput("Opcion: ")
            if option == 1:
                self._router.navigate('/action')
            elif option == 2:
                self._router.navigate('/file')
            elif option == 0:
                break
            else:
                raise DomainException('Opción inválida.')
