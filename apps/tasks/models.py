from apps.tasks.managers import TaskManager
from core.models import BaseModel
from django.db import models


class Task(BaseModel):

    class TaskStatus(models.TextChoices):
        BACKLOG = 'backlog', 'Backlog'
        TODO = 'todo', 'À fazer'
        DEVELOPMENT = 'development', 'Em desenvolvimento'
        DONE = 'done', 'Finalizado'

    title = models.CharField('Título', max_length=255)
    status = models.CharField('Status', max_length=100, choices=TaskStatus.choices, default=TaskStatus.BACKLOG)
    description = models.TextField('Descrição', blank=True, null=True)
    due_date = models.DateField('Data de entrega', blank=True, null=True)

    objects = TaskManager()

    class Meta:
        ordering = ['status', 'due_date']
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'

    def __str__(self):
        return self.title
