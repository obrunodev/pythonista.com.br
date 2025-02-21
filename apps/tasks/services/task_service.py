from django.db.models import QuerySet
from apps.tasks.models import Task


class TaskService:
    
    @staticmethod
    def set_next_task_status(query_set: QuerySet, next_status: str = None):
        """Passa a tarefa para o próximo status"""
        task = query_set.first()
        if task and next_status:
            task.status = next_status
            task.save()
            return True, 'success'
        return False, 'error'
