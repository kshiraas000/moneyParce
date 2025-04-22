from django.shortcuts import render
def index(request):
    template_data = {}
    template_data['title'] = 'Money Parse'
    return render(request, 'home/index.html', {
        'template_data': template_data})

def about(request):
    template_data = {}
    template_data['title'] = 'Financial Tips'
    return render(request,
                  'home/financial_tips.html',
                  {'template_data': template_data})

#aashna added code
def spending_report(request):
    data = [
        ['Category', 'Amount'],
        ['Income', 1200],
        ['Groceries', 300],
        ['Rent', 600],
        ['Entertainment', 150],
    ]
    context = {
        'chart_data': data
    }
    return render(request, 'home/spending_report.html', context)