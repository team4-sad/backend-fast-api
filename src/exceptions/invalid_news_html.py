class InvalidNewsHTML (Exception):
    def __str__(self):
        return "Invalid news HTML"

    def __init__(self, html: str):
        self.html = html
