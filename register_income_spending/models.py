from django.db import models
from django.contrib.auth.models import User

FREQUENCY_CHOICES = [
    ('one-time', 'One-time'),
    ('weekly', 'Weekly'),
    ('biweekly', 'Biweekly'),
    ('monthly', 'Monthly'),
    ('custom', 'Custom'),
]

TRANSACTION_TYPE_CHOICES = [
    ('income', 'Income'),
    ('spending', 'Spending'),
]

class PlannedTransaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    date = models.DateField()
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES, default='one-time')
    created_at = models.DateTimeField(auto_now_add=True)