from django.shortcuts import render, redirect
from .models import Movie 
from .forms import MovieForm

# Create your views here.
def index (request):
    movies = Movie.objects.all()
    context = {
        'movies' : movies
    }
    return render(request, 'movies/index.html', context)

def create(request):
    if request.method == 'POST':
        movieform = MovieForm(request.POST)
        if movieform.is_valid():
            movieform.save()
            return redirect('movies:index')
    else:
        movieform = MovieForm()
    context = {
        'movieform' : movieform,
    }
    return render(request, 'movies/create.html', context)