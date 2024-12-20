from apps.chatbot.models import AgentAI
from core.forms import BaseModelForm
from django import forms


class AgentAIForm(BaseModelForm):

    class Meta:
        model = AgentAI
        fields = ['name', 'description', 'prompts']
