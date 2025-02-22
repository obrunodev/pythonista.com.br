from apps.finance.managers import DebtManager, TransactionManager
from core.models import BaseModel
from django.db import models
from dateutil.relativedelta import relativedelta


class TransactionCategory(BaseModel):
    category = models.CharField('Nome da categoria', max_length=255)

    class Meta:
        ordering = ['category']
        verbose_name = 'Categoria de transação'
        verbose_name_plural = 'Categorias de transação'
    
    def __str__(self):
        return self.category


class Debt(BaseModel):
    description = models.CharField('Descrição da dívida', max_length=255)
    total_value = models.DecimalField('Valor total da dívida', max_digits=10, decimal_places=2)
    installment_count = models.PositiveIntegerField('Número de parcelas')
    first_due_date = models.DateField('Data de vencimento da 1ª parcela')
    is_paid = models.BooleanField('Está quitada?', default=False)
    category = models.ForeignKey(
        TransactionCategory,
        related_name='selected_debts',
        verbose_name='Categoria',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    objects = DebtManager()

    class Meta:
        ordering = ['-first_due_date']
        verbose_name = 'Dívida'
        verbose_name_plural = 'Dívidas'
    
    def __str__(self):
        return self.description
    
    def generate_transations(self):
        """Gera as transações para cada parcela da dívida"""
        installment_value = self.total_value / self.installment_count
        transactions = []

        for i in range(self.installment_count):
            due_date = self.first_due_date + relativedelta(months=i)
            transaction = Transaction(
                debt=self,
                transaction_type=Transaction.TransactionType.EXPENSE,
                value=installment_value,
                description=f'Parcela {i + 1}/{self.installment_count} - {self.description}',
                category=self.category,
                due_date=due_date,
            )
            transactions.append(transaction)
        
        Transaction.objects.bulk_create(transactions)


class Transaction(BaseModel):

    class TransactionType(models.TextChoices):
        INCOME = 'income', 'Entrada'
        EXPENSE = 'expense', 'Despesa'
    
    debt = models.ForeignKey(Debt, on_delete=models.CASCADE, blank=True, null=True)
    is_permanent = models.BooleanField('É permanente?', default=False)
    is_paid = models.BooleanField('Está pago?', default=False)
    transaction_type = models.CharField('Tipo', max_length=7, choices=TransactionType.choices)
    value = models.DecimalField('Valor', max_digits=10, decimal_places=2)
    description = models.CharField('Descrição da transação', max_length=255, blank=True, null=True)
    category = models.ForeignKey(
        TransactionCategory,
        related_name='selected_transactions',
        verbose_name='Categoria',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    due_date = models.DateField('Data de vencimento', blank=True, null=True)

    objects = TransactionManager()

    class Meta:
        ordering = ['-due_date']
        verbose_name = 'Transação'
        verbose_name_plural = 'Transações'
    
    def __str__(self):
        return f'{self.get_transaction_type_display()} - R$ {self.value}'
    
    def set_transaction_to_paid(self):
        """Marca a transação como quitada, e verifica se ela é vinculada a uma dívida."""
        self.is_paid = True
        self.save()

        if self.debt:  # Se possui débitos, verifica se todas as parcelas foram quitadas
            if not self.debt.transaction_set.filter(is_paid=False).exists():
                self.debt.is_paid = True
                self.debt.save()
