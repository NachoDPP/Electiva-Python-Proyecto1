from src.exceptions.navigation_exception import NavigationException
from src.controllers.action_controller import ActionController
from src.controllers.file_controller import FileController
from src.controllers.main_controller import MainController
from src.routers.main_router import MainRouter

# Controladores registrados en la aplicación
controllers: list = [
    MainController,
    FileController,
    ActionController
]


def main():
    """Método principal para iniciar la aplicación"""
    # Creamos el router
    router = MainRouter()

    # Registramos todos los controladores
    for controller in controllers:
        router.register(controller(router))

    # Nos dirigimos a la ruta inicial "/"
    try:
        router.navigate('/')
    except NavigationException:
        router.execute()
    except BaseException as e:
        print('La aplicación ha fallado')
        print(e)
    finally:
        print('Saliendo...')


if __name__ == '__main__':
    main()
