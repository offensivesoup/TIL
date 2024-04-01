from django.shortcuts import render, redirect
from .models import Garage

# Create your views here.
def index(request):
    garages = Garage.objects.all()
    context = {
        'garages' : garages
    }
    return render(request, 'garages/index.html', context)

def new(request):
    return render(request, 'garages/new.html')

def create(request):
    location = request.POST.get('location')
    capacity = request.POST.get('capacity')
    is_parking_avaliable = request.POST.get('is_parking_avaliable')
    opening_time = request.POST.get('opening_time')
    closing_time = request.POST.get('closing_time')

    garage = Garage(location=location,capacity=capacity,is_parking_avaliable=is_parking_avaliable,opening_time=opening_time,closing_time=closing_time)
    garage.save()
    return redirect('garages:index')

def detail(request, garage_pk):
    ## pk 값이 사용자가 요청 보내온 pk 값을 가지고 있는 데이터 하나
    garage = Garage.objects.get(pk = garage_pk)
    context = {
        'garage' : garage
    }
    return render(request, 'garages/detail.html', context)
