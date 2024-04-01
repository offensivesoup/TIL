from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles 
    }
    return render(request, 'articles/index.html', context)

def new(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    form = ArticleForm()
    context = {
        'form' : form
    }
    return render(request, 'articles/new.html', context)
