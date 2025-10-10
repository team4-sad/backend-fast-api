import unittest

from src.exceptions.code_exception import CodeException
from src.models.news_list_response_model import NewsListResponseModel
from src.models.news_model import NewsModel
from src.models.pagination_model import PaginationModel
from src.models.singular_news_model import SingularNewsModel
from src.parsers.news_parser import NewsParser
from src.services.news_service import NewsService
from test.mock.classes.mock_corrupted_news_repository import MockCorruptedNewsRepository
from test.mock.classes.mock_news_repository import MockNewsRepository


class NewsServiceTest(unittest.TestCase):
    def setUp(self):
        self.news_service = NewsService(
            news_parser=NewsParser(base_link_url="https://miigaik.ru"),
            news_repository=MockNewsRepository()
        )
        self.corrupted_news_service = NewsService(
            news_parser=NewsParser(base_link_url="https://miigaik.ru"),
            news_repository=MockCorruptedNewsRepository()
        )


    def test_get_list_news(self):
        result = self.news_service.get_news_list(1)
        self.assertEqual(
            result,

            NewsListResponseModel(
                news_list=[
                    NewsModel(id='6614',
                              header='День воссоединения ДНР, '
                                     'ЛНР, Запорожской и '
                                     'Херсонской областей с '
                                     'Российской Федерацией',
                              date_created='30.09.2025',
                              news_link='https://miigaik.ru/about/news/6614/',
                              image_link='https://miigaik.ru/upload/iblock/358/g5xbjld3fng4cl1024pdt9z2hvguhmvz.png',
                              description='Установлен в 2023 году '
                                          'Указом президента РФ'),
                    NewsModel(id='6615',
                              header='В МИИГАиК завершилась '
                                     'проектно-аналитическая '
                                     'сессия в рамках '
                                     'кросс-вузовской экспертизы',
                              date_created='30.09.2025',
                              news_link='https://miigaik.ru/about/news/6615/',
                              image_link='https://miigaik.ru/upload/iblock/aea/vt7uabx3euuz478lw5lxech55n5gi90j.png',
                              description='Завершившаяся сессия '
                                          'стала не только '
                                          'площадкой для '
                                          'выработки решений, но '
                                          'и важным шагом к '
                                          'сплочению коллектива.')
                ],
                pagination=PaginationModel(
                    is_previous_page=False,
                    current_page=1,
                    is_next_page=True
                )
            )

        )

    def test_get_singular_news_html(self):
        result = self.news_service.get_singular_news(1)
        self.assertEqual(
            result,

            SingularNewsModel(
                header='Студенты МИИГАиК на фестивале "Открытый город"',
                date_created='22.09.2025',
                content_html='<hr/>\n'
                               '<div class="news-item-image">\n'
                               "<img alt='Студенты МИИГАиК на фестивале "
                               '"Открытый город"\' '
                               'src="/upload/iblock/de2/xnkgdh2140swp45nojmanzlsukgamcm1.jpg" '
                               "title='Студенты МИИГАиК на фестивале "
                               '"Открытый город"\' width="800"/>\n'
                               '</div>\n'
                               '<hr/>\n'
                               '<!-- Об интереснейшем и сложном объекте '
                               'рассказал его автор, куратор фестиваля, '
                               'архитектор Тимур Башкаев. -->\n'
                               '                В рамках фестиваля <a '
                               'href="http://opencityfest.ru/">«Открытый '
                               'город»</a> группа градостроителей 5 курса '
                               'Факультета архитектуры и градостроительства '
                               'вместе преподавателем по архитектурному и '
                               'градостроительному проектированию Еленой '
                               'Ганушкиной посвятила выходные дни изучению '
                               'города и посетила экскурсию по крупнейшему '
                               'транспортно-пересадочному узлу Москвы. Об '
                               'интереснейшем и сложном объекте рассказал его '
                               'автор, куратор фестиваля, архитектор Тимур '
                               'Башкаев.\n'
                               '<p style="text-align: center;">\n'
                               '<img '
                               'src="/upload/images/content-img(227).png"/>\n'
                               '</p>\n'
                               '<p style="text-align: center;">\n'
                               '<img '
                               'src="/upload/images/content-img(226).png"/>\n'
                               '</p>\n'
                               ' ТПУ «Нижегородская» объединяет метро '
                               '(Некрасовская и БКЛ), МЦК, МЦД, железную '
                               'дорогу, наземный транспорт и ежедневно '
                               'обслуживает около 100 тысяч поездок. Это не '
                               'только пересадочный пункт, но и современное '
                               'городское пространство с эксплуатируемой '
                               'кровлей, стеклянным атриумом и озелененной '
                               'площадью по проекту Arteza. Центральный акцент '
                               'ансамбля — арт-объект «Московские кольца».\n'
                               '<p style="text-align: center;">\n'
                               '<img '
                               'src="/upload/images/content-img(229).png"/>\n'
                               '</p>\n'
                               '<p style="text-align: center;">\n'
                               '<img '
                               'src="/upload/images/content-img(228).png"/>\n'
                               '</p>\n'
                               ' На экскурсии студенты МИИГАиК узнали:<br/>\n'
                               ' - каковы особенности проектирования '
                               'крупнейшего ТПУ столицы,<br/>\n'
                               ' - как изменились подходы к созданию подобных '
                               'объектов за последние годы,<br/>\n'
                               ' - какие дополнительные функции могут обрести '
                               'подобные транзитные пространства в будущем.\n'
                               '<p style="text-align: center;">\n'
                               '<img '
                               'src="/upload/images/content-img(230).png"/>\n'
                               '</p>\n'
                               '<p style="text-align: center;">\n'
                               '<img '
                               'src="/upload/images/content-img(231).png"/>\n'
                               '</p>\n'
                               ' Фотографии: <a '
                               'href="http://prorus.ru/projects/tpu-nizhegorodskaya-v-moskve/#gallery-13%20">ПРОЕКТ '
                               'РОССИЯ</a><br/>\n'
                               '<br/>'
            )
        )

    def test_get_corrupted_news_list(self):
        with self.assertRaises(CodeException) as e:
            self.corrupted_news_service.get_news_list(1)
        self.assertEqual(e.exception, CodeException('Failed to process news list', 424))

    def test_get_corrupted_singular_news(self):
        with self.assertRaises(CodeException) as e:
            self.corrupted_news_service.get_singular_news(1)
        self.assertEqual(e.exception, CodeException('Failed to process singular news', 424))




if __name__ == '__main__':
    unittest.main()
