from apps.notes.models import Note, Folder
from core.forms import BaseModelForm


class NoteForm(BaseModelForm):

    class Meta:
        model = Note
        fields = ['title', 'content', 'tags']


class FolderForm(BaseModelForm):

    class Meta:
        model = Folder
        fields = ['name']
