class InvalidExamGroupException (Exception):
    def __str__(self):
        return "Invalid group ID"

    def __init__(self, group_id: str):
        self.group_id = group_id
