from django.shortcuts import render, redirect
from .forms import PlannedTransactionForm
from django.contrib.auth.decorators import login_required
from user_transactions.models import Transaction

@login_required
def register_income_spending(request):
    if request.method == 'POST':
        form = PlannedTransactionForm(request.POST)
        if form.is_valid():
            planned = form.save(commit=False)
            planned.user = request.user
            planned.save()

            # Create a corresponding Transaction
            transaction_category = 'Income' if planned.transaction_type == 'income' else 'Expense'

            Transaction.objects.create(
                user=request.user,
                category=transaction_category,
                amount=planned.amount,
                description=planned.description,
                date=planned.date
            )

            return redirect('user_transactions:transactions_list')
    else:
        form = PlannedTransactionForm()

    return render(request, 'register_income_spending/register_income_spending.html', {'form': form})