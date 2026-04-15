from datetime import date, datetime, timedelta


def date2strDMY(convert_date: date) -> str:
    return convert_date.strftime('%d.%m.%Y')


def str2dateDMY(convert_date: str) -> date:
    return datetime.strptime(convert_date, "%d.%m.%Y").date()


def str2datetimeDMYHMS(convert_date: str) -> datetime:
    return datetime.strptime(convert_date, "%d.%m.%Y %H:%M:%S")


def is_only_date(str_date: str) -> bool:
    return ":" not in str_date


def remove_str_time(convert_date: str) -> str:
    return convert_date.split(" ")[0]


def get_monday_datetime(curr: datetime) -> date:
    start_of_week = curr - timedelta(days=curr.weekday())
    return start_of_week.date()


def get_sunday_datetime(curr: datetime) -> date:
    monday = get_monday_datetime(curr)
    return monday + timedelta(days=6)


def is_prime_week(curr: date) -> bool:
    # prime week == Верхняя неделя
    number = curr.isocalendar().week
    return number % 2 == 0


def date2strYMD(dt: date) -> str:
    return dt.strftime("%Y-%m-%d")


def str2dateYMD(s: str) -> date:
    return datetime.strptime(s, "%Y-%m-%d").date()


def str2iso(s: str) -> datetime:
    return datetime.fromisoformat(s)


def date2iso(dt: date | datetime) -> str:
    return dt.isoformat()
