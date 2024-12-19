from apps.notes.models import NoteTag


def get_tags_list() -> list:
    return [tag.name for tag in NoteTag.objects.all()]
