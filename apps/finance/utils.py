from django.utils import timezone
from shared.mappings import months_mapping


def get_month_balance(transactions):
    """Retorna o balanço do mês."""
    month_balance = 0
    for t in transactions:
        if t.transaction_type == 'expense': month_balance -= t.value
        else: month_balance += t.value
    return month_balance


def get_selected_month_year(request):
    """Obtém o mês e o ano da query string ou usa o mês atual."""
    now = timezone.now()
    return (
        int(request.GET.get("month", now.month)),
        int(request.GET.get("year", now.year)),
    )

def get_month_navigation(selected_month, selected_year):
    return {
        'previous': f'month=12&year={ selected_year - 1 }' if selected_month == 1 else f'month={ selected_month - 1}&year={ selected_year }',
        'actual': f'{months_mapping[selected_month]} de {selected_year}',
        'next': f'month=1&year={ selected_year + 1 }' if selected_month == 12 else f'month={ selected_month + 1}&year={ selected_year }',
    }