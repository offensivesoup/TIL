from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .models import User 해당 방식은 지양해야한다.

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # 현재 django 프로젝트에 활성화된 User 객체를 반환하는 함수
        model = get_user_model()

## 이건 회원정보 수정 페이지
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = (
                  'first_name',
                  'last_name',
                  'email',
                  )