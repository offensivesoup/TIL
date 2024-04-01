from django import forms
from .models import Memo

class MemoForm(forms.ModelForm):
    class Meta:
        model = Memo
        fields = "__all__"
        widgets = {
            'content': forms.Textarea(
                attrs={
                    'cols': 50,
                    'rows': 5,
                    'placeholder': 'memo'
                }
            ),
            'Summary': forms.TextInput(
                attrs={
                    'placeholder': 'summary'
                }
            )
        }