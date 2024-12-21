from django.urls import path
from . import views

app_name = 'chatbot'
urlpatterns = [
    path('', views.AgentAIListView.as_view(), name='list'),
    path('create/', views.AgentAICreateView.as_view(), name='create'),
    path('<int:pk>/agent/', views.AgentAIDetailView.as_view(), name='detail'),
    path('<int:agent_id>/get-answer/', views.agent_ai_answer, name='get_agent_answer'),
]