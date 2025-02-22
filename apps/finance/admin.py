from django.contrib import admin
from apps.finance.models import Debt, Transaction, TransactionCategory


@admin.register(Debt)
class DebtAdmin(admin.ModelAdmin):
    ...


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['description', 'category', 'value', 'due_date']


@admin.register(TransactionCategory)
class TransactionCategoryAdmin(admin.ModelAdmin):
    ...
