from apps.notes.models import Note, Folder
from apps.notes.forms import NoteForm, FolderForm
from apps.notes.helpers import context_helper
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from urllib.parse import urlencode


class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    context_object_name = 'notes'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags_list'] = context_helper.get_tags_list()
        context['folders'] = Folder.objects.get_base_folders(self.request)
        context['selected_folder'] = Folder.objects.filter(
            id=self.request.GET.get('folder')
        ).first()
        return context

    def get_queryset(self):
        return Note.objects.get_notes(self.request)


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NoteForm

    def get_success_url(self):
        folder_id = self.request.POST.get('folder_id') or self.request.GET.get('folder_id')
        base_url = reverse('notes:list')
        query_string = f"?{urlencode({'folder': folder_id})}" if folder_id else ""
        return f"{base_url}{query_string}"

    def form_valid(self, form):
        if folder_id := self.request.POST.get('folder_id', ''):
            form.instance.parent_folder = Folder.objects.get(id=folder_id)
        return super().form_valid(form)


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


class FolderCreateView(CreateView):
    model = Folder
    form_class = FolderForm

    def get_success_url(self):
        folder_id = self.request.POST.get('folder_id') or self.request.GET.get('folder_id')
        base_url = reverse('notes:list')
        query_string = f"?{urlencode({'folder': folder_id})}" if folder_id else ""
        return f"{base_url}{query_string}"

    def form_valid(self, form):
        if folder_id := self.request.POST.get('folder_id', ''):
            form.instance.parent_folder = Folder.objects.get(id=folder_id)
        return super().form_valid(form)


class FolderDeleteView(DeleteView):
    model = Folder
    success_url = reverse_lazy('notes:list')
