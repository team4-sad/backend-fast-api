from datetime import datetime
from unittest import TestCase
from src.exceptions.code_exception import CodeException
from src.models.education_info_model import EducationInfoModel
from src.models.item_family_model import ItemFamilyModel
from src.models.lk_profile_model import LkProfileModel
from src.services.lk_service import LkService
from test.mock.classes.mock_corrupted_lk_repository import MockCorruptedLkRepository
from test.mock.classes.mock_lk_repository import MockLkRepository


class LkServiceTest(TestCase):
    def test_success_lk_service(self):
        result = LkService(lk_repository=MockLkRepository()).get_me("1")
        self.assertEqual(
            LkProfileModel(
                first_name='Владимир',
                last_name='Путин',
                patronymic='Владимирович',
                lk_email='0000001234@miigaik.ru',
                email='VVPutin@kremlin.ru',
                address='Москва, Центральный административный округ, Тверской район, Кремль',
                job_place='Москва, Центральный административный округ, Тверской район, Кремль',
                job_title='Президент РФ',
                number_student_card='1234/56',
                datetime_student_card=datetime(1970, 9, 1, 0, 0),
                record_book_number='1234/56',
                education_info=[
                    EducationInfoModel(
                        faculty='Юридический факультет',
                        form='Очная',
                        type_form='Бюджетная основа',
                        level='Полное Высшее',
                        direction='Международное отделение',
                        group='ЮФ-МО-1б-1970',
                        course='4',
                        status='Выпускник',
                        profile=""
                    )
                ],
                family=[
                    ItemFamilyModel(
                        kinship='Мать',
                        fio='Путина Мария Ивановна'
                    ),
                    ItemFamilyModel(
                        kinship='Отец',
                        fio='Путин Владимир Спиридонович'
                    )
                ]
            ), result)

    def test_empty_key_lk_service(self):
        with self.assertRaises(CodeException) as e:
            LkService(lk_repository=MockLkRepository()).get_me("")
        self.assertEqual(e.exception, CodeException('Not Authorized', 401))

    def test_corrupted_lk_service(self):
        with self.assertRaises(CodeException) as e:
            LkService(lk_repository=MockCorruptedLkRepository()).get_me("")
        self.assertEqual(e.exception, CodeException('Lk error: mock exception', 503))
