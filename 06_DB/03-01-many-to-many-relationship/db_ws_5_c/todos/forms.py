from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = '__all__'
        exclude = ('user', 'like_users',)
        widgets = {'is_completed': forms.HiddenInput()}