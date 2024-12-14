from apps.notes.models import Note
from apps.notes.forms import NoteForm
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


class NoteListView(ListView):
    model = Note
    context_object_name = 'notes'


class NoteCreateView(CreateView):
    model = Note
    form_class = NoteForm
    
    def get_success_url(self):
        return reverse('notes:list')


class NoteDetailView(DetailView):
    model = Note
    context_object_name = 'note'


class NoteUpdateView(UpdateView):
    model = Note
    form_class = NoteForm
    
    def get_success_url(self):
        return reverse('notes:list')


class NoteDeleteView(DeleteView):
    model = Note
    
    def get_success_url(self):
        return reverse('notes:list')
