from abc import ABC


class Repository(ABC):
    """Clase base para la implementación del patrón Repository"""

    repository = None

    @classmethod
    def get_repository(cls):
        if (cls.repository):
            return cls.repository
        else:
            cls.repository = cls()
            return cls.repository
