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
