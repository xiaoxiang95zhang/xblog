from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, UserInfo


class Login_Form(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirm password2", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "email")

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["self.password2"]:
            raise forms.ValidationError("password do not match")
        else:
            return cd["password2"]


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("phone", "birth")


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ("school", "company", "profession", "adress", "aboutme","photo")


class UserForm(forms.ModelForm):
    class Meta:
        fields = ("email",)

