from django.shortcuts import render, redirect
from .forms import KeywordForm
from .models import Keyword
from selenium import webdriver
from bs4 import BeautifulSoup
from .models import Keyword, Trend
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
import base64
# Create your views here.

def keyword(request):
    if request.method == 'POST':
        form = KeywordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trends:keyword')
    else:
        
        form = KeywordForm()
    
    keywords = Keyword.objects.all()
    context = {
        'form':form,
        'keywords':keywords,
    }
    return render(request, 'trends/keyword.html', context)

def delete(request, pk):
    keyword = Keyword.objects.get(pk=pk)
    keyword.delete()
    return redirect('trends:keyword')




def crawling(request):
    # 크롬 창 숨기기
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
   # Chrome webdriver 실행
    driver = webdriver.Chrome()
    # Keyword 테이블에서 모든 키워드 가져오기
    keywords = Keyword.objects.all()
    # 각 키워드에 대해 크롤링 실행
    for keyword in keywords:
        # 구글 검색 페이지 URL 생성
        search_url = f'https://www.google.com/search?q={keyword.name}'
        # 검색 결과 페이지 열기
        driver.get(search_url) 
        # 검색 결과 페이지 HTML 가져오기
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        # 검색 결과 개수 추출
        try:
            result_count_text = soup.select_one('#result-stats').text
            result_count  = int(result_count_text.split(' ')[2][:-1].replace(',',''))
        
        except:
            result_count = 0
        # 테이블에 저장

        trend, created = Trend.objects.get_or_create(
        name = keyword.name,
        search_period = 'all',
        defaults={
            'result': result_count,
            }
        )
        
        # Chrome webdriver 종료
        if not created:
            trend.result = result_count
            trend.save()
    driver.quit()
    trends = Trend.objects.all()
    context = {
        'trends' : trends
    }
    return render(request, 'trends/crawling.html', context)

def crawling_histogram(request):
    trends = Trend.objects.filter(search_period='all')

# 키워드와 검색 결과 개수를 각각 리스트에 저장합니다.
    keywords = [trend.name for trend in trends]
    results = [trend.result for trend in trends]

    # 막대 그래프를 출력합니다.
    plt.figure(figsize=(10, 6))
    plt.bar(keywords, results)
    plt.title('Technology Trend Analysis')
    plt.xlabel('Keyword')
    plt.ylabel('Result')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid()
    plt.legend(loc = 'upper right')
    buffer=BytesIO()
    plt.savefig(buffer, format='png')
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n','')
    buffer.close()
    context = {
        'img' : f'data:image/png;base64, {img_base64}'
    }
    return render(request, 'trends/crawling_histogram.html', context)

def crawling_advanced(request):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    # Chrome webdriver 실행
    driver = webdriver.Chrome()
    # Keyword 테이블에서 모든 키워드 가져오기
    keywords = Keyword.objects.all()
    # 각 키워드에 대해 크롤링 실행
    for keyword in keywords:
        # 구글 검색 페이지 URL 생성
        search_url = f'https://www.google.com/search?q={keyword.name}&tbs=qdr:y'
        # 검색 결과 페이지 열기
        driver.get(search_url) 
        # 검색 결과 페이지 HTML 가져오기
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        # 검색 결과 개수 추출
        try:
            result_count_text = soup.select_one('#result-stats').text
            result_count  = int(result_count_text.split(' ')[2][:-1].replace(',',''))
        
        except:
            result_count = 0
        # 테이블에 저장
        trend, created = Trend.objects.get_or_create(
        name = keyword.name,
        search_period = 'year',
        defaults={
            'result': result_count,
            }
        )
        
        # Chrome webdriver 종료
        if not created:
            trend.result = result_count
            trend.save()
    driver.quit()
    trends = Trend.objects.filter(search_period='year')
    # 키워드와 검색 결과 개수를 각각 리스트에 저장합니다.
    keywords = [trend.name for trend in trends]
    results = [trend.result for trend in trends]

    # 막대 그래프를 출력합니다.
    plt.figure(figsize=(10, 6))
    plt.bar(keywords, results)
    plt.title('Technology Trend Analysis')
    plt.xlabel('Keyword')
    plt.ylabel('Result')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid()
    plt.legend(loc = 'upper right')
    buffer=BytesIO()
    plt.savefig(buffer, format='png')
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n','')
    buffer.close()
    context = {
        'img' : f'data:image/png;base64, {img_base64}'
    }
    return render(request, 'trends/crawling_advanced.html', context)
    
        
        
        


