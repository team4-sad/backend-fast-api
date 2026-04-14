from datetime import datetime, timedelta, date


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

def date2str(dt: date) -> str:
    return dt.strftime("%Y-%m-%d")

def str2date(s: str) -> date:
    return datetime.strptime(s, "%Y-%m-%d").date()