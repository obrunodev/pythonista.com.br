from apps.chatbot.models import AgentAI
from django.contrib import admin


@admin.register(AgentAI)
class AgentAIAdmin(admin.ModelAdmin):
    ...
