"""
Скрипт на получение всех возможных вариаций postfix групп.
В данном случае postfix'ом считается подстрока идущей после специальности и номера группы, например:
2023-ФГиИБ-ПИ-1б -> б
2019-ЗФ-ПГ-1с(дзо) -> с(дзо)
2020-ГФ-ПГ-4с -> c
2022-ЗФ-ГиДЗг-1б(дзо-у) -> б(дзо-у)

На вход скрипт получает список всех групп в формате JSON от результата выполнения запроса
https://study.miigaik.ru/api/v1/search/group?groupName=

На выход, в директорию, где расположен скрипт, создается/перезаписывается два файла:
postfixes.json - все уникальные postfix
response.json - оригинальный ответ от сервера
"""
import json

from requests import get

response = get('https://study.miigaik.ru/api/v1/search/group?groupName=')
response.raise_for_status()
jsn = response.json()


def get_postfix_group(group_name):
    last_part = "-".join(group_name.split("-")[3:])
    last_part_without_digits = "".join([i for i in last_part if not i.isdigit()])
    return last_part_without_digits


with open('response.json', 'w', encoding="utf-8") as f:
    json.dump(jsn, f, ensure_ascii=False)

group_names = [i["groupName"] for i in jsn]
postfixes = [get_postfix_group(i) for i in group_names]
unique_postfixes = list(set(postfixes))

with open('postfixes.json', 'w', encoding="utf-8") as f:
    json.dump(unique_postfixes, f, ensure_ascii=False)
