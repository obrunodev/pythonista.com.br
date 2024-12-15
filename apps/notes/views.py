from apps.notes.models import Note
from apps.notes.forms import NoteForm
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    context_object_name = 'notes'
    paginate_by = 25

    def get_queryset(self):
        query_set = super().get_queryset()
        if query_param := self.request.GET.get('q'):
            query_set = query_set.filter(title__icontains=query_param)
        return query_set


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
