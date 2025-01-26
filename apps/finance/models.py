from core.models import BaseModel
from django.db import models


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

    class Meta:
        verbose_name = 'Dívida'
        verbose_name_plural = 'Dívidas'
    
    def __str__(self):
        return self.description


class Transaction(BaseModel):

    class TransactionType(models.TextChoices):
        INCOME = 'income', 'Entrada'
        EXPENSE = 'expense', 'Despesa'
    
    debt = models.ForeignKey(Debt, on_delete=models.CASCADE, blank=True, null=True)
    is_permanent = models.BooleanField('É permanente?', default=False)
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

    class Meta:
        ordering = ['-due_date']
        verbose_name = 'Transação'
        verbose_name_plural = 'Transações'
    
    def __str__(self):
        return f'{self.get_transaction_type_display()} - R$ {self.value}'
