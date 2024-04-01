from django.shortcuts import render
from .forms import LoginForm
# Create your views here.
def login(request):
    loginForm = LoginForm()
    context = {
        'loginForm' : loginForm
    }
    return render(request, 'accounts/login.html', context)