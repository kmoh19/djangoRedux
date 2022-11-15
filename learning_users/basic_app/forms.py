from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo
from django.contrib.auth.password_validation import validate_password, password_validators_help_text_html


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), validators=[validate_password],
                               help_text=password_validators_help_text_html())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')


