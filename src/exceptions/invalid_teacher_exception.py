class InvalidTeacherException (Exception):
    def __str__(self):
        return "Invalid teacher"

    def __init__(self, teacher_id: str):
        self.teacher_id = teacher_id
