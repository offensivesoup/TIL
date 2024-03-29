from django import forms
from .models import Article
# class ArticleForm(forms.Form):
#     title   = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea) ## 모델 필드가 아니라 max_length가 없어도 가능

class ArticleForms(forms.ModelForm):
    title = forms.CharField(
        label = "제목",
        widget = forms.TextInput(
            attrs = {
                'class' : 'my-title',
                'id' : 'aaa'
            }
        )
    )
    class Meta:
        model  = Article # 어떤 모델과 연동할건데?
        fields = '__all__' # 그 모델에서 어떤 필드를 쓸지?('title', 'content')
    

