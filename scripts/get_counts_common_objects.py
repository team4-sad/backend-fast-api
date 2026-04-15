"""
Скрипт на получение количества студенческий групп, аудиторий и преподавателей на сервисе расписания МИИГАиК
"""

from requests import get

response = get('https://study.miigaik.ru/api/v1/search/group?groupName=')
response.raise_for_status()
groups: list[dict] = response.json()

response = get('https://study.miigaik.ru/api/v1/search/teacher?teacherFullName=')
response.raise_for_status()
teachers: list[dict] = response.json()

response = get('https://study.miigaik.ru/api/v1/search/classroom?classroomName=')
response.raise_for_status()
classrooms: list[dict] = response.json()

print(f"Количество групп: {len(groups)}")
print(f"Количество преподавателей: {len(teachers)}")
print(f"Количество аудиторий: {len(classrooms)}")
