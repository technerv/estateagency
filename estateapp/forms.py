from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    first_name = forms.CharField(label='First Name', widget=forms.TextInput)
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput)
    email = forms.EmailField(label='Email', widget=forms.EmailInput)
    username = forms.CharField(label='Username', widget=forms.TextInput)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

    def create(self, validated_data):
        password1 = validated_data.pop('password1',None)
        instance = self.Meta.model(**validated_data)

        if password1 is not None:
            instance.set_password(password1)
        instance.save()
        return instance

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)
