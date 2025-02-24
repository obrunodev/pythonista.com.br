from apps.notes.models import Note, NoteTag
from apps.notes.forms import NoteForm
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


class NoteListView(LoginRequiredMixin, ListView):
    context_object_name = 'notes'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags_list'] = [tag.name for tag in NoteTag.objects.all()]
        return context

    def get_queryset(self):
        return Note.objects.get_notes(self.request)


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NoteForm
    
    def get_success_url(self):
        return reverse('notes:list')


class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note
    context_object_name = 'note'


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    form_class = NoteForm
    
    def get_success_url(self):
        return reverse('notes:list')


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    context_object_name = 'note'
    
    def get_success_url(self):
        return reverse('notes:list')


class PublicNotesListView(ListView):
    template_name = 'notes/public_note_list.html'
    context_object_name = 'notes'
    paginate_by = 20

    def get_queryset(self):
        return Note.objects.get_public_notes(self.request)
