from apps.finance.forms import DebtForm, TransactionForm
from apps.finance.models import Debt, Transaction
from apps.finance.utils import get_month_balance, get_selected_month_year, get_month_navigation
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from django.views import View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect


class TransactionListView(LoginRequiredMixin, ListView):
    context_object_name = 'transactions'
    paginate_by = 20

    def get_queryset(self):
        selected_month, selected_year = get_selected_month_year(self.request)
        return Transaction.objects.get_monthly_transactions(selected_month, selected_year)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        selected_month, selected_year = get_selected_month_year(self.request)

        context['change_month_href'] = get_month_navigation(selected_month, selected_year)
        context['month_balance'] = get_month_balance(self.get_queryset())
        return context


class TransactionCreateView(LoginRequiredMixin, CreateView):
    model = Transaction
    form_class = TransactionForm
    success_url = reverse_lazy('finance:transaction_list')


class TransactionIsPaidView(LoginRequiredMixin, View):

    def post(self, request, transaction_id):
        transaction = get_object_or_404(Transaction, id=transaction_id)
        transaction.set_transaction_to_paid()
        return redirect('finance:transaction_list')


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
