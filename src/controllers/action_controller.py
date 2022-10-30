import datetime
from typing import Iterable
from src.DTOs.competitor_dto import CompetitorDto
from src.routers.router import Router
from src.repositories.competitors_repository import CompetitorsRepository
from src.controllers.controller import Controller


from src.views.action_view import ActionView
from src.views.report_view import ReportView


class ActionController(Controller):
    """Controlador para el manejo de peticiones del menu de principal de acciones"""

    def __init__(self, router: Router):
        super().__init__(router, '/action')
        self.__view = ActionView(router, self)
        self.__competitors_repository = CompetitorsRepository.get_repository()
        self.__report_view = ReportView(router, self)

    def execute(self, data=None):
        self.__view.render()

    def find_all(self):
        """Lista con la totalidad de participantes (tabla)"""

        if (len(self.__competitors_repository.competitors) == 0):
            self.__report_view.render_messages(['No se encontraron registros'])
        else:
            self.__report_view.render_table(
                "Lista de participantes",
                [
                    'Cédula',
                    'Primer Apellido',
                    'Segundo Apellido',
                    'Primer Nombre',
                    'Inicial',
                    'Sexo',
                    'Edad',
                    'Tiempo'
                ],
                [i.to_list() for i in self.__competitors_repository.competitors]
            )

    def count_all(self):
        """Cantidad total de participantes (una línea)"""

        if (len(self.__competitors_repository.competitors) == 0):
            self.__report_view.render_messages(['No se encontraron registros'])
        else:
            count = len(self.__competitors_repository.competitors)
            self.__report_view.render_messages(
                [f'La cantidad de participantes es: {count}']
            )

    def count_by_etarios(self):
        """Cantidad de participantes por grupo etario (tabla, solo el grupo y la cantidad)"""

        if (len(self.__competitors_repository.competitors) == 0):
            self.__report_view.render_messages(['No se encontraron registros'])
        else:
            juniors_count = 0
            seniors_count = 0
            masters_count = 0

            for competitor in self.__competitors_repository.competitors:
                if (self.__isJunior(competitor)):
                    juniors_count += 1
                elif (self.__isSenior(competitor)):
                    seniors_count += 1
                elif (self.__isMaster(competitor)):
                    masters_count += 1

            data = [
                ['Juniors', str(juniors_count)],
                ['Seniors', str(seniors_count)],
                ['Masters', str(masters_count)],
            ]

            self.__report_view.render_table('Cantidad agrupados por etarios', [
                                            'Grupo', 'Cantidad'], data)

    def count_by_sex(self):
        """Cantidad de participantes por sexo (línea, sólo el grupo y la cantidad)"""

        if (len(self.__competitors_repository.competitors) == 0):
            self.__report_view.render_messages(['No se encontraron registros'])
        else:
            male_count = 0
            female_count = 0

            for competidor in self.__competitors_repository.competitors:
                if (competidor.sex == 'M'):
                    male_count += 1
                elif (competidor.sex == 'F'):
                    female_count += 1

            self.__report_view.render_messages(
                [
                    f'La cantidad de participantes Masculinos es: {male_count}',
                    f'La cantidad de participantes Femeninos es: {female_count}',
                ]
            )

    def winners_by_etarios(self):
        """Ganadores por grupo etario (tabla)"""

        if (len(self.__competitors_repository.competitors) == 0):
            self.__report_view.render_messages(['No se encontraron registros'])
        else:
            juniors = []
            seniors = []
            masters = []

            for competitor in self.__competitors_repository.competitors:
                if (self.__isJunior(competitor)):
                    juniors.append(competitor)
                elif (self.__isSenior(competitor)):
                    seniors.append(competitor)
                elif (self.__isMaster(competitor)):
                    masters.append(competitor)

            junior_winner = self.__find_winner(juniors)
            senior_winner = self.__find_winner(seniors)
            master_winner = self.__find_winner(masters)

            data = [
                ['Juniors', '', '', '', ''],
                ['Seniors', '', '', '', ''],
                ['Masters', '', '', '', ''],
            ]

            if (junior_winner):
                data[0] = ['Juniors', str(junior_winner.id), str(junior_winner.first_name), str(
                    junior_winner.first_surname), str(junior_winner.finish_time)]

            if (senior_winner):
                data[1] = ['Seniors', str(senior_winner.id), str(senior_winner.first_name), str(
                    senior_winner.first_surname), str(senior_winner.finish_time)]

            if (master_winner):
                data[2] = ['Masters', str(master_winner.id), str(master_winner.first_name), str(
                    master_winner.first_surname), str(master_winner.finish_time)]

            self.__report_view.render_table(
                'Ganadores agrupados por etarios',
                [
                    'Grupo',
                    'Cédula',
                    'Primer Nombre',
                    'Primer Apellido',
                    'Tiempo'
                ],
                data
            )

    def winners_by_sex(self):
        """Ganadores por sexo (tabla)"""

        if (len(self.__competitors_repository.competitors) == 0):
            self.__report_view.render_messages(['No se encontraron registros'])
        else:
            males = []
            females = []

            for competidor in self.__competitors_repository.competitors:
                if (competidor.sex == 'M'):
                    males.append(competidor)
                elif (competidor.sex == 'F'):
                    females.append(competidor)

            male_winner = self.__find_winner(males)
            female_winner = self.__find_winner(females)

            data = [
                ['Masculino', '', '', '', ''],
                ['Femenino', '', '', '', ''],
            ]

            if male_winner:
                data[0] = ['Masculino', str(male_winner.id), str(male_winner.first_name), str(
                    male_winner.first_surname), str(male_winner.finish_time)]

            if female_winner:
                data[1] = ['Femenino', str(female_winner.id), str(female_winner.first_name), str(
                    female_winner.first_surname), str(female_winner.finish_time)]

            self.__report_view.render_table(
                'Ganadores agrupados por sexo',
                [
                    'Sexo',
                    'Cédula',
                    'Primer Nombre',
                    'Primer Apellido',
                    'Tiempo'
                ],
                data
            )

    def winners_by_sex_and_etarios(self):
        """Ganadores por grupo etario y sexo (tabla)"""

        if (len(self.__competitors_repository.competitors) == 0):
            self.__report_view.render_messages(['No se encontraron registros'])
        else:
            junior_males = []
            juniors_females = []

            seniors_males = []
            seniors_females = []

            masters_males = []
            masters_females = []

            for competitor in self.__competitors_repository.competitors:
                if (self.__isJunior(competitor)):
                    if (competitor.sex == 'M'):
                        junior_males.append(competitor)
                    elif (competitor.sex == 'F'):
                        juniors_females.append(competitor)
                elif (self.__isSenior(competitor)):
                    if (competitor.sex == 'M'):
                        seniors_males.append(competitor)
                    elif (competitor.sex == 'F'):
                        seniors_females.append(competitor)
                elif (self.__isMaster(competitor)):
                    if (competitor.sex == 'M'):
                        masters_males.append(competitor)
                    elif (competitor.sex == 'F'):
                        masters_females.append(competitor)

            junior_male_winner = self.__find_winner(junior_males)
            juniors_female_winner = self.__find_winner(juniors_females)

            seniors_male_winner = self.__find_winner(seniors_males)
            seniors_female_winner = self.__find_winner(seniors_females)

            masters_male_winner = self.__find_winner(masters_males)
            masters_female_winner = self.__find_winner(masters_females)

            data = [
                ['Junior', 'Masculino', '', '', '', ''],
                ['', 'Femenino', '', '', '', ''],
                ['Senior', 'Masculino', '', '', '', ''],
                ['', 'Femenino', '', '', '', ''],
                ['Masters', 'Masculino', '', '', '', ''],
                ['', 'Femenino', '', '', '', ''],
            ]

            if junior_male_winner:
                data[0] = ['Junior', 'Masculino', str(junior_male_winner.id), str(junior_male_winner.first_name), str(
                    junior_male_winner.first_surname), str(junior_male_winner.finish_time)]

            if juniors_female_winner:
                data[1] = ['', 'Femenino', str(juniors_female_winner.id), str(juniors_female_winner.first_name), str(
                    juniors_female_winner.first_surname), str(juniors_female_winner.finish_time)]

            if seniors_male_winner:
                data[2] = ['Senior', 'Masculino', str(seniors_male_winner.id), str(seniors_male_winner.first_name), str(
                    seniors_male_winner.first_surname), str(seniors_male_winner.finish_time)]

            if seniors_female_winner:
                data[3] = ['', 'Femenino', str(seniors_female_winner.id), str(seniors_female_winner.first_name), str(
                    seniors_female_winner.first_surname), str(seniors_female_winner.finish_time)]

            if masters_male_winner:
                data[4] = ['Masters', 'Masculino', str(masters_male_winner.id), str(masters_male_winner.first_name), str(
                    masters_male_winner.first_surname), str(masters_male_winner.finish_time)]

            if masters_female_winner:
                data[5] = ['', 'Femenino', str(masters_female_winner.id), str(masters_female_winner.first_name), str(
                    masters_female_winner.first_surname), str(masters_female_winner.finish_time)]

            self.__report_view.render_table(
                'Ganadores agrupados por etarios y sexo',
                [
                    'Grupo',
                    'Sexo',
                    'Cédula',
                    'Primer Nombre',
                    'Primer Apellido',
                    'Tiempo'
                ],
                data
            )

    def main_winner(self):
        """Ganador general (línea)"""

        if (len(self.__competitors_repository.competitors) == 0):
            self.__report_view.render_messages(['No se encontraron registros'])
        else:
            if (len(self.__competitors_repository.competitors) == 0):
                self.__report_view.render_messages(
                    ['No se encontraron registros'])
            else:
                winner = self.__find_winner(
                    self.__competitors_repository.competitors)

                group = 'Junior' if self.__isJunior(winner) else (
                    'Senior' if self.__isSenior(winner) else 'Master')

                sex = 'Masculino' if winner.sex == 'M' else 'Femenino'

                self.__report_view.render_messages(
                    [f'El ganador general es: {winner.first_name} {winner.first_surname} (CI: {winner.id} - Grupo: {group} - Sexo: {sex})'])

    def histogram_by_etarios(self):
        """Histograma de participante por grupo etario"""

        if (len(self.__competitors_repository.competitors) == 0):
            self.__report_view.render_messages(['No se encontraron registros'])
        else:
            total = len(self.__competitors_repository.competitors)

            juniors_count = 0
            seniors_count = 0
            masters_count = 0

            for competitor in self.__competitors_repository.competitors:
                if (self.__isJunior(competitor)):
                    juniors_count += 1
                elif (self.__isSenior(competitor)):
                    seniors_count += 1
                elif (self.__isMaster(competitor)):
                    masters_count += 1

            # Normalizamos
            norm_juniors = int((juniors_count / total) * 100)
            norm_seniors = int((seniors_count / total) * 100)
            norm_masters = int((masters_count / total) * 100)

            self.__report_view.render_histogram(
                'Histograma Agrupados Etarios',
                ['Junior', 'Senior', 'Master'],
                [str(juniors_count), str(seniors_count), str(masters_count)],
                [norm_juniors, norm_seniors, norm_masters]
            )

    def average_by_etarios_and_sex(self):
        """Promedio de tiempo por grupo etario y sexo"""

        if (len(self.__competitors_repository.competitors) == 0):
            self.__report_view.render_messages(['No se encontraron registros'])
        else:
            juniors_males = []
            juniors_females = []

            seniors_males = []
            seniors_females = []

            masters_males = []
            masters_females = []

            for competitor in self.__competitors_repository.competitors:
                if (self.__isJunior(competitor)):
                    if (competitor.sex == 'M'):
                        juniors_males.append(competitor)
                    elif (competitor.sex == 'F'):
                        juniors_females.append(competitor)
                elif (self.__isSenior(competitor)):
                    if (competitor.sex == 'M'):
                        seniors_males.append(competitor)
                    elif (competitor.sex == 'F'):
                        seniors_females.append(competitor)
                elif (self.__isMaster(competitor)):
                    if (competitor.sex == 'M'):
                        masters_males.append(competitor)
                    elif (competitor.sex == 'F'):
                        masters_females.append(competitor)

            junior_male_average = self.__time_average(juniors_males)
            juniors_female_average = self.__time_average(juniors_females)

            seniors_male_average = self.__time_average(seniors_males)
            seniors_female_average = self.__time_average(seniors_females)

            masters_male_average = self.__time_average(masters_males)
            masters_female_average = self.__time_average(masters_females)

        data = [
            ['Junior', 'Masculino', ''],
            ['', 'Femenino', ''],
            ['Senior', 'Masculino', ''],
            ['', 'Femenino', ''],
            ['Masters', 'Masculino', ''],
            ['', 'Femenino', ''],
        ]

        if junior_male_average:
            data[0] = ['Junior', 'Masculino', junior_male_average]

        if juniors_female_average:
            data[1] = ['', 'Femenino', juniors_female_average]

        if seniors_male_average:
            data[2] = ['Senior', 'Masculino', seniors_male_average]

        if seniors_female_average:
            data[3] = ['', 'Femenino', seniors_female_average]

        if masters_male_average:
            data[4] = ['Masters', 'Masculino', masters_male_average]

        if masters_female_average:
            data[5] = ['', 'Femenino', masters_female_average]

        self.__report_view.render_table(
            'Promedio de tiempo por grupo etario y sexo',
            [
                'Grupo',
                'Sexo',
                'Tiempo Promedio'
            ],
            data
        )

    def __isJunior(self, competitor: CompetitorDto):
        if (not competitor):
            return False
        return True if competitor.age <= 25 else False

    def __isSenior(self, competitor: CompetitorDto):
        if (not competitor):
            return False
        return True if competitor.age > 25 and competitor.age <= 40 else False

    def __isMaster(self, competitor: CompetitorDto):
        if (not competitor):
            return False
        return True if competitor.age > 40 else False

    def __find_winner(self, competitors: Iterable[CompetitorDto]):
        if (len(competitors) == 0):
            return None

        winner: CompetitorDto = competitors[0]

        for competitor in competitors:
            if (competitor.finish_time < winner.finish_time):
                winner = competitor

        return winner

    def __time_average(self, competitors: Iterable[CompetitorDto]):
        if (len(competitors) == 0):
            return ''

        times = [str(competitor.finish_time) for competitor in competitors]
        average = str(datetime.timedelta(seconds=sum(map(lambda f: int(
            f[0])*3600 + int(f[1])*60 + int(f[2]), map(lambda f: f.split(':'), times)))//len(times)))
        return average
