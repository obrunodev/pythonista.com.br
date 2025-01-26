from apps.finance.forms import DebtForm, TransactionForm
from apps.finance.models import Debt, Transaction
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.utils import timezone


class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    context_object_name = 'transactions'
    paginate_by = 20

    def get_queryset(self):
        timezone_now = timezone.now()
        return Transaction.objects.filter(
            due_date__month=timezone_now.month,
            due_date__year=timezone_now.year,
        )


class TransactionCreateView(LoginRequiredMixin, CreateView):
    model = Transaction
    form_class = TransactionForm
    success_url = reverse_lazy('finance:transaction_list')


class DebtListView(ListView):
    model = Debt
    context_object_name = 'debts'
    paginate_by = 20


class DebtCreateView(CreateView):
    model = Debt
    form_class = DebtForm
    success_url = reverse_lazy('finance:debt_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.generate_transations()
        return response
