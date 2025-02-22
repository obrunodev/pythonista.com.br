from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('users/', include('apps.users.urls')),
    path('admin/', admin.site.urls),
    path('chat/', include('apps.chatbot.urls')),
    path('finance/', include('apps.finance.urls')),
    path('notes/', include('apps.notes.urls')),
    path('tasks/', include('apps.tasks.urls')),
]

if settings.DEBUG is False:  # Apenas se DEBUG=False
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
