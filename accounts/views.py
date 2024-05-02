from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.
def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if form.is_valid():
        user_ = form.get_user()
        login(request, user_)
        return redirect('/')
    context = {
        'form': form,
        'btn_label': 'Login',
        'title': 'Login'
    }
    return render(request, 'accounts/auth.html', context)
def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('/')
    context = {
        'form': form,
        'btn_label': 'Register',
        'title': 'Register'
    }
    return render(request, 'accounts/auth.html', context)

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')
    context = {
        'form': None,
        'btn_label': 'Logout',
        'description': 'Are you sure you want to logout?',
        'title': 'Logout'
    }
    return render(request, 'accounts/auth.html', context)


