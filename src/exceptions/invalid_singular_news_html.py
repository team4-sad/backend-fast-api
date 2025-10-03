from src.enums.required_news_fields import RequiredNewsFields


class InvalidSingularNewsHTML (Exception):
    def __str__(self):
        return f"Invalid singular news HTML - not found {self.field}"

    def __init__(self, html: str, field: RequiredNewsFields):
        self.html = html
        self.field = field
