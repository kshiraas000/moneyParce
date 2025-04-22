from django.db.models import Sum
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from register_income_spending.models import PlannedTransaction

@login_required
def spending_report(request):
    user_data = PlannedTransaction.objects.filter(user=request.user)

    # Total income vs spending
    income_total = user_data.filter(transaction_type='income').aggregate(Sum('amount'))['amount__sum'] or 0
    spending_total = user_data.filter(transaction_type='spending').aggregate(Sum('amount'))['amount__sum'] or 0

    bar_chart_data = [
        ['Category', 'Amount'],
        ['Income', float(income_total)],
        ['Spending', float(spending_total)],
    ]

    # Pie chart: spending breakdown by category
    spending_by_category = (
        user_data
        .filter(transaction_type='spending')
        .values('category')
        .annotate(total=Sum('amount'))
        .order_by('-total')
    )

    pie_chart_data = [['Category', 'Amount']]
    for entry in spending_by_category:
        pie_chart_data.append([entry['category'], float(entry['total'])])

    context = {
        'bar_chart_data': bar_chart_data,
        'pie_chart_data': pie_chart_data
    }

    return render(request, 'reports/spending_report.html', context)
