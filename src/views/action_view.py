from src.exceptions.domain_expection import DomainException
from src.sys_io.int_input import NumberInput
from src.views.view import View


class ActionView(View):
    """Vista principal del menú de administrador de acciones"""

    def render(self):
        option = 0

        self._console.header('ADMINISTRADOR DE ACCIONES', '#')
        self._console.option_message('1', 'Lista con la totalidad de participantes')
        self._console.option_message('2', 'Cantidad total de participantes')
        self._console.option_message('3', 'Cantidad de participantes por grupo etario')
        self._console.option_message('4', 'Cantidad de participantes por sexo')
        self._console.option_message('5', 'Ganadores por grupo etario')
        self._console.option_message('6', 'Ganadores por sexo')
        self._console.option_message('7', 'Ganadores por grupo etario y sexo')
        self._console.option_message('8', 'Ganador general')
        self._console.option_message('9', 'Histograma de participante por grupo etario')
        self._console.option_message('10', 'Promedio de tiempo por grupo etario y sexo')
        self._console.option_message('0', 'Regresar')
        self._console.break_line()
        self._console.print_decorator()

        while True:
            option = NumberInput("Opcion: ")
            if option == 1:
                self._controller.find_all()
            elif option == 2:
                self._controller.count_all()
            elif option == 3:
                self._controller.count_by_etarios()
            elif option == 4:
                self._controller.count_by_sex()
            elif option == 5:
                self._controller.winners_by_etarios()
            elif option == 6:
                self._controller.winners_by_sex()
            elif option == 7:
                self._controller.winners_by_sex_and_etarios()
            elif option == 8:
                self._controller.main_winner()
            elif option == 9:
                self._controller.histogram_by_etarios()
            elif option == 10:
                self._controller.average_by_etarios_and_sex()
            elif option == 0:
                self._router.navigate('/')
            else:
                raise DomainException('Opción inválida.')
