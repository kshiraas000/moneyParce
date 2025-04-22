from django.urls import path
from .views import BudgetListView, BudgetCreateView, BudgetUpdateView, BudgetDeleteView

urlpatterns = [
    path('', BudgetListView.as_view(), name='budget-list'),
    path('new/', BudgetCreateView.as_view(), name='budget-create'),
    path('<int:pk>/edit/', BudgetUpdateView.as_view(), name='budget-edit'),
    path('<int:pk>/delete/', BudgetDeleteView.as_view(), name='budget-delete'),
]
