from django.urls import path
from . import views

urlpatterns = [
    path('spending-report/', views.spending_report, name='reports.spending_report'),
]
