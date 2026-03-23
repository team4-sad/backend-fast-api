from datetime import datetime
from unittest import TestCase

from freezegun import freeze_time

from src.enums.document_form_field_type import DocumentFormFieldType
from src.enums.order_document_status import OrderDocumentStatus
from src.exceptions.code_exception import CodeException
from src.models.certification_model import CertificationModel
from src.models.course_education_plan_model import CourseEducationPlanModel
from src.models.document_form_field_model import DocumentFormFieldModel
from src.models.document_form_model import DocumentFormModel
from src.models.education_info_model import EducationInfoModel
from src.models.education_plan_model import EducationPlanModel
from src.models.filled_document_form_field_model import FilledDocumentFormFieldModel
from src.models.filled_document_form_model import FilledDocumentFormModel
from src.models.interval_model import IntervalModel
from src.models.item_family_model import ItemFamilyModel
from src.models.lk_academic_record_model import LkAcademicRecordModel
from src.models.lk_course_record_model import LkCourseRecordModel
from src.models.lk_profile_model import LkProfileModel
from src.models.lk_semester_record_model import LkSemesterRecordModel
from src.models.order_document_model import OrderDocumentModel
from src.models.semester_education_plan_model import SemesterEducationPlanModel
from src.services.lk_service import LkService
from test.mock.classes.mock_corrupted_lk_repository import MockCorruptedLkRepository
from test.mock.classes.mock_lk_repository import MockLkRepository


