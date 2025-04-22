from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Budget
from django.db.models import Sum

from user_transactions.models import Transaction


class BudgetListView(LoginRequiredMixin, ListView):
    model = Budget
    template_name = 'budgets/budget_list.html'

    def get_queryset(self):
        return Budget.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        budgets = context['object_list']

        budget_spending = {}
        budget_remaining = {}
        budget_percentage = {}

        total_budget = 0
        total_spent = 0

        for budget in budgets:
            spent = Transaction.objects.filter(
                user=self.request.user,
                category__iexact=budget.category
            ).aggregate(Sum('amount'))['amount__sum'] or 0

            remaining = budget.amount - spent
            percent = (spent / budget.amount * 100) if budget.amount > 0 else 0

            budget_spending[budget.id] = spent
            budget_remaining[budget.id] = remaining
            budget_percentage[budget.id] = min(percent, 100)

            total_budget += budget.amount
            total_spent += spent

        context['budget_spending'] = budget_spending
        context['budget_remaining'] = budget_remaining
        context['budget_percentage'] = budget_percentage
        context['total_budget'] = total_budget
        context['total_spent'] = total_spent
        context['total_remaining'] = total_budget - total_spent

        return context

class BudgetCreateView(LoginRequiredMixin, CreateView):
    model = Budget
    fields = ['category', 'amount']
    template_name = 'budgets/budget_form.html'
    success_url = reverse_lazy('budget-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BudgetUpdateView(LoginRequiredMixin, UpdateView):
    model = Budget
    fields = ['category', 'amount']
    template_name = 'budgets/budget_form.html'
    success_url = reverse_lazy('budget-list')

class BudgetDeleteView(LoginRequiredMixin, DeleteView):
    model = Budget
    template_name = 'budgets/budget_confirm_delete.html'
    success_url = reverse_lazy('budget-list')

