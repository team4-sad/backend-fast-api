class LkException (Exception):
    def __str__(self):
        return f"Lk error: {str(self.origin)}"

    def __init__(self, origin: str):
        self.origin = origin
