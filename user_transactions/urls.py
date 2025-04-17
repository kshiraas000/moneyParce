from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_transaction, name='add_transaction'),
    path('list/', views.transactions_list, name='transactions_list'),

]