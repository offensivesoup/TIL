from django.db import models

# Create your models here.
# class 를 상속받으면
    # -> 부모 클래스가 가진 각종 메서드, 속성 등을
    # -> 직접 정의하지 않아도 똑같이 사용 가능
class Article(models.Model):
    # 필드 정의
    # title 변수는? 무슨 변수?
    # 클래스 변수 -> 모든 인스턴스가 공통으로 가지는 속성
    title = models.CharField(max_length=150)
    # 글자수 제한 없는 문자열 공간 만들어 줄 수 있음
    content = models.TextField()
    # 자동으로 현재 시간을 생성된 시점에만, 
    created_at = models.DateTimeField(auto_now_add = True)
    # 자동으로 현재 시간을 매번
    updated_at = models.DateTimeField(auto_now = True)

'''
    파이썬(views.py) 파일에서 사용하기 편하게
    class로 DB의 모양을 정의하고, 그 class 의 instance 값들을 다룰것
    DB에 class로 만든 데이터 schema를 실제 테이블로 만들려면?
    그건 SQL로 만들어야 한다.
    django 가 알아서 해준다. => makemigrations, migrate
    실제로 클래스의 내용을 DB에 테이블로 만들려면, 필요한 추가 설정과 내용이 더 있다.
    -> migrate()
'''

# # Article 클래스의 인스턴스를 생성한다.
# article_1 = Article()
# # 이때의 title 은, 인스턴스 article_1 의 속성 title
# article_1.title = '제목1'
# article_1.content = '내용1'

# # 동일한 규칙이 적용된다.
# article_2 = Article()
# article_2.title = 'article_1.title 과 똑같은 규칙 적용'
# article_2.content = '내용2'