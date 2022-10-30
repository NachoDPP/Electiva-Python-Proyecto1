from typing import Iterable
from src.exceptions.domain_expection import DomainException
from src.sys_io.int_input import NumberInput
from src.views.view import View


class ReportView(View):
    """Vista principal para imprimir reportes con los resultados obtenidos"""

    def render(self):
        option = 0

        self._console.print_decorator()
        self._console.break_line()
        self._console.option_message('0', 'Regresar')
        self._console.break_line()
        self._console.print_decorator()

        while True:
            option = NumberInput("Opcion: ")
            if option == 0:
                self._router.navigate('/action')
            else:
                self._console.print_message('Opción inválida.')
                print()

    def render_messages(self, messages: list = []):
        """Método para mostrar reporte con mensajes de una linea"""

        # Limpiamos consola
        self._console.clear()

        # Renderizamos el header
        self._console.header('REPORTE', '#')

        for message in messages:
            self._console.print_message(message)
            self._console.break_line()

        self.render()

    def render_histogram(self, title: str, headers: Iterable[str], values: Iterable[str], data: Iterable[int]):
        """Método para imprimir por consola un histograma con escala en procentaje y base 100"""
        # Limpiamos consola
        self._console.clear()

        # Renderizamos el header
        self._console.header('REPORTE', '#')

        self._console.print_message(title)

        row_separator = "-" * 100

        max_size = len(headers[0]) + len(values[0])
        for i in range(len(headers)):
            if (len(headers[i]) + len(values[i]) > max_size):
                max_size = len(headers[i]) + len(values[i])

        self._console.print_message(row_separator)

        for i in range(len(headers)):
            separator = max_size - (len(headers[i]) + len(values[i]))
            self._console.print_message(
                f'{headers[i]} ({values[i]}):{" " * separator} | {"*" * data[i]}')

        self._console.print_message(row_separator)
        self._console.break_line()

        self.render()

    def render_table(self, title: str, headers: list, data: list):
        """Método para mostrar reporte con tabla personalizada"""

        # Limpiamos consola
        self._console.clear()

        # Renderizamos el header
        self._console.header('REPORTE', '#')

        if len(data) > 0:
            self._console.print_message(title)
            self._console.break_line()

            # Calculamos el tamaño de los headers
            col_sizes: list = [len(header) for header in headers]

            # Verificamos si existen valore más grandes que los headers
            for row in data:
                for i in range(len(col_sizes)):
                    col_sizes[i] = col_sizes[i] if col_sizes[i] >= len(
                        row[i]) else len(row[i])

            # Creamos el separador horizontal
            row_separator = '-' * (sum(col_sizes, 0) + 3 * len(col_sizes) + 1)

            # Inicializamos las filas
            table_row = '|'

            for j in range(len(col_sizes)):
                table_row += "{" + ":<" + str(col_sizes[j] + 2) + "}|"

            # Formatemos elementos a la izquierda
            table_header: str = table_row.replace(":<", ":^").format(*headers)

            self._console.print_message(table_header)
            self._console.print_message(row_separator)

            # Imprimimos el resto de filas
            for row in data:
                self._console.print_message(table_row.format(*row))

            self._console.print_message(row_separator)
            self._console.break_line()
        else:
            self._console.print_message('No se encontraron registros')
            self._console.break_line()

        self.render()
