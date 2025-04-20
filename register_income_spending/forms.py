from django import forms
from .models import PlannedTransaction

class PlannedTransactionForm(forms.ModelForm):
    class Meta:
        model = PlannedTransaction
        fields = [
            'transaction_type',
            'amount',
            'category',
            'description',
            'date',
            'frequency',
        ]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }