from datetime import date, datetime


def date2str(convert_date: date) -> str:
    return convert_date.strftime('%d.%m.%Y')


def str2date(convert_date: str) -> date:
    return datetime.strptime(convert_date, "%d.%m.%Y").date()


def str2datetime(convert_date: str) -> datetime:
    return datetime.strptime(convert_date, "%d.%m.%Y %H:%M:%S")


def is_only_date(str_date: str) -> bool:
    return ":" not in str_date


def remove_time(convert_date: str) -> str:
    return convert_date.split(" ")[0]
