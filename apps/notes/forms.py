from apps.notes.models import Note
from core.forms import BaseModelForm


class NoteForm(BaseModelForm):

    class Meta:
        model = Note
        fields = ['title', 'content', 'tags']
