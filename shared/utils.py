from django.utils.timezone import now

def prettify_created_at(created_at):
    """
    Retorna o tempo decorrido desde `created_at` em um formato amigável.
    """
    if created_at.tzinfo is None:
        raise ValueError("created_at deve ser um datetime timezone-aware")

    diferenca = now() - created_at

    if diferenca.total_seconds() < 60:
        return f"Há {int(diferenca.total_seconds())} segundos"
    elif diferenca.total_seconds() < 3600:
        minutos = int(diferenca.total_seconds() // 60)
        return f"Há {minutos} minuto{'s' if minutos > 1 else ''}"
    elif diferenca.total_seconds() < 86400:
        horas = int(diferenca.total_seconds() // 3600)
        return f"Há {horas} hora{'s' if horas > 1 else ''}"
    elif diferenca.days < 30:
        return f"Há {diferenca.days} dia{'s' if diferenca.days > 1 else ''}"
    elif diferenca.days < 365:
        meses = diferenca.days // 30
        return f"Há {meses} {'meses' if meses > 1 else 'mês'}"
    else:
        anos = diferenca.days // 365
        return f"Há {anos} ano{'s' if anos > 1 else ''}"

