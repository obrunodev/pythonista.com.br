
from apps.tasks.models import Task
from apps.tasks.forms import TaskForm
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'

    def get_queryset(self):
        query_set = super().get_queryset()
        if query_param := self.request.GET.get('q'):
            query_set = query_set.filter(title__icontains=query_param)
        return query_set


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    
    def get_success_url(self):
        return reverse('tasks:list')


class TaskDetailView(DetailView):
    model = Task
    context_object_name = 'task'


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    
    def get_success_url(self):
        return reverse('tasks:list')


class TaskDeleteView(DeleteView):
    model = Task
    context_object_name = 'task'
    
    def get_success_url(self):
        return reverse('tasks:list')
