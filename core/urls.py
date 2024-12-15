from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('users/', include('apps.users.urls')),
    path('admin/', admin.site.urls),
    path('chat/', include('apps.chatbot.urls')),
    path('notes/', include('apps.notes.urls')),
    path('tasks/', include('apps.tasks.urls')),
]
