from django.contrib import admin
from apps.finance.models import Debt, Transaction, TransactionCategory


@admin.register(Debt)
class DebtAdmin(admin.ModelAdmin):
    ...


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    ...


@admin.register(TransactionCategory)
class TransactionCategoryAdmin(admin.ModelAdmin):
    ...
