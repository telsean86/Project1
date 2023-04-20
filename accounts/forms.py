from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'password', 'password2', 'age',
                  'tel', 'address', 'style', 'email', 'postal_code')
        labels = {
            'id': '아이디',
            'password': '비밀번호',
        }
