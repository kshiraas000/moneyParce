from django.shortcuts import render, redirect, get_object_or_404
from .models import Transaction
from .forms import TransactionForm
from django.contrib.auth.decorators import login_required
from datetime import date

@login_required
def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('user_transactions:transactions_list')
    else:
        form = TransactionForm()
    return render(request, 'user_transactions/add_transaction.html', {'form': form})

@login_required
def transactions_list(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')
    return render(request, 'user_transactions/transactions_list.html', {'transactions': transactions})

@login_required
def edit_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            if not transaction.date:
                transaction.date = date.today()
            return redirect('user_transactions:transactions_list')

    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'user_transactions/edit_transactions.html', {'form': form})

@login_required
def delete_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
    transaction.delete()
    return redirect('user_transactions:transactions_list')

