from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm, CommentForm
# Create your views here.
# article 전체 정보를 pk 기준 오름차순 정렬
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

@login_required
def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit = False)
            article.user = request.user
            article.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form' : form
    }
    return render(request, 'articles/create.html', context)

@login_required
def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comment_form = CommentForm()
    context = {
        'article' : article,
        'comment_form' : comment_form
    }
    return render(request, 'articles/detail.html', context)

@login_required
def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.user == article.user:
        article.delete()
    return redirect('articles:index')
    
@login_required
def update(request, article_pk):
    article = Article.objects.get(pk = article_pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance = article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article_pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form' : form
    }
    return render(request, "articles/update.html", context)

def comment_create(request, article_pk, user_pk):
    article = Article.objects.get(pk = article_pk)
    comment_form = CommentForm(request.POST)
    if comment_form .is_valid():
        comment_form.save()
        return redirect('articles:detail', article.pk)
    context = {
        'article' : article,
        'comment_form' : comment_form,
    }
    return render(request, 'articles/detail.html', context)
    
    