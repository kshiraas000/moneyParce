from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(
        max_length=20,
        choices=[('deposit', 'Deposit'), ('withdrawal', 'Withdrawal')],
        default='deposit'  # ← Add this
    )
    category = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date = models.DateField(default=date.today)

    def __str__(self):
        return f"{self.user.username} - {self.amount} on {self.date}"
