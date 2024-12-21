from django.contrib.auth.models import User
from core.models import BaseModel
from django.db import models


class AgentAI(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField('Nome do agente', max_length=255)
    description = models.TextField('Descrição do agente')
    prompts = models.TextField('Prompts do agente')

    class Meta:
        ordering = ['name']
        verbose_name = 'Agente de IA'
        verbose_name_plural = 'Agentes de IA'
    
    def __str__(self):
        return self.name
    
    def get_system_context(self):
        return f'Você é o { self.name }. Uma descrição sobre você: { self.description }. Formas que deve agir: { self.prompts }'
    
    def get_message_logs(self):
        return self.agentaiconversationlog_set.all()[:10][::-1]
    
    def get_list_messages(self):
        return [{
            'role': log.role,
            'content': log.message,
        } for log in self.get_message_logs()]


class AgentAIConversationLog(BaseModel):
    agent = models.ForeignKey(AgentAI, on_delete=models.CASCADE)
    role = models.CharField(max_length=20)
    message = models.TextField()

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Histórico de conversa'
        verbose_name_plural = 'Históricos de conversa'
    
    def __str__(self):
        return '%s - %s: %s' % (
            self.agent, self.role, self.message
        )
