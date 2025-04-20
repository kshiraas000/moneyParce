from django.shortcuts import render, redirect
from .forms import TransactionForm

def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('user_transactions')
    else:
        form = TransactionForm()
    return render(request, 'user_transactions/add_transaction.html', {'form': form})
