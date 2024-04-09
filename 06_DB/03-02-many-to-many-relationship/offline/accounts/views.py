from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .form import CustomUserCreationForm
from .models import User

# Create your views here.

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save() # 사용자가 보낸 정보로 user를 생성한다.
            return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('accounts:profile', form.get_user().username)
    else:
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('accounts:login')

@login_required
def profile(request, username):
    profile_owner = User.objects.get(username = username)
    context = {
        'profile_owner' : profile_owner
    }
    return render(request, 'accounts/profile.html', context)

@login_required
def follow(request, profile_owner_pk):
    profile_owner = User.objects.get(pk=profile_owner_pk)
    me = request.user
    if me in profile_owner.followers.all():
        profile_owner.followers.remove(me)
    else:
        profile_owner.followers.add(me)
    return redirect('accounts:profile', profile_owner.username)

