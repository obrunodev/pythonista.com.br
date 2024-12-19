from django.db.models import QuerySet


class NoteService():

    @staticmethod
    def filter_notes(query_set: QuerySet, query_param: str = None, filter_param: str = None) -> QuerySet:
        """Recebe parâmetros de busca e retorna anotações filtradas."""
        if query_param:
            query_set = query_set.filter(title__icontains=query_param)
        
        if filter_param:
            query_set = query_set.filter(tags__name=filter_param)
        
        return query_set