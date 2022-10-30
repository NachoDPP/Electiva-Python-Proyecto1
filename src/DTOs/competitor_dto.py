from datetime import time
from src.DTOs.converter import TryParseTime

from src.exceptions.value_exception import ValueException


class CompetitorDto:
    """Objeto de transferencia de datos de los competidores"""

    def __init__(self, id: int, first_surname: str, second_surname: str, first_name: str, middle_name: str, sex: str, age: int, hours: int, mins: int, segs: int):
        self.id = id
        self.first_surname = first_surname
        self.second_surname = second_surname
        self.first_name = first_name
        self.middle_name = middle_name
        self.sex = sex
        self.age = age
        self.finish_time = TryParseTime(hours, mins, segs)

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value: int):
        if (type(value) != int or value < 1):
            raise ValueException('CI del competidor inválido.')
        self.__id = value

    @property
    def first_surname(self):
        return self.__first_surname

    @first_surname.setter
    def first_surname(self, value: str):
        if (type(value) != str or value == ""):
            raise ValueException('Primer apellido del competidor inválido.')
        self.__first_surname = value

    @property
    def second_surname(self):
        return self.__second_surname

    @second_surname.setter
    def second_surname(self, value: str):
        if (type(value) != str or value == ""):
            raise ValueException('Segundo apellido del competidor inválido.')
        self.__second_surname = value

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value: str):
        if (type(value) != str or value == ""):
            raise ValueException('Primer nombre del competidor inválido.')
        self.__first_name = value

    @property
    def middle_name(self):
        return self.__middle_name

    @middle_name.setter
    def middle_name(self, value: str):
        if (type(value) != str or value == ""):
            raise ValueException('Segundo nombre del competidor inválido.')
        self.__middle_name = value

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, value: str):
        if (type(value) != str or value not in ['F', 'M']):
            raise ValueException('Sexo del competidor inválido.')
        self.__sex = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value: int):
        if (type(value) != int or value < 1):
            raise ValueException('Edad del competidor inválido.')
        self.__age = value

    @property
    def finish_time(self):
        return self.__finish_time

    @finish_time.setter
    def finish_time(self, value: time):
        if (type(value) != time):
            raise ValueException(
                'Tiempo de finalización del competidor inválido.')
        self.__finish_time = value

    def to_list(self):
        return [
            str(self.id),
            str(self.first_surname),
            str(self.second_surname),
            str(self.first_name),
            str(self.middle_name),
            str(self.sex),
            str(self.age),
            str(self.finish_time)
        ]
