from django.shortcuts import render
def index(request):
    return render(request, 'home/index.html')
def about(request):
    return render(request, 'home/about.html')

# erm, in fact, all of base home was created by...
# ~ AEDAN, CHAPTER 2 :D ~