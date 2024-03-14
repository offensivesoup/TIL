from django.shortcuts import render
from .models import Article
# Create your views here.

def create(request):
    article_1 = Article()
    article_1.title = '제목1'
    article_1.content = '내용1'
    article_1.save()
