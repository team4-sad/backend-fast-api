import enum


class RequiredNewsFields(enum.Enum):
    header = 0
    date = 1
    news_link = 2
    content = 3