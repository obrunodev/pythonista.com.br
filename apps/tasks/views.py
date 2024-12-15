
from apps.tasks.models import Task
from apps.tasks.forms import TaskForm
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'

    def get_queryset(self):
        query_set = super().get_queryset()
        query_set = query_set.exclude(status=Task.TaskStatus.DONE)
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
