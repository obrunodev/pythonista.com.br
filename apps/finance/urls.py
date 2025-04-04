from django.urls import path
from apps.finance import views

app_name = 'finance'
urlpatterns = [
    path('transactions/', views.TransactionListView.as_view(), name='transaction_list'),
    path('transactions/create/', views.TransactionCreateView.as_view(), name='transaction_create'),
    path('transactions/<int:pk>/update/', views.TransactionUpdateView.as_view(), name='transaction_update'),
    path('transaction/<int:transaction_id>/is-paid/', views.TransactionIsPaidView.as_view(), name='transaction_is_paid'),

    path('debt/', views.DebtListView.as_view(), name='debt_list'),
    path('debt/create/', views.DebtCreateView.as_view(), name='debt_create'),
    path('debt/<int:pk>/', views.DebtDetailView.as_view(), name='debt_detail'),
]
