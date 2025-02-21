from django.db import models
from django.utils import timezone


class TaskManager(models.Manager):

    def get_tasks(self, request):
        """Retorna as tarefas do usuário, e um campo que não existe na model para definir se a task está atrasada, para ser estilizado no template."""
        today = timezone.now().date()
        queryset = self.all()
        if q := request.GET.get('q'): queryset = queryset.filter(title__icontains=q)
        if f := request.GET.get('f'):
            queryset = queryset.filter(status=f)
        else:
            queryset = queryset.exclude(status__in=['backlog', 'done'])
        for obj in queryset:
            if obj.due_date is None:
                obj.is_late = False
                continue
            obj.is_late = obj.due_date < today
        return queryset
