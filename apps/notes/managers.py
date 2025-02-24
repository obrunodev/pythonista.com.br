from django.db import models
from django.db.models import Q
from shared.utils import prettify_created_at


class NoteManager(models.Manager):

    def get_notes(self, request):
        queryset = self.get_queryset()

        if q := request.GET.get('q', ''):
            queryset = queryset.filter(
                Q(title__icontains=q) | Q(content__icontains=q),
            )
        
        if f := request.GET.get('f', ''):
            queryset = queryset.filter(tags__name=f)

        return queryset
    

    def get_public_notes(self, request):
        queryset = self.filter(is_public=True)
        if q := request.GET.get('q'):
            queryset = queryset.filter(
                Q(title__icontains=q) | Q(content__icontains=q),
            )
        for q in queryset:
            q.created_ago = prettify_created_at(q.created_at)
        return queryset
