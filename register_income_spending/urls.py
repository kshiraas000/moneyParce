from django.urls import path
from . import views
app_name = 'register_income_spending'
urlpatterns = [
    path('', views.register_income_spending, name='register_income_spending'),
]