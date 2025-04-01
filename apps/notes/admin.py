from apps.notes.models import Note, NoteTag, Folder
from django.contrib import admin


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    search_fields = ['title', 'content']


@admin.register(NoteTag)
class NoteTagAdmin(admin.ModelAdmin):
    list_display = ['name', 'color_class', 'used_count']
    readonly_fields = ['used_count']
    search_fields = ['name']

    def used_count(self, obj):
        return obj.note_set.count()


@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    ...
