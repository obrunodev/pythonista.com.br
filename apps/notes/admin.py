from apps.notes.models import Note, NoteTag
from django.contrib import admin


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    search_fields = ['title', 'content']


@admin.register(NoteTag)
class NoteTagAdmin(admin.ModelAdmin):
    list_display = ['name', 'color_class']
    search_fields = ['name']
