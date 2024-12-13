from core.models import BaseModel
from django.db import models


class Note(BaseModel):
    title = models.CharField('Título', max_length=100, blank=True, null=True)
    content = models.TextField('Conteúdo')

    class Meta:
        verbose_name = 'Anotação'
        verbose_name_plural = 'Anotações'
    
    def __str__(self):
        if self.title: return self.title
        content = self.content[:30]
        if len(self.content) > 30:
            content = content + '...'
        return content
