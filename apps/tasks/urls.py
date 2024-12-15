from django.urls import path
from apps.tasks import views

app_name = 'tasks'
urlpatterns = [
    path('', views.TaskListView.as_view(), name='list'),
    path('create/', views.TaskCreateView.as_view(), name='create'),
    path('<int:pk>/detail/', views.TaskDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', views.TaskUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.TaskDeleteView.as_view(), name='delete'),
    path('change-status/', views.change_task_status, name='change_status'),
]
