from django.shortcuts import render, redirect
from .models import Article
from .forms  import ArticleForms


# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

def create(request):
    form = ArticleForms(request.POST)
    if request.method == "POST":
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForms()
    context = {
        'form' : form,
    }
    return render(request, 'articles/create.html', context)

def update(request,pk):
    article = Article.objects.get(pk = pk)
    if request.method == "POST":
        form = ArticleForms(request.POST, instance = article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForms(instance=article)
    context = {
        'form' : form,
        'article' : article
    }
    return render(request, 'articles/edit.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

# def new(request):
#     form = ArticleForms()
#     context = {
#         'form' : form
#     }
#     return render(request, 'articles/new.html', context)

# def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    # article = Article(title=title, content=content)
    form = ArticleForms(request.POST)
    ## 유효성 검사를 통과하면
    if form.is_valid():
        article = form.save()
        return redirect('articles:detail', article.pk)
    ## 유효성 검사를 통과하지 못하면??
    context = {
        'form' : form
    }
    
    return render(request, 'articles/new.html', context)

# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     form = ArticleForms(instance=article)
#     context = {
#         'article': article,
#         'form'  : form,
#     }
#     return render(request, 'articles/edit.html', context)

# def update(request, pk):
    article = Article.objects.get(pk=pk)
    form = ArticleForms(request.POST, instance = article)
    if form.is_valid():
        form.save()
        return redirect('articles:detail', article.pk)
    context = {
        'form' : form,
        'article' : article
    }
    return render(request, 'articles/edit.html', context)