class LkServiceTest(TestCase):
    def test_success_get_me(self):
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

    def test_empty_access_token_get_me(self):
        with self.assertRaises(CodeException) as e:
            LkService(lk_repository=MockLkRepository()).get_me("")
        self.assertEqual(e.exception, CodeException('Not Authorized', 401))

    def test_corrupted_get_me(self):
        with self.assertRaises(CodeException) as e:
            LkService(lk_repository=MockCorruptedLkRepository()).get_me("")
        self.assertEqual(e.exception, CodeException('Lk error: mock exception', 503))

    def test_success_get_academic_records(self):
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
                                rate='Зачтено',
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
                                subject='Основы программирования',
                                type='Экзамен',
                                rate='5',
                                teachers=['Максимова Елена Юрьевна']
                            ),
                            LkAcademicRecordModel(
                                subject='История России',
                                type='Зачёт',
                                rate='Зачтено',
                                teachers=["Закатов Александр Николаевич", "Денисов Андрей Олегович"]
                            ),
                            LkAcademicRecordModel(
                                subject='Основы военной подготовки',
                                type='Зачёт',
                                rate='Зачтено',
                                teachers=["Кудакаев Тагир Галимханович", "Чебан Иван Феодорович", "Ильин Олег Юрьевич"]
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
                                subject='Дискретная математика',
                                type='Зачёт с оценкой',
                                rate='3',
                                teachers=["Чанга Марис Евгеньевич"]
                            ),
                            LkAcademicRecordModel(
                                subject="Методы математического моделирования",
                                type="Зачёт с оценкой",
                                rate='4',
                                teachers=['Сёмов Александр Михайлович']
                            )
                        ]
                    ),
                    LkSemesterRecordModel(
                        semester=4,
                        records=[
                            LkAcademicRecordModel(
                                subject='Физика',
                                type='Экзамен',
                                rate='Неявка',
                                teachers=["Падалка Наталья Михайловна"]
                            ),
                            LkAcademicRecordModel(
                                subject='Оптика',
                                type='Экзамен',
                                rate='2',
                                teachers=["Падалка Наталья Михайловна"]
                            ),
                            LkAcademicRecordModel(
                                subject='История земельных отношений',
                                type='Зачёт с оценкой',
                                rate=None,
                                teachers=["Закатов Александр Николаевич", "Денисов Андрей Олегович"]
                            ),
                            LkAcademicRecordModel(
                                subject='Иностранный язык',
                                type='Экзамен',
                                rate="5",
                                teachers=["Чуканова Татьяна Александровна", "Милова Татьяна Николаевна"]
                            ),
                            LkAcademicRecordModel(
                                subject='Психология саморазвития',
                                type='Зачёт',
                                rate='Зачтено',
                                teachers=["Самойленко Светлана Алексеевна"]
                            )
                        ]
                    )
                ]
            )
        ], result)

    def test_empty_access_token_get_academic_records(self):
        with self.assertRaises(CodeException) as e:
            LkService(lk_repository=MockLkRepository()).get_academic_records("")
        self.assertEqual(e.exception, CodeException('Not Authorized', 401))

    def test_corrupted_get_academic_records(self):
        with self.assertRaises(CodeException) as e:
            LkService(lk_repository=MockCorruptedLkRepository()).get_academic_records("")
        self.assertEqual(e.exception, CodeException('Lk error: mock exception', 503))

    def test_success_get_education_plan(self):
        result = LkService(lk_repository=MockLkRepository()).get_education_plan("1")
        self.assertEqual(
            result, [
                CourseEducationPlanModel(
                    course=1,
                    semesters=[
                        SemesterEducationPlanModel(
                            semester=1,
                            plan=[
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
                            plan=[
                                EducationPlanModel(
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
                                EducationPlanModel(
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
                )
            ]
        )

    def test_empty_access_token_get_education_plan(self):
        with self.assertRaises(CodeException) as e:
            LkService(lk_repository=MockLkRepository()).get_education_plan("")
        self.assertEqual(e.exception, CodeException('Not Authorized', 401))

    def test_corrupted_lk_sservice_get_education_plan(self):
        with self.assertRaises(CodeException) as e:
            LkService(lk_repository=MockCorruptedLkRepository()).get_education_plan("")
        self.assertEqual(e.exception, CodeException('Lk error: mock exception', 503))

    def test_success_get_orders_document(self):
        result = LkService(lk_repository=MockLkRepository()).get_orders_document("1")
        self.assertEqual(
            result,
            [OrderDocumentModel(
                id=1337,
                number='2026-0000001224',
                name='Тест заказ документа',
                created_at=datetime(2005, 10, 4, 0, 0, 1),
                interval=IntervalModel(start_day=2, end_day=5),
                status=OrderDocumentStatus.complete,
                comment='Документ готов к выдаче'
            )]
        )

    def test_empty_access_token_get_orders_document(self):
        with self.assertRaises(CodeException) as e:
            LkService(lk_repository=MockLkRepository()).get_orders_document("")
        self.assertEqual(e.exception, CodeException('Not Authorized', 401))

    def test_corrupted_lk_sservice_get_orders_document(self):
        with self.assertRaises(CodeException) as e:
            LkService(lk_repository=MockCorruptedLkRepository()).get_orders_document("")
        self.assertEqual(e.exception, CodeException('Lk error: mock exception', 503))

    def test_success_get_document_forms(self):
        result = LkService(lk_repository=MockLkRepository()).get_document_forms(access_token="1")
        self.assertEqual(result,
                         [
                             DocumentFormModel(
                                 name='Допуск',
                                 description='Описание допуска идк',
                                 interval_make=IntervalModel(start_day=2, end_day=5),
                                 fields=[
                                     DocumentFormFieldModel(
                                         label='тип зачета',
                                         type=DocumentFormFieldType.select,
                                         is_required=True,
                                         options=['зачет', 'зачет с оценкой', 'экзамен']
                                     ),
                                     DocumentFormFieldModel(label='ФИО преподавателя',
                                                            type=DocumentFormFieldType.single_line,
                                                            is_required=True,
                                                            options=[]),
                                     DocumentFormFieldModel(label='Полное название группы',
                                                            type=DocumentFormFieldType.single_line,
                                                            is_required=True,
                                                            options=[])]),
                             DocumentFormModel(
                                 name='Бумажка',
                                 description='Описание бумажки идк',
                                 interval_make=IntervalModel(start_day=1, end_day=3),
                                 fields=[
                                     DocumentFormFieldModel(
                                         label='куда вам бумажку?',
                                         type=DocumentFormFieldType.select,
                                         is_required=True,
                                         options=['домой', 'на работу', 'по приколу']),
                                     DocumentFormFieldModel(label='Какую бумажку',
                                                            type=DocumentFormFieldType.single_line,
                                                            is_required=True,
                                                            options=[])]),
                             DocumentFormModel(
                                 name='Важная бумажка',
                                 description='Описание важной бумажки идк',
                                 interval_make=IntervalModel(start_day=1, end_day=3),
                                 fields=[
                                     DocumentFormFieldModel(
                                         label='куда вам бумажку?',
                                         type=DocumentFormFieldType.select,
                                         is_required=True,
                                         options=['домой', 'на работу', 'по приколу']),
                                     DocumentFormFieldModel(
                                         label='Какую бумажку',
                                         type=DocumentFormFieldType.single_line,
                                         is_required=True,
                                         options=[])])])

    def test_invalid_get_document_forms(self):
        with self.assertRaises(CodeException) as e:
            LkService(lk_repository=MockCorruptedLkRepository()).get_document_forms(access_token="1")
        self.assertEqual(e.exception, CodeException('Lk error: mock exception', 503))

    @freeze_time("2025-04-01 12:00:00")
    def test_success_send_filled_document_form(self):
        result = LkService(lk_repository=MockLkRepository()).send_filled_document_form(
            access_token="1",
            filled_document_form_model=FilledDocumentFormModel(
                name="name",
                description="description",
                interval_make=IntervalModel(
                    start_day=1, end_day=5),
                user_id="000005678",
                fields=[
                    DocumentFormFieldModel(
                        label='Какую бумажку',
                        type=DocumentFormFieldType.single_line,
                        is_required=True,
                        options=[])
                ],
                filled_fields=[
                    FilledDocumentFormFieldModel(
                        label="какую Бумажку",
                        type=DocumentFormFieldType.single_line,
                        is_required=True,
                        options=[],
                        value="вон ту, синенькую"
                    )]
            ))
        self.assertEqual(result, OrderDocumentModel(
            id=0,
            name="name",
            number="2026-0000000000",
            created_at=datetime(year=2025, month=4, day=1, hour=12, minute=0, second=0),
            interval=IntervalModel(start_day=1, end_day=5),
            status=OrderDocumentStatus.in_progress,
            comment=""
        ))

    def test_invalid_send_filled_document_form(self):
        with self.assertRaises(CodeException) as e:
            LkService(lk_repository=MockCorruptedLkRepository()).send_filled_document_form(
                filled_document_form_model=FilledDocumentFormModel(
                    name="name",
                    description="description",
                    interval_make=IntervalModel(start_day=1, end_day=5),
                    user_id="000005678",
                    fields=[DocumentFormFieldModel(
                        label='Какую бумажку',
                        type=DocumentFormFieldType.single_line,
                        is_required=True,
                        options=[]
                    )],
                    filled_fields=[FilledDocumentFormFieldModel(
                        label="какую Бумажку",
                        type=DocumentFormFieldType.single_line,
                        is_required=True,
                        options=[],
                        value="вон ту, синенькую"
                    )]
                ),
                access_token="1"
            )
        self.assertEqual(e.exception, CodeException('Lk error: mock exception', 503))

    def test_empty_access_token_get_document_forms(self):
        with self.assertRaises(CodeException) as e:
            LkService(lk_repository=MockLkRepository()).get_document_forms("")
        self.assertEqual(e.exception, CodeException('Not Authorized', 401))

    def test_empty_access_token_send_filled_document_form(self):
        with self.assertRaises(CodeException) as e:
            LkService(lk_repository=MockLkRepository()).send_filled_document_form(
                filled_document_form_model=FilledDocumentFormModel(
                    name="name",
                    description="description",
                    interval_make=IntervalModel(start_day=1, end_day=5),
                    user_id="000005678",
                    fields=[DocumentFormFieldModel(
                        label='Какую бумажку',
                        type=DocumentFormFieldType.single_line,
                        is_required=True,
                        options=[]
                    )],
                    filled_fields=[FilledDocumentFormFieldModel(
                        label="какую Бумажку",
                        type=DocumentFormFieldType.single_line,
                        is_required=True,
                        options=[],
                        value="вон ту, синенькую"
                    )]
                ),
                access_token=""
            )
        self.assertEqual(e.exception, CodeException('Not Authorized', 401))
