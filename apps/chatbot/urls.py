from django.urls import path
from . import views

app_name = 'chatbot'
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.AgentAIListView.as_view(), name='list'),
    path('create/', views.AgentAICreateView.as_view(), name='create'),
]