from django.db import models
from django.db.models import Q


class FolderManager(models.Manager):

    def get_base_folders(self, request):
        if folder_id := request.GET.get('folder', ''):
            return self.filter(parent_folder__id=folder_id)
        return self.filter(parent_folder__isnull=True)


class NoteManager(models.Manager):

    def get_notes(self, request):
        """Recebe parâmetros de busca e retorna anotações filtradas."""
        if folder_id := request.GET.get('folder', ''):
            query_set = self.filter(parent_folder__id=folder_id)
        else:
            query_set = self.filter(parent_folder__isnull=True)

        if query_param := request.GET.get('q', ''):
            query_set = query_set.filter(
                Q(title__icontains=query_param) |
                Q(content__icontains=query_param),
            )

        if filter_param := request.GET.get('f', ''):
            query_set = query_set.filter(tags__name=filter_param)

        return query_set
