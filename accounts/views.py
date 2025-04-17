from django.shortcuts import render
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from .forms import CustomUserCreationForm, CustomErrorList
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UsernamePasswordResetForm, SetNewPasswordForm


@login_required
def logout(request):
    auth_logout(request)
    return redirect('home.index')
def login(request):
    template_data = {}
    template_data['title'] = 'Login'
    if request.method == 'GET':
        return render(request, 'accounts/login.html',
            {'template_data': template_data})
    elif request.method == 'POST':
        user = authenticate(
            request,
            username = request.POST['username'],
            password = request.POST['password']
        )
        if user is None:
            template_data['error'] = 'The username or password is incorrect.'
            return render(request, 'accounts/login.html',
                {'template_data': template_data})
        else:
            auth_login(request, user)
            return redirect('home.index')
def signup(request):
    template_data = {}
    template_data['title'] = 'Sign Up'
    if request.method == 'GET':
        template_data['form'] = CustomUserCreationForm()
        return render(request, 'accounts/signup.html',
            {'template_data': template_data})
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST, error_class=CustomErrorList)
        if form.is_valid():
            form.save()
            return redirect('accounts.login')
        else:
            template_data['form'] = form
            return render(request, 'accounts/signup.html',
                {'template_data': template_data})


def password_reset_request(request):
    if request.method == "POST":
        form = UsernamePasswordResetForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            request.session['reset_username'] = username  # Store username in session
            return redirect('password_reset')
    else:
        form = UsernamePasswordResetForm()

    return render(request, "accounts/password_reset_request.html", {"form": form})


def password_reset(request):
    username = request.session.get('reset_username', None)

    if not username:
        messages.error(request, "Invalid session. Please enter your username again.")
        return redirect('password_reset_request')

    if request.method == "POST":
        form = SetNewPasswordForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data['new_password']
            user = User.objects.get(username=username)
            user.set_password(new_password)
            user.save()
            messages.success(request, "Your password has been reset successfully!")
            del request.session['reset_username']  # Clear session
            return redirect('accounts.login')
    else:
        form = SetNewPasswordForm()

    return render(request, "accounts/password_reset.html", {"form": form})