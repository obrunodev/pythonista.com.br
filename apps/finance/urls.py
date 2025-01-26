from django.urls import path
from apps.finance import views

app_name = 'finance'
urlpatterns = [
    path('transactions/', views.TransactionListView.as_view(), name='transaction_list'),
    path('transactions/create/', views.TransactionCreateView.as_view(), name='transaction_create'),

    path('debt/', views.DebtListView.as_view(), name='debt_list'),
    path('debt/create/', views.DebtCreateView.as_view(), name='debt_create'),
]
