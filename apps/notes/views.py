from apps.notes.models import Note
from apps.notes.forms import NoteForm
from apps.notes.helpers import context_helper
from apps.notes.services.note_service import NoteService
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    context_object_name = 'notes'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags_list'] = context_helper.get_tags_list()
        return context

    def get_queryset(self):
        return NoteService.filter_notes(
            query_set=super().get_queryset(),
            query_param=self.request.GET.get('q'),
            filter_param=self.request.GET.get('f'),
        )


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
