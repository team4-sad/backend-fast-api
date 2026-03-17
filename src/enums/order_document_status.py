import enum

class OrderDocumentStatus(enum.Enum):
    complete = 'complete'
    reject = 'reject'
    in_progress = 'in_progress'
