from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Article
# Create your views here.
def index(request):
    ## 생성을 위한 요청은 두가지 작업
    articles = Article.objects.all().order_by('-pk') # p케이 순으로 내림\

    context  = {
        'articles' : articles
    } 
    return render(request, 'articles/index.html')

def create(request):
    '''
        1. 생성하기 위한 데이터를 입력할 수 있는 페이지
        2. 입력한 데이터를 실제 데이터를 생성하는 함수
    '''
    ## 사용자 요청 방식에 따라서 조건 분기
    if request.method == 'POST': # POST 요청이 오려면, GET 요청 처리가 먼저다
        form = ArticleForm(request.POST)
        if form.is_valid():
            ## 유효성 검사 메서드 통과 ## DB에 저장할 수 있을 것 같음
            ## 사용자가 보내온 데이터가 정의된 field에 삽입하기 적절하다.
            form.save()
            ## 모델에 article 을 연결 했으니 거기서 났다.
            ## 저장 다 했다
            return redirect('articles:index')
    else:
        # GET 요청이 들어왔을 때 article 생성할 수 있는 form을 랜더링한다
        form = ArticleForm()
    context = {
        'form' : form
    }
    return render(request, 'articles/create.html', context)
