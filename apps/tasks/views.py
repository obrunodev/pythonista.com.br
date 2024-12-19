
from apps.tasks.helpers.context_helper import get_task_filter_context
from apps.tasks.models import Task
from apps.tasks.forms import TaskForm
from apps.tasks.services.task_service import TaskService
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_params'] = get_task_filter_context()
        return context

    def get_queryset(self):
        query_set = super().get_queryset()
        return TaskService.filter_tasks(
            query_set=query_set,
            query_param=self.request.GET.get('q'),
            filter_param=self.request.GET.get('f')
        )


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    
    def get_success_url(self):
        return reverse('tasks:list')


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    
    def get_success_url(self):
        return reverse('tasks:list')


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    
    def get_success_url(self):
        return reverse('tasks:list')


@login_required
def change_task_status(request):
    """
    Altera o status da tarefa de acordo com parâmetro enviado do frontend.
    """
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        next_status = request.POST.get('next_status')
        if next_status and task_id:
            task = Task.objects.filter(id=task_id).first()
            
            if not task:
                return redirect('tasks:list')
            
            task.status = next_status
            task.save()
        
        return redirect('tasks:list')
