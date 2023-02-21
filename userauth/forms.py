from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'name','adm_num' ,'password1', 'password2')


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('email', 'adm_num')
