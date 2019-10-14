from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import WikiModel


class WikiForm(ModelForm):
    class Meta:
        model = WikiModel
        fields = ['entryName', 'entryInfo']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "password"]


class ExistingUserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]
