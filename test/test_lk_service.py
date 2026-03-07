from datetime import datetime
from unittest import TestCase
from src.exceptions.code_exception import CodeException
from src.models.certification_model import CertificationModel
from src.models.course_education_plan_model import CourseEducationPlanModel
from src.models.education_info_model import EducationInfoModel
from src.models.education_plan_model import EducationPlanModel
from src.models.item_family_model import ItemFamilyModel
from src.models.lk_academic_record_model import LkAcademicRecordModel
from src.models.lk_course_record_model import LkCourseRecordModel
from src.models.lk_profile_model import LkProfileModel
from src.models.lk_semester_record_model import LkSemesterRecordModel
from src.models.semester_education_plan_model import SemesterEducationPlanModel
from src.services.lk_service import LkService
from test.mock.classes.mock_corrupted_lk_repository import MockCorruptedLkRepository
from test.mock.classes.mock_lk_repository import MockLkRepository


class LkServiceTest(TestCase):
    def test_success_lk_service_get_me(self):
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

    def test_empty_key_lk_service_get_me(self):
        with self.assertRaises(CodeException) as e:
            LkService(lk_repository=MockLkRepository()).get_me("")
        self.assertEqual(e.exception, CodeException('Not Authorized', 401))

    def test_corrupted_lk_service_get_me(self):
        with self.assertRaises(CodeException) as e:
            LkService(lk_repository=MockCorruptedLkRepository()).get_me("")
        self.assertEqual(e.exception, CodeException('Lk error: mock exception', 503))

    def test_success_lk_service_get_academic_records(self):
        result = LkService(lk_repository=MockLkRepository()).get_academic_records("1")
        self.assertEqual([
            LkCourseRecordModel(
                course=1,
                records=[
                    LkSemesterRecordModel(
                        semester=1,
                        records=[
                            LkAcademicRecordModel(
                                subject='Математика',
                                type='Зачёт с оценкой',
                                rate='3',
                                teachers=['Королева Татьяна Михайловна']
                            ),
                            LkAcademicRecordModel(
                                subject='Основы права',
                                type='Зачёт',
                                rate='Зачёт',
                                teachers=['Михайлов Филипп Николаевич']
                            ),
                            LkAcademicRecordModel(
                                subject='Физика',
                                type='Зачёт с оценкой',
                                rate='3',
                                teachers=['Старцев Сергей Александрович']
                            )
                        ]
                    ),
                    LkSemesterRecordModel(
                        semester=2,
                        records=[
                            LkAcademicRecordModel(
                                subject='Математика',
                                type='Зачёт с оценкой',
                                rate='3',
                                teachers=['Королева Татьяна Михайловна']
                            ),
                            LkAcademicRecordModel(
                                subject='Основы права',
                                type='Зачёт',
                                rate='Зачёт',
                                teachers=['Михайлов Филипп Николаевич']
                            ),
                            LkAcademicRecordModel(
                                subject='Физика',
                                type='Зачёт с оценкой',
                                rate='3',
                                teachers=['Старцев Сергей Александрович']
                            )
                        ]
                    )
                ]
            ),
            LkCourseRecordModel(
                course=2,
                records=[
                    LkSemesterRecordModel(
                        semester=3,
                        records=[
                            LkAcademicRecordModel(
                                subject='Математика',
                                type='Зачёт с оценкой',
                                rate='3',
                                teachers=['Королева Татьяна Михайловна']
                            ),
                            LkAcademicRecordModel(
                                subject='Основы права',
                                type='Зачёт',
                                rate='Зачёт',
                                teachers=['Михайлов Филипп Николаевич']
                            ),
                            LkAcademicRecordModel(
                                subject='Физика',
                                type='Зачёт с оценкой',
                                rate='3',
                                teachers=['Старцев Сергей Александрович']
                            )
                        ]
                    ),
                    LkSemesterRecordModel(
                        semester=4,
                        records=[
                            LkAcademicRecordModel(
                                subject='Математика',
                                type='Зачёт с оценкой',
                                rate='4',
                                teachers=['Королева Татьяна Михайловна']
                            ),
                            LkAcademicRecordModel(
                                subject='Основы права',
                                type='Зачёт',
                                rate='Зачёт',
                                teachers=['Михайлов Филипп Николаевич']
                            ),
                            LkAcademicRecordModel(
                                subject='Физика',
                                type='Зачёт с оценкой',
                                rate='4',
                                teachers=['Старцев Сергей Александрович']
                            )
                        ]
                    )
                ]
            )
        ], result)

    def test_empty_key_lk_service_get_academic_records(self):
        with self.assertRaises(CodeException) as e:
            LkService(lk_repository=MockLkRepository()).get_academic_records("")
        self.assertEqual(e.exception, CodeException('Not Authorized', 401))

    def test_corrupted_lk_service_get_academic_records(self):
        with self.assertRaises(CodeException) as e:
            LkService(lk_repository=MockCorruptedLkRepository()).get_academic_records("")
        self.assertEqual(e.exception, CodeException('Lk error: mock exception', 503))

    def test_success_lk_service_get_education_plan(self):
        result = LkService(lk_repository=MockLkRepository()).get_education_plan("1")
        self.assertEqual(
            result,
            [CourseEducationPlanModel
            (
                course=1,
                semesters=[
                    SemesterEducationPlanModel
                        (
                        semester=1,
                        plan=
                        [
                            EducationPlanModel(
                                index='0124',
                                discipline='Линейная алгебра',
                                academic_hours=9998,
                                credit_units=1,
                                certification=CertificationModel(
                                    exam=True,
                                    credit_with_rate=False,
                                    credit=False,
                                    course_work=False,
                                    course_project=False
                                ),
                                department='Кафедра высшей математики',
                                count_lectures=4999,
                                count_laboratories=0,
                                count_independent_work=5,
                                count_practical=4994,
                                exist_essay=False
                            ),
                            EducationPlanModel(
                                index='0127',
                                discipline='Математика',
                                academic_hours=9994,
                                credit_units=1,
                                certification=CertificationModel(
                                    exam=False,
                                    credit_with_rate=True,
                                    credit=False,
                                    course_work=False,
                                    course_project=False
                                ),
                                department='Кафедра высшей математики',
                                count_lectures=4997,
                                count_laboratories=0,
                                count_independent_work=4,
                                count_practical=4993,
                                exist_essay=False
                            )
                        ]
                        ),
                    SemesterEducationPlanModel(
                        semester=2,
                        plan=
                        [
                            EducationPlanModel
                            (
                                index='0127',
                                discipline='Математика',
                                academic_hours=9998,
                                credit_units=1,
                                certification=CertificationModel(
                                    exam=True,
                                    credit_with_rate=False,
                                    credit=False,
                                    course_work=False,
                                    course_project=False
                                ),
                                department='Кафедра высшей математики',
                                count_lectures=4999,
                                count_laboratories=0,
                                count_independent_work=5,
                                count_practical=4994,
                                exist_essay=False
                            ),
                            EducationPlanModel
                            (
                                index='0243',
                                discipline='История',
                                academic_hours=4,
                                credit_units=1,
                                certification=CertificationModel(
                                    exam=True,
                                    credit_with_rate=False,
                                    credit=False,
                                    course_work=False,
                                    course_project=False
                                ),
                                department='Кафедра истории',
                                count_lectures=4,
                                count_laboratories=0,
                                count_independent_work=1,
                                count_practical=0,
                                exist_essay=True
                            )
                        ]
                    )
                ]
            )]
        )


    def test_empty_key_lk_service_get_education_plan(self):
        with self.assertRaises(CodeException) as e:
            LkService(lk_repository=MockLkRepository()).get_education_plan("")
        self.assertEqual(e.exception, CodeException('Not Authorized', 401))

    def test_corrupted_lk_sservice_get_education_plan(self):
        with self.assertRaises(CodeException) as e:
            LkService(lk_repository=MockCorruptedLkRepository()).get_education_plan("")
        self.assertEqual(e.exception, CodeException('Lk error: mock exception', 503))