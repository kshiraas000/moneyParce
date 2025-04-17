from django.urls import path
from . import views
from .views import password_reset_request, password_reset

urlpatterns = [
    path('signup', views.signup, name='accounts.signup'),
    path('login/', views.login, name='accounts.login'),
    path('logout/', views.logout, name='accounts.logout'),
    path("password-reset-request/", password_reset_request, name="password_reset_request"),
    path("password-reset/", password_reset, name="password_reset"),
]