from django import forms
from django.utils.translation import ugettext as _

from .models import MyUser


class LoginForm(forms.Form):
    email = forms.CharField(label=_('Email'))
    password = forms.CharField(
        label=_("Password"), widget=forms.PasswordInput())


class SignupForm(forms.Form):
    email = forms.CharField(label=_('Email'))
    password = forms.CharField(
        label=_("Password"), widget=forms.PasswordInput())
    password2 = forms.CharField(
        label=_("Password again"), widget=forms.PasswordInput())

    def clean_email(self):
        if MyUser.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError(_("User with this email already exists"))
        return self.cleaned_data['email']


class EditForm(forms.ModelForm):
    first_name = forms.CharField(label=_('First name'))
    last_name = forms.CharField(
        label=_("Last name"))
    nick = forms.CharField(label=_("Nick"))

    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'nick', 'avatar']
