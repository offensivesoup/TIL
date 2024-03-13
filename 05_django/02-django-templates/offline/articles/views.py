from django.shortcuts import render

# Create your views here.
def index(request):
    # app에서 사용할 template는 templates 폴더에 넣는데
    # 왜... app/templates/app/*.html
    # 처럼 app 이름이 중복되도록 폴더 구조를 만들까
    '''
        만약... templates/*.html 로 만들었다면...
        app이 2개인 경우... articles와 accounts에서..
        articles/templates/index.html
        accounts/templates/index.html

        두 파일 중... 순회 순서에 따라서 먼저 발견하는 대상
        index.html 을 render 하게 되어버린다.

        그러면... 폴더를 그렇게 만들지 말고.. 파일명을..
        articles/templates/article_index.html
        accounts/templates/account_index.html
        이렇게 만들면 되는 거 아님?
        맞음!
        그런데 폴더로 관리하는게 더 깔끔함
    '''
    return render(request, 'articles/index.html')

def dtl_practice(request):
    lunch = ['타코야끼','치킨하이라이스','볶음우동','강식당라면','불백']
    empty_list = []
    context = {
        'lunch' : lunch,
        'empty_list' : empty_list
    }
    return render(request, 'articles/dtl-practice.html', context)

'''
    함수의 매개변수인데 ...
    그리고 url의 변수명인데 ...
    왜 두개는 항상 동일해야 하나?
    왜 매개변수의 값이 고정되어야 하나?
    그런 경우가 함수 정의할 떄 언제가 있지?
'''
def profile(request, username):
    context = {
        'username' : username
    }
    return render(request, 'articles/profile.html', context)

def numbers(request, num):
    context = {
        'num' : num
    }
    return render(request, 'articles/numbers.html', context)