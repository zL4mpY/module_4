from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        max_length=30,
        label='Логин',
        widget=forms.TextInput(attrs={'class':'form-control form-control-lg'}))
    
    name = forms.CharField(
        max_length=30,
        label='Ваше имя',
        widget=forms.TextInput(attrs={'class':'form-control form-control-lg'}))
    
    surname = forms.CharField(
        max_length=30,
        label='Фамилия',
        widget=forms.TextInput(attrs={'class':'form-control form-control-lg'}))
    
    password1 = forms.CharField(
        max_length=30,
        label='Введите пароль',
        widget=forms.TextInput(attrs={'class':'form-control form-control-lg'}))
    
    password2 = forms.CharField(
        max_length=30,
        label='Повторите пароль',
        widget=forms.TextInput(attrs={'class':'form-control form-control-lg'}))
    
    error_messages = {
        'password_too_short': 'Пароль слишком короткий. Он должен содержать не менее %(min_length)d символов.',
        'password_too_common': 'Пароль слишком простой. Пожалуйста, выберите более сложный пароль.',
        'password_entirely_numeric': 'Пароль не может состоять из цифр.',
        'password_validation_mismatch': 'Пароли не совпадают.',
    }

    class Meta:
        model = User
        fields = ("username", "name", "surname", "password1", "password2")
        labels = {
            'username': 'Логин',
            'name': 'Ваше имя',
            'surname': 'Фамилия',
            'password1': 'Введите пароль',
            'password2': 'Повторите пароль',
        }

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Пароли не совпадают.")