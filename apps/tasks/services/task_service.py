from django.db.models import QuerySet
from apps.tasks.models import Task


class TaskService:

    @staticmethod
    def filter_tasks(query_set: QuerySet, query_param: str = None, filter_param: str = None):
        """
        Recebe parâmetros de busca, como texto e status, e retorna o query_set filtrado
        """
        if filter_param:
            query_set = query_set.filter(status=filter_param)
        else:
            query_set = query_set.exclude(status__in=[
                Task.TaskStatus.DONE,
                Task.TaskStatus.BACKLOG,
            ])
        
        if query_param:
            query_set = query_set.filter(title__icontains=query_param)
        
        return query_set
