class InvalidPaginationHTML (Exception):
    def __str__(self):
        return "Invalid pagination HTML"

    def __init__(self, html: str):
        self.html = html
