from django import forms
from .models import Article

'''
    한가지 확실한건, class 에 상속 시켜줄 class 라는 점
    class -> pascalCase

    Form -> Model에 대한 정보가 없는 Form을 위한 클래스

    ModelForm -> Model에 대한 정보가 있는 Form을 위한 클래스

    Form vs ModelForm
'''
## 모델에 대한 정보 없이 Form을 구성하려면?
## 적절한 Field 들을 내가 직접 작성해 주어야 한다.
'''
HTML에서 쓸 form 태그를 구성해주는 class 인데...
field에 대한 정보가 없으면..? input tag 무엇을 써야할지 알 수 없다.
그래서 그 field 들 내가 정의한다.
정의하는 방법은 Model 정의하는거랑 똑같다
'''
class ArticleForm(forms.ModelForm):
    ## 필드명을 변수로
    title = forms.CharField(
        # form 내부에서 보여줄 input을 어떻게 정의할 것인가?
        # 어떤 input?
        # html 태그는 여러개의 속성
            # 이 속성을 쓰는 방법은
            # 속성명 = "값" -> 키: 벨류
        max_length = 100,
        widget= forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholeder' : '제목을 입력해 주세요'
            }
        ))
    content = forms.CharField(
        widget = forms.Textarea(
            attrs={
                'class' : 'form-control',
                'placeholeder' : '내용을 입력해 주세요'
            }
        )
    )
    ##  model로 부터 받아온다
    class Meta:
        model = Article
        fields = '__all__'
        '''
            내가 가진 field들 중에, 어떤 이름을 가진 필드들의
            속성만 간단하게 수정하고 싶어.
            field 각 이름은? 고유값 -> 가진 어떤 속성(value)
        '''
        widgets = {
            'is_hidden' : forms.RadioSelect(
                attrs = {
                    'class' : 'form-control',
                },
                choices = (
                    (True, '비공개'),(False, '공개')
                           )
            )
        }


