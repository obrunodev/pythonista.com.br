from apps.finance.forms import DebtForm, TransactionForm
from apps.finance.models import Debt, Transaction
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Q
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.utils import timezone
from shared.mappings import months_mapping


class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    context_object_name = 'transactions'
    paginate_by = 20

    def get_queryset(self):
        timezone_now = timezone.now()
        selected_month = timezone_now.month if not self.request.GET.get('month') else int(self.request.GET.get('month'))
        selected_year = timezone_now.year if not self.request.GET.get('year') else int(self.request.GET.get('year'))
        return Transaction.objects.filter(
            Q(due_date__month=selected_month, due_date__year=selected_year) |
            Q(is_permanent=True),
        )
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        selected_month = timezone.now().month if not self.request.GET.get('month') else int(self.request.GET.get('month'))
        selected_year = timezone.now().year if not self.request.GET.get('year') else int(self.request.GET.get('year'))
        context['change_month_href'] = {
            'previous': f'month=12&year={ selected_year - 1 }' if selected_month == 1 else f'month={ selected_month - 1}&year={ selected_year }',
            'actual': f'{months_mapping[selected_month]} de {selected_year}',
            'next': f'month=1&year={ selected_year + 1 }' if selected_month == 12 else f'month={ selected_month + 1}&year={ selected_year }',
        }
        month_balance = 0
        for t in self.get_queryset():
            if t.transaction_type == 'expense': month_balance -= t.value
            else: month_balance += t.value
        context['month_balance'] = month_balance
        return context


class TransactionCreateView(LoginRequiredMixin, CreateView):
    model = Transaction
    form_class = TransactionForm
    success_url = reverse_lazy('finance:transaction_list')


class DebtListView(ListView):
    model = Debt
    context_object_name = 'debts'
    paginate_by = 20

    def get_queryset(self):
        return Debt.objects.get_all_pending_debts()


class DebtCreateView(CreateView):
    model = Debt
    form_class = DebtForm
    success_url = reverse_lazy('finance:debt_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.generate_transations()
        return response
