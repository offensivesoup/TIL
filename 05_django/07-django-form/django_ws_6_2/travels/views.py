from django.shortcuts import render, redirect
from .models import Travel
from .forms import TravelForm


# Create your views here.
def index(request):
    travels = Travel.objects.all()
    context = {
        'travels' : travels
    }
    return render(request, 'travels/index.html', context)

def create(request):
    if request.method == "POST":
        travel = TravelForm(request.POST)
        if travel.is_valid():
            travel = travel.save()
            return redirect('travels:detail', travel.pk)
    else:
        form = TravelForm()
    context = {
        'form' : form
    }
    return render(request, 'travels/create.html', context)

def detail(request, travel_pk):
    travel = Travel.objects.get(pk = travel_pk)
    context = {
        'travel' : travel
    }
    return render(request, 'travels/detail.html', context)