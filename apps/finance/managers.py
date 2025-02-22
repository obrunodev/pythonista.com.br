from django.db import models
from django.db.models import Count, Q


class DebtManager(models.Manager):

    def get_all_pending_debts(self, request):
        """Retorna todas as dívidas pendentes, se houver filtro aplicado, retorna as dívidas filtradas."""
        debt_status = request.GET.get('debt_status') == 'paid'
        queryset = self.filter(is_paid=debt_status)
        return queryset.annotate(
            paid_transactions_count=Count(
                'transaction',
                filter=Q(transaction__is_paid=True)
            )
        )


class TransactionManager(models.Manager):

    def get_monthly_transactions(self, selected_month, selected_year):
        """Retorna todas as transações pendentes, se houver filtro aplicado, retorna as transações filtradas."""
        return self.filter(
            Q(due_date__month=selected_month, due_date__year=selected_year) |
            Q(is_permanent=True),
        )
