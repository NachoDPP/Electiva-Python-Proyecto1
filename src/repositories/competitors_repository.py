from typing import Iterable
from src.DTOs.competitor_dto import CompetitorDto
from src.exceptions.file_exception import FileException
from src.repositories.repository import Repository


class CompetitorsRepository(Repository):
    """Repositorio para el manejo de persistencia de los competidores"""

    def __init__(self):
        self.__competitors = []

    @property
    def competitors(self) -> Iterable[CompetitorDto]:
        return self.__competitors

    def load(self, file_name: str):
        """Permite carga los datos de los competidores desde un archivo .txt"""
        save = self.__competitors
        self.__competitors = []
        current_line: int = 1

        try:
            if not file_name.endswith('.txt'):
                raise FileException(
                    f'Extensión inválida (*.{file_name.split(".")[-1]}), esperada: *.txt')
            with open(file_name, "r", encoding="utf-8") as competitor_file:
                for competitor_data in competitor_file:
                    competitor = competitor_data.split(",")

                    if len(competitor) < 10:
                        raise FileException(
                            f'Error en la [Fila #{current_line}]: Fila incompleta.')

                    self.__competitors.append(
                        CompetitorDto(
                            int(competitor[0].strip()),
                            competitor[1].strip(),
                            competitor[2].strip(),
                            competitor[3].strip(),
                            competitor[4].strip(),
                            competitor[5].strip(),
                            int(competitor[6].strip()),
                            int(competitor[7].strip()),
                            int(competitor[8].strip()),
                            int(competitor[9].rstrip())
                        )
                    )

                    current_line += 1
        except FileNotFoundError as e:
            self.__competitors = save
            raise FileException(
                f'No se encontró el archivo de nombre \"{file_name}\"')
        except ValueError as e:
            self.__competitors = save
            raise FileException(f'Error en la [FILA #{current_line}]: ${e}')
        except FileException as e:
            self.__competitors = save
            raise e
        except Exception as e:
            self.__competitors = save
            raise FileException(
                f'Ha ocurrido un error al tratar de cargar el archivo \"{file_name}\"')
