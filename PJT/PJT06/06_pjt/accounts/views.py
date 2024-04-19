from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from boards.models import Board, Comment


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('boards:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("boards:index")
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)




def logout(request):
    auth_logout(request)
    return redirect('boards:index')



def profile(request, pk):
    author = get_user_model().objects.get(pk=pk)
    comments = Comment.objects.all().filter(author_id = author.pk)
    context = {
        'author': author,
        'comments': comments,
    }
    return render(request, 'accounts/profile.html', context)



def follow(request, pk):
    me = request.user
    you = get_user_model().objects.get(pk=pk)
    if me in you.followers.all():
        you.followers.remove(me)
    else:
        you.followers.add(me)
    return redirect('accounts:profile', you.pk)