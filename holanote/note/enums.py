from enum import Enum

class NoteStatusChoice(Enum):
    published = "published"
    draft = "draft"
    deleted = "deleted"

    @classmethod
    def choices(cls):
        return ((item.value, item.value) for item in cls)