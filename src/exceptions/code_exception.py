class CodeException(Exception):
    def __init__(self, message, error_code):
        self.message = message
        self.error_code = error_code

    def __str__(self):
        return f"{self.message} (Error Code: {self.error_code})"

    def __eq__(self, other):
        if isinstance(other, CodeException):
            return self.message == other.message and self.error_code == other.error_code
        return super().__eq__(other)