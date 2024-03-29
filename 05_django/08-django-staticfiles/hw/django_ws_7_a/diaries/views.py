from django.shortcuts import render, redirect
from .forms import DiaryForm
from .models import Diary

# Create your views here.
def index(request):
    diaries = Diary.objects.all()
    context = {
        'diaries': diaries,
    }
    return render(request, 'diaries/index.html', context)

def create(request):
    form = DiaryForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            diary = form.save()
            return redirect('diaries:index')
    else:
        form = DiaryForm()
    context = {
        'form' : form
    }
    return render(request, 'diaries/create.html', context)