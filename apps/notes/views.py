from apps.notes.models import Note
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


class NoteListView(ListView):
    model = Note
    context_object_name = 'notes'

