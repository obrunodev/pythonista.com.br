from apps.chatbot.models import AgentAI, AgentAIConversationLog
from django.contrib import admin


@admin.register(AgentAI)
class AgentAIAdmin(admin.ModelAdmin):
    ...


@admin.register(AgentAIConversationLog)
class AgentAIConversationLogAdmin(admin.ModelAdmin):
    ...
