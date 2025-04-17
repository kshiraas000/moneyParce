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

# erm, in fact, all of base home was created by...
# ~ AEDAN, CHAPTER 2 :D ~