from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    TRANSACTION_TYPES = [
        ('deposit', 'Deposit'),
        ('withdrawal', 'Withdrawal'),
    ]

    transaction_type = forms.ChoiceField(choices=TRANSACTION_TYPES)
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))  # Calendar picker

    class Meta:
        model = Transaction
        fields = ['transaction_type', 'amount', 'category', 'description', 'date']
