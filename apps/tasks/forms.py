from apps.tasks.models import Task
from core.forms import BaseModelForm


class TaskForm(BaseModelForm):

    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date']
