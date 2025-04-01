from apps.notes.managers import FolderManager, NoteManager
from core.models import BaseModel
from django.db import models


class NoteTag(BaseModel):
    name = models.CharField('Nome da tag', max_length=100)
    color_class = models.CharField(
        'Classe Bootstrap para cor',
        max_length=20,
        help_text='Define uma classe para colorir os elementos. Ex.: primary, secondary, etc.'
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Tag de anotação'
        verbose_name_plural = 'Tags de anotação'

    def __str__(self):
        return self.name


class Folder(BaseModel):
    name = models.CharField('Nome da pasta', max_length=255)
    parent_folder = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='subfolders'
    )

    objects = FolderManager()

    class Meta:
        ordering = ['name']
        verbose_name = 'Pasta'
        verbose_name_plural = 'Pastas'

    def __str__(self):
        return self.name


class Note(BaseModel):
    parent_folder = models.ForeignKey(
        Folder,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='folder_notes'
    )
    title = models.CharField('Título', max_length=100, blank=True, null=True)
    content = models.TextField('Conteúdo')
    tags = models.ManyToManyField(NoteTag, blank=True)

    objects = NoteManager()

    class Meta:
        ordering = ['title']
        verbose_name = 'Anotação'
        verbose_name_plural = 'Anotações'

    def __str__(self):
        if self.title:
            return self.title
        content = self.content[:30]
        if len(self.content) > 30:
            content = content + '...'
        return content
