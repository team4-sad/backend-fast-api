class InvalidScheduleException (Exception):
    def __str__(self):
        return f"Invalid schedule {self.tag=} {self.payload=}"

    def __init__(self, payload, tag: str, status_code: int):
        self.payload = payload
        self.tag = tag
        self.status_code = status_code

    @staticmethod
    def group(payload, status_code: int):
        return InvalidScheduleException(payload=payload, status_code=status_code, tag="group")

    @staticmethod
    def teacher(payload, status_code: int):
        return InvalidScheduleException(payload=payload, status_code=status_code, tag="teacher")

    @staticmethod
    def classroom(payload, status_code: int):
        return InvalidScheduleException(payload=payload, status_code=status_code, tag="classroom")
