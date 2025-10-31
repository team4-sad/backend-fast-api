class InvalidScheduleException (Exception):
    def __str__(self):
        return "Invalid schedule"

    def __init__(self, group_id: str, status_code: int):
        self.group_id = group_id
        self.status_code = status_code
