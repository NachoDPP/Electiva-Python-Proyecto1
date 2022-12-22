<p align="center">
  <a href="https://fastapi.tiangolo.com"><img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI"></a>
</p>
<p align="center">
    <em>FastAPI framework, high performance, easy to learn, fast to code, ready for production</em>
</p>
<p align="center">
<a href="https://github.com/tiangolo/fastapi/actions?query=workflow%3ATest+event%3Apush+branch%3Amaster" target="_blank">
    <img src="https://github.com/tiangolo/fastapi/workflows/Test/badge.svg?event=push&branch=master" alt="Test">
</a>
<a href="https://coverage-badge.samuelcolvin.workers.dev/redirect/tiangolo/fastapi" target="_blank">
    <img src="https://coverage-badge.samuelcolvin.workers.dev/tiangolo/fastapi.svg" alt="Coverage">
</a>
<a href="https://pypi.org/project/fastapi" target="_blank">
    <img src="https://img.shields.io/pypi/v/fastapi?color=%2334D058&label=pypi%20package" alt="Package version">
</a>
<a href="https://pypi.org/project/fastapi" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/fastapi.svg?color=%2334D058" alt="Supported Python versions">
</a>
</p>

# Electiva-Python-Proyecto1 - Manuel Da Pena
Proyecto Práctico 1 de la materia electiva Programación con Python de Ingeniería Informática en la Universidad Católica Andrés Bello.

## Descripción

Una empresa que organiza competiciones le ha contratado a usted para que le desarrolle una aplicación que le permita analizar los resultados de su última competencia. Ha requerimiento suyo los datos de la competencia le serán suministrado en un archivo txt, el cual contendrá en cada línea los datos separados por coma de cada participante.


## Instrucciones

- Lee cuidadosamente todo el texto del proyecto antes de empezar a trabajar, si tiene alguna duda, consulte al profesor, según las condiciones al final del texto.
- Use una estructura de carpetas (paquetes) que permita la separación de las diferentes partes de la aplicación. Se sugiere una para la vista, otra para la parte de obtención de datos, una para el manejo de excepciones y una para su procesamiento (controlador).
- El archivo suministrado contiene en cada línea la siguiente información separada por comas:
  - CI, 1er Apellido, 2do Apellido, Nombre, Inicial 2do Nombre, Sexo, Edad, Horas, Minutos y Segundos.
- La ventana principal del proyecto debe contener un menú para manejar las opciones y acciones de la aplicación: Archivo y Acciones. Desde el menú Archivo se podrá Seleccionar Cargar Archivo, para escoger el archivo que contendrá los datos y Salir, para salirse de la aplicación.
- En Acciones se mostrarán diversas acciones de acuerdo a lo que el usuario desee ver, de acuerdo a los resultados que se solicitan más abajo.
- Los resultados solicitados serán mostrados en dos maneras: 
  - Si el resultado solicitado es de una línea, se presentará en una sola línea.
  - Si el resultado involucra varios datos se debe presentar en una tabla formateada sobre la salida estándar, usando los comandos aprendidos en clase para el formateo 
de strings y el uso de print.
- Los participantes se dividen en grupos etarios (por edad) y por sexo. Los grupos etarios son:
  - Juniors, iguales o menores a 25 años.
  - Seniors, mayores de 25 y menores o iguales a 40 años.
  - Masters, mayores de 40 años.
- Los resultados a mostrar, usando diversos menús de selección en la opción Acciones son:
  - Lista con la totalidad de participantes (tabla).
  - Cantidad total de participantes (una línea).
  - Cantidad de participantes por grupo etario (tabla, solo el grupo y la cantidad).
  - Cantidad de participantes por sexo (línea, sólo el grupo y la cantidad).
  - Ganadores por grupo etario (tabla).
  - Ganadores por sexo (tabla).
  - Ganadores por grupo etario y sexo (tabla).
  - Ganador general (línea).
  - Histograma de participante por grupo etario.
  - Promedio de tiempo por grupo etario y sexo.
-  Se considera ganador al participante que ha empleado menos tiempo en ejecutar la competencia.
-  Después de presentar cada acción del menú debe existir una opción para retornar al menú principal.
- La aplicación debe estar activa mientras el usuario no seleccione la opción de salir del menú Archivos.

## Las excepciones y mensajes
La aplicación debe ser capaz de suministrar información al usuario cuando cargue un archivo que no sea el correcto, es decir que no sea un archivo .txt. Las excepciones que debe manejar el sistema, con sus respectivos mensajes son:

- Tipo de archivo incorrecto (para validar que sea txt).
- Cantidad de columnas incorrecto (las líneas tienen la información indicada anteriormente).

Al producirse cualquier de los fallos mencionados debe notificar al usuario con un mensaje y permitiéndole repetir la acción de forma correcta.
