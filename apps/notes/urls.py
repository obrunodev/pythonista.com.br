from apps.notes import views
from django.urls import path


app_name = 'notes'
urlpatterns = [
    path('', views.NoteListView.as_view(), name='list'),
    path('create/', views.NoteCreateView.as_view(), name='create'),
    path('<int:pk>/detail/', views.NoteDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', views.NoteUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.NoteDeleteView.as_view(), name='delete'),

    # Folder views
    path(
        'folder/create/',
        views.FolderCreateView.as_view(),
        name='create_folder'
    ),
    path(
        'folder/<int:pk>/delete/',
        views.FolderDeleteView.as_view(),
        name='delete_folder'
    ),
]
