from apps.finance.models import Debt, Transaction
from core.forms import BaseModelForm


class DebtForm(BaseModelForm):

    class Meta:
        model = Debt
        fields = ['description', 'total_value', 'installment_count', 'first_due_date', 'is_paid', 'category']


class TransactionForm(BaseModelForm):

    class Meta:
        model = Transaction
        fields = ['transaction_type', 'description', 'category', 'value', 'due_date', 'is_permanent']
