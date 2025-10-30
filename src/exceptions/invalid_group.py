class InvalidGroup (Exception):
    def __str__(self):
        return "Invalid group"

    def __init__(self, group_id: int):
        self.group_id = group_id
