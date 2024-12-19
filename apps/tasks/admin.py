from apps.tasks.models import Task
from django.contrib import admin


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_filter = ['status']
