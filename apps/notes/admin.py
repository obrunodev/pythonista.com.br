from apps.notes.models import Note
from django.contrib import admin


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    search_fields = ['title', 'content']
