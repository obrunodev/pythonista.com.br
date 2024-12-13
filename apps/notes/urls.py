from apps.notes import views
from django.urls import path


app_name = 'notes'
urlpatterns = [
    path('', views.NoteListView.as_view(), name='list'),
]

