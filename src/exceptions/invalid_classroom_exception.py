class InvalidClassroomException (Exception):
    def __str__(self):
        return "Invalid classroom"

    def __init__(self, classroom_id: str):
        self.classroom_id = classroom_id